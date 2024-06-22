<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main class="relative flex items-center justify-center min-h-screen overflow-hidden">
    <img src="@/assets/social.jpg" alt="Welcome Image" class="absolute inset-0 w-full h-full object-cover z-0">

  </main>
</template>

<style scoped>
.main {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  overflow: hidden;
}

img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

h1 {
  z-index: 10;
  color: white; /* Make text white for better contrast on the image */
}
</style>





