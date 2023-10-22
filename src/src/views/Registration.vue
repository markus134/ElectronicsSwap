<template>
    <div class="min-h-screen flex items-center justify-center background">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
        <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
        <p class="text-base mb-6 text-lg">Registreerimine</p>
        <form @submit.prevent="register">
          <div class="mb-6">
            <label for="username" class="block font-medium mb-3 text-base">Nimi</label>
            <input type="text" id="username" v-model="username" placeholder="Kirjuta oma nimi" class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300">
          </div>
          <div class="mb-6">
            <label for="email" class="block font-medium mb-3 text-base">Email</label>
            <input type="email" id="email" v-model="email" placeholder="Kirjuta oma email" class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300">
          </div>
          <div class="mb-6">
            <label for="password" class="block font-medium mb-3 text-base">Parool</label>
            <input type="password" id="password" v-model="password" placeholder="Kirjuta oma parool" class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300">
          </div>
          <div class="m-4 text-left">
            <!--Default checkbox-->
            <input type="checkbox" id="accept_toc" v-model="accept_toc" class="mr-4">
            <label>Olen nõus platvormi tegevustega</label>
           
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
        password: '',
        accept_toc: false
      };
    },
    methods: {
      register() {
        console.log("Username: " + this.username);
        console.log("Email: " + this.email)
        console.log("Password: " + this.password);
        console.log("Accepts conditions: " + this.accept_toc)
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
  