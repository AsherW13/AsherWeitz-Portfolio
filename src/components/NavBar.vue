<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Bars3Icon, XMarkIcon, EnvelopeIcon } from '@heroicons/vue/24/outline'

const menuOpen = ref(false)
const showShadow = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const scrollToSection = (id) => {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
    menuOpen.value = false
  }
}

const handleScroll = () => {
  showShadow.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
    <nav
    :class="[
      'w-full fixed top-0 left-0 z-50 bg-gray-50 transition-shadow duration-300',
      showShadow ? 'shadow' : ''
    ]"
    >
    <div class="flex items-center justify-between px-6 py-4">

      <div class="w-1/3 font-bold text-2xl pl-10">Asher Weitz</div>

      <ul class="hidden md:flex justify-center w-1/3 space-x-8 text-xl">
        <li><button @click="scrollToSection('about')" class="hover:text-indigo-500 hover:underline hover:underline-offset-3">About</button></li>
        <li><button @click="scrollToSection('projects')" class="hover:text-indigo-500 hover:underline hover:underline-offset-3">Projects</button></li>
        <li><button @click="scrollToSection('experience')" class="hover:text-indigo-500 hover:underline hover:underline-offset-3">Experience</button></li>
        <li><button @click="scrollToSection('contact')" class="hover:text-indigo-500 hover:underline hover:underline-offset-3">Contact</button></li>
      </ul>

      <div class="w-1/3 hidden md:flex justify-end items-center space-x-4 pr-10">
        <a href="https://linkedin.com/in/asher-weitz" target="_blank" aria-label="LinkedIn">
          <FontAwesomeIcon :icon="['fab', 'linkedin']"  size="2x" class="w-6 h-6 hover:text-indigo-500" />
        </a>
        <a href="https://github.com/AsherW13" target="_blank" aria-label="GitHub">
          <FontAwesomeIcon :icon="['fab', 'github']"  size="2x" class="w-6 h-6 hover:text-indigo-500" />
        </a>
        <a href="mailto:asherfweitz@gmail.com" aria-label="Email">
          <EnvelopeIcon class="w-8 h-8 hover:text-indigo-500" />
        </a>
      </div>

      <button @click="toggleMenu" class="md:hidden focus:outline-none">
        <Bars3Icon v-if="!menuOpen" class="w-6 h-6" />
        <XMarkIcon v-else class="w-6 h-6" />
      </button>
    </div>

    <div v-if="menuOpen" class="md:hidden px-6 pb-4 flex flex-col space-y-4 text-lg">
      <button @click="scrollToSection('about')" class="text-left hover:text-indigo-500">About</button>
      <button @click="scrollToSection('projects')" class="text-left hover:text-indigo-500">Projects</button>
      <button @click="scrollToSection('experience')" class="text-left hover:text-indigo-500">Experience</button>
      <button @click="scrollToSection('contact')" class="text-left hover:text-indigo-500">Contact</button>
      <div class="flex space-x-4 mt-2">
        <a href="https://linkedin.com/in/asher-weitz" target="_blank" aria-label="LinkedIn">
          <FontAwesomeIcon :icon="['fab', 'linkedin']" class="w-6 h-6 hover:text-indigo-500" />
        </a>
        <a href="https://github.com/AsherW13" target="_blank" aria-label="GitHub">
          <FontAwesomeIcon :icon="['fab', 'github']" class="w-6 h-6 hover:text-indigo-500" />
        </a>
        <a href="mailto:asherfweitz@gmail.com" aria-label="Email">
          <EnvelopeIcon class="w-6 h-6 hover:text-indigo-500" />
        </a>
      </div>
    </div>
  </nav>
</template>



<style scoped>
.read-the-docs {
  color: #888;
}
</style>
