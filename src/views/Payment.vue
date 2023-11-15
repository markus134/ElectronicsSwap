<template>
    <div class="min-h-screen flex flex-col">
      <div class="mb-32">
      <Navbar />
      </div>
      <p class="ml-16 font-medium text-2xl">TODO</p>
    </div>
  </template>
  
  <script>
  import Navbar from "@/components/Navbar.vue";
  
  export default {
      components: {
      Navbar,
    }
  }
  </script>
  