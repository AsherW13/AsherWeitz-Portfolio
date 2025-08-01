<template>
  <section class="relative z-10 overflow-hidden bg-white dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-col items-center justify-center px-4">
        <div class="mb-8 text-center">
          <span class="block text-2xl font-semibold text-primary">Contact Me!</span>
        </div>

        <div class="w-full max-w-[570px]">
          <div class="relative p-8 bg-white rounded-lg shadow-lg dark:bg-dark-2 sm:p-12">
            <form @submit.prevent="submitForm">
              <div class="mb-6">
                <input
                  v-model="form.name"
                  type="text"
                  placeholder="Your Name"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none"
                  required
                />
              </div>
              <div class="mb-6">
                <input
                  v-model="form.email"
                  type="email"
                  placeholder="Your Email"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none"
                  required
                />
              </div>
              <div class="mb-6">
                <textarea
                  v-model="form.message"
                  rows="6"
                  placeholder="Your Message"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full resize-none rounded border py-3 px-[14px] text-base outline-none"
                  required
                ></textarea>
              </div>

              <div class="mb-6">
                <div
                  class="g-recaptcha"
                  :data-sitekey="siteKey"
                  style="min-height: 78px"
                ></div>
                <p v-if="recaptchaError" class="text-red-600 text-sm mt-2">{{ recaptchaError }}</p>
              </div>

              <div>
                <button
                  type="submit"
                  class="w-full p-3 text-white transition border rounded border-primary bg-primary hover:bg-opacity-90"
                >
                  Send Message
                </button>
              </div>
            </form>
            <div>
              <span class="absolute -top-10 -right-9 z-[-1]">
                <svg
                  width="100"
                  height="100"
                  viewBox="0 0 100 100"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M0 100C0 44.7715 0 0 0 0C55.2285 0 100 44.7715 100 100C100 100 100 100 0 100Z"
                    fill="#3056D3"
                  />
                </svg>
              </span>
              <span class="absolute -bottom-10 -left-9 z-[-1]" style="transform: scaleX(-1) rotate(90deg);">
                <svg
                  width="100"
                  height="100"
                  viewBox="0 0 100 100"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M0 100C0 44.7715 0 0 0 0C55.2285 0 100 44.7715 100 100C100 100 100 100 0 100Z"
                    fill="#3056D3"
                  />
                </svg>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script setup>
import { ref } from 'vue'

const form = ref({ name: '', email: '', message: '' })
const recaptchaError = ref('')
const siteKey = import.meta.env.VITE_RECAPTCHA_SITE_KEY
const apiUrl = import.meta.env.VITE_API_URL

const submitForm = async () => {
  recaptchaError.value = ''

  if (typeof grecaptcha === 'undefined') {
    recaptchaError.value = 'reCAPTCHA not loaded. Please refresh the page.'
    return
  }

  const token = grecaptcha.getResponse()
  if (!token) {
    recaptchaError.value = 'Please complete the reCAPTCHA.'
    return
  }

  try {
    const response = await fetch(`${apiUrl}/api/contact`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: form.value.name,
        email: form.value.email,
        message: form.value.message,
        recaptcha: token,
      }),
    })

    const data = await response.json()

    if (response.ok) {
      alert(data.message)
      form.value = { name: '', email: '', message: '' }
      grecaptcha.reset() // reset widget after successful submission
    } else {
      const errorMsg = data.errors
        ? Object.entries(data.errors).map(([k, v]) => `${k}: ${v.join(', ')}`).join('\n')
        : data.message || 'Submission failed'
      alert(errorMsg)
    }
  } catch (err) {
    console.error('Submission error:', err)
    alert('An error occurred. Please try again later.')
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>