<script setup>
import NavBar from './components/NavBar.vue'
import About from './components/About.vue'
import Projects from './components/Projects.vue'
import Contact from './components/Contact.vue'
</script>

<template>
  <div class="p-10 px-20 bg-gray-50">
    <NavBar />
  </div>
  <main class="bg-gray-50">
    <section id="about" class="scroll-mt-24">
      <About />
    </section>
    <section id="projects" class="scroll-mt-24">
      <Projects />
    </section>
    <section id="contact" class="scroll-mt-24">
      <Contact />
    </section>
  </main>
</template>

