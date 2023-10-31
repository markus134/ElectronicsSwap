<template>
  <div class="min-h-screen flex items-center justify-center background">
    <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
      <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
      <p class="text-base mb-6 text-lg">Sisselogimine</p>
      <form @submit.prevent="login">
        <div class="mb-6">
          <label for="username" class="block font-medium mb-3 text-base">Nimi</label>
          <input
            type="text"
            id="username"
            v-model="username"
            :class="{ 'border-red-500': !usernameValidationPassed }"
            placeholder="Kirjuta oma nimi"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block font-medium mb-3 text-base">Parool</label>
          <input
            type="password"
            id="password"
            v-model="password"
            :class="{ 'border-red-500': !passwordValidationPassed }"
            placeholder="Kirjuta oma parool"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="m-4 text-right">
          <a href="/forgot_password" class="font-thin">Unustasid oma parooli?</a>
        </div>
        <div class="flex items-center justify-center mb-8">
          <button
            type="submit"
            class="button-background text-white py-2 px-4 w-full rounded-md"
          >
            Logi sisse
          </button>
        </div>
        <div class="text-center pb-4">
          <p>Kas pole veel kontot? <a href="/registration" class="font-medium">Registreeri</a></p>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import router from "@/router/index.js";

export default {
  data() {
    return {
      username: '',
      password: '',
      usernameValidationPassed: true,
      passwordValidationPassed: true,
    };
  },
  methods: {
    login() {
      // Check username and password
      this.usernameValidationPassed = this.username.trim() !== "";
      this.passwordValidationPassed = this.password.trim() !== "";

      // Perform login logic if both username and password are valid
      if (this.usernameValidationPassed && this.passwordValidationPassed) {
        console.log("Username: " + this.username);
        console.log("Password: " + this.password);
        router.push('/laenutamine')
      }
    },
  },
};
</script>

<style scoped>
.button-background {
  background-color: #b4beef;
}

.background {
  background-image: url("../assets/background.png");
}
.border-red-500 {
  border-color: #ef4444;
}
</style>
