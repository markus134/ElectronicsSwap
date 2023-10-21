<template>
    <div class="min-h-screen flex items-center justify-center bg-neutral-200">
      <div class="bg-white p-8 rounded shadow-md w-2/4 h-4/5 min-h-full">
        <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
        <p class="text-base mb-6 text-lg">Registreerimine</p>
        <form @submit.prevent="register">
          <div class="mb-6">
            <label for="username" class="block font-medium mb-3 text-base">Nimi</label>
            <input type="text" id="username" v-model="username" placeholder="Kirjuta oma nimi" class="w-full p-2 border bg-neutral-200">
          </div>
          <div class="mb-6">
            <label for="email" class="block font-medium mb-3 text-base">Email</label>
            <input type="email" id="email" v-model="email" placeholder="Kirjuta oma email" class="w-full p-2 border bg-neutral-200">
          </div>
          <div class="mb-6">
            <label for="password" class="block font-medium mb-3 text-base">Parool</label>
            <input type="password" id="password" v-model="password" placeholder="Kirjuta oma parool" class="w-full p-2 border bg-neutral-200">
          </div>
          <div class="m-4 text-left">
            <p class="font-thin">Olen nõus platvormi tingimustega</p>
          </div>
          <div class="flex items-center justify-center mb-8">
            <button type="submit" class="button-background text-white py-2 px-4 w-full">Registreeri</button>
          </div>
          <div class="text-center pb-4">
            <p>Kas on konto olemas? <a href="/login" class="font-medium">Logi sisse</a></p>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: ''
      };
    },
    methods: {
      register() {
        console.log("Username: " + this.username);
        console.log("Email: " + this.email)
        console.log("Password: " + this.password);
      }
    }
  };
  </script>

<style scoped>
.button-background {
    background-color: #484848;
}
</style>
  