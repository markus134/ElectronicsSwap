<template>
    <div class="min-h-screen flex items-center justify-center bg-neutral-200">
      <div class="bg-white p-8 rounded shadow-md w-2/4 h-4/5 min-h-full">
        <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
        <p class="text-base mb-6 text-lg">Sisselogimine</p>
        <form @submit.prevent="login">
          <div class="mb-6">
            <label for="username" class="block font-medium mb-3 text-base">Nimi</label>
            <input type="text" id="username" v-model="username" placeholder="Kirjuta oma nimi" class="w-full p-2 border bg-neutral-200">
          </div>
          <div class="mb-6">
            <label for="password" class="block font-medium mb-3 text-base">Parool</label>
            <input type="password" id="password" v-model="password" placeholder="Kirjuta oma parool" class="w-full p-2 border bg-neutral-200">
          </div>
          <div class="m-4 text-right">
            <a href="/forgot_password" class="font-thin">Unustasid oma parooli?</a>
          </div>
          <div class="flex items-center justify-center mb-8">
            <button type="submit" class="button-background text-white py-2 px-4 w-full">Logi sisse</button>
          </div>
          <div class="text-center pb-4">
            <p>Kas pole veel kontot? <a href="/registration" class="font-medium">Registreeri</a></p>
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
        password: ''
      };
    },
    methods: {
      login() {
        console.log("Username: " + this.username);
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
  