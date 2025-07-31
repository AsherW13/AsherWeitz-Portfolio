import os
import smtplib
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from email.message import EmailMessage
from dotenv import load_dotenv
from form import ContactForm
from flask_wtf.csrf import CSRFProtect, CSRFError

import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

CORS(app)

limiter = Limiter(get_remote_address, app=app, default_limits=["2 per hour"])

csrf = CSRFProtect(app)

@app.route("/api/contact", methods=["POST"])
@limiter.limit("2 per hour")
def contact():
    data = request.get_json()

    app.logger.info(f"Incoming JSON data: {data}")

    form = ContactForm(data=data)

    if not form.validate():
        app.logger.error(f"Validation errors: {form.errors}")
        return jsonify({"message": "Validation failed", "errors": form.errors}), 400

    recaptcha_token = data.get("recaptcha", "")
    if not recaptcha_token:
        return jsonify({"message": "Missing reCAPTCHA token"}), 400

    recaptcha_response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={
            "secret": os.getenv("RECAPTCHA_SECRET"),
            "response": recaptcha_token
        }
    ).json()

    if not recaptcha_response.get("success"):
        return jsonify({"message": "Invalid reCAPTCHA. Please try again."}), 403

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio Contact from {form.name.data}"
    msg["From"] = os.getenv("EMAIL_SENDER")
    msg["To"] = os.getenv("EMAIL_RECEIVER")
    msg.set_content(f"From: {form.name.data} <{form.email.data}>\n\n{form.message.data}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASSWORD"))
            smtp.send_message(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        print("SMTP Error:", e)
        return jsonify({"message": "Failed to send email"}), 500

if __name__ == "__main__":
    app.run()
