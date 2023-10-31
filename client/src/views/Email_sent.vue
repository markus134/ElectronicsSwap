<template>
    <div class="min-h-screen flex items-center justify-center background">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
        <p class="text-base mb-6 text-lg">Sinu e-mailile on saadetud e-kiri kasutajanime parooliga</p>
        <form @submit.prevent="login">
          <div class="flex items-center justify-center mb-8">
            <button type="submit" class="button-background text-white py-2 px-4 w-full rounded-md">Logi sisse</button>
          </div>
         
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import router from "@/router/index.js";

  export default {
    methods: {
      login() {
        router.push("/login");
      }
    }
  };
  </script>

<style scoped>
.button-background {
    background-color: #b4beef;
}

.background {
  background-image: url("../assets/background.png");
}
</style>
  