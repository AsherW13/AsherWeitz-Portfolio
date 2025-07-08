<script setup>
import NavBar from './components/NavBar.vue'
import About from './components/About.vue'
import Projects from './components/Projects.vue';
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
    <section id="experience" class="scroll-mt-24">
      <!-- <About /> -->
    </section>
    <section id="contact" class="scroll-mt-24">
      <!-- <About /> -->
    </section>
  </main>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
