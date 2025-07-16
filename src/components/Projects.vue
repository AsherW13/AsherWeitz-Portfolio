<template>
  <section class="p-4 bg-gray-50">
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      <div
        v-for="project in projects"
        :key="project.id"
        class="bg-gray-50 shadow rounded-lg p-4 flex flex-col justify-between max-w-sm w-full mx-auto"
      >
        <div class="flex flex-col justify-between items-center">
          <h2 class="text-xl font-semibold mb-2">{{ project.title }}</h2>
          <p class="mb-4">{{ project.description }}</p>
          <div class="border-t border-gray-800 pt-4 mt-2 w-full text-center">
            <a
            :href="project.link"
            target="_blank"
            rel="noopener noreferrer"
            class="text-blue-600 hover:underline mt-auto"
            >
            Link for project
            </a>
          </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script setup>
  const projects = [
    {
      id: 1,
      title: "Raspberry Pi LED Display",
      description: "This project turns a Raspberry Pi with a Sense HAT into a remote-controlled pixel canvas. Users can draw in real time on the 8×8 LED display using a web interface built with Flask and Socket.IO. The Pi’s joystick also supports drawing locally, including color selection and pixel clearing. The system runs as a systemd service, automatically launching the server on boot. This project showcases full-stack integration, real-time communication, and embedded hardware control.",
      link: "https://youtu.be/iVVlPMUDpDQ"
    },
    {
      id: 2,
      title: "SpaceX Launch Viewer",
      description: "SpaceX Launch Viewer is a frontend project built with Vue.js and Bootstrap that fetches and displays SpaceX launch data using their public API. It features a dynamic carousel of launch videos, a year-based filter dropdown, and a synchronized launch list. Users can easily browse recent and historical launches, with visual highlighting that syncs the video carousel and list items. This project helped me deepen my understanding of DOM manipulation, reactive UI design, and REST API integration in a modern JavaScript framework.",
      link: "https://github.com/AsherW13/LearnFrontend"
    },
    {
      id: 3,
      title: "RF Chamber Software Design",
      description: "This senior design project modernized Itron's RF chamber testing software by consolidating two legacy applications (Visual Basic and LabView) into a single, multithreaded C++ program with a Qt-based GUI. The software controls instruments including a turntable, 3D rotator, antenna, spectrum analyzer, and vector network analyzer to perform automated 3D RF measurements. We added support for the Prologix USB-to-GPIB adapter, enabling instrument control from modern laptops without the need of legacy desktops. The application also features real-time data visualization with 2D and 3D polar graphs, enhanced logging, and debugging tools for improved test control. This unified tool enables engineers to run high- and low-frequency RF tests",
      link: "/CS2507_Expo_Poster.pdf"
    }
  ]
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>