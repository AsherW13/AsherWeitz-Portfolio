<template>
  <section class="relative z-10 overflow-hidden bg-white dark:bg-dark py-20 lg:py-[120px]">
    <div class="container mx-auto">
      <div class="flex flex-col items-center justify-center px-4">
        <div class="mb-8 text-center">
          <span class="block text-2xl font-semibold text-primary">Contact Me!</span>
        </div>

        <div class="w-full max-w-[570px]">
          <div class="relative p-8 bg-white rounded-lg shadow-lg dark:bg-dark-2 sm:p-12">
            <form>
              <div class="mb-6">
                <input
                  type="text"
                  placeholder="Your Name"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none"
                />
              </div>
              <div class="mb-6">
                <input
                  type="email"
                  placeholder="Your Email"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none"
                />
              </div>
              <div class="mb-6">
                <input
                  type="text"
                  placeholder="Your Phone"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none"
                />
              </div>
              <div class="mb-6">
                <textarea
                  rows="6"
                  placeholder="Your Message"
                  class="border-stroke dark:border-dark-3 dark:text-dark-6 dark:bg-dark text-body-color focus:border-primary w-full resize-none rounded border py-3 px-[14px] text-base outline-none"
                ></textarea>
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

</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>