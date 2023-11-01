<template>
  <div class="min-h-screen flex items-center justify-center background">
    <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
      <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
      <p class="text-base mb-6 text-lg">Registreerimine</p>
      <div class="bg-red-200 h-16 w-full rounded mb-4 text-center p-5 text-red-900" v-if="error">
        <p>{{ error }}</p>
      </div>
      <form @submit.prevent="register">
        <div class="mb-6">
          <label for="username" class="block font-medium mb-3 text-base">Nimi</label>
          <input
            type="text"
            id="username"
            v-model="user.username"
            :class="{ 'border-red-500': !usernameValidationPassed }"
            placeholder="Kirjuta oma nimi"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="mb-6">
          <label for="email" class="block font-medium mb-3 text-base">Email</label>
          <input
            type="email"
            id="email"
            v-model="user.email"
            :class="{ 'border-red-500': !emailValidationPassed }"
            placeholder="Kirjuta oma email"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="mb-6">
          <label for="password" class="block font-medium mb-3 text-base">Parool</label>
          <input
            type="password"
            id="password"
            v-model="user.password"
            :class="{ 'border-red-500': !passwordValidationPassed }"
            placeholder="Kirjuta oma parool"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="control-group mb-5">
          <label class="control control-checkbox">
            Olen nõus platvormi tingimustega
            <input type="checkbox" checked="checked" id="accept_toc" v-model="accept_toc" class="rounded-md" />
            <div class="control_indicator"></div>
          </label>
        </div>
        <div class="flex items-center justify-center mb-8">
          <button
            type="submit"
            @click.prevent="register"
            class="button-background text-white py-2 px-4 w-full rounded-md"
          >
            Registreeri
          </button>
        </div>
        <div class="text-center pb-4">
          <p>Kas on konto olemas? <a href="/login" class="font-medium">Logi sisse</a></p>
        </div>
      </form>
    </div>
  </div>
</template>



<script>
import { useAuthStore } from '../store/modules/auth';
import {ref} from 'vue';
import router from '@/router';

export default {
  setup () {
    const authStore = useAuthStore()
    const user = ref({
      username: "",
      email: "",
      password: "",
    });

    let accept_toc = ref(false);
    let usernameValidationPassed = ref(true);
    let passwordValidationPassed = ref(true);
    let emailValidationPassed = ref(true);
    let error = ref("");

    const register = async () => {
      // Check username, email, password, and conditions
      usernameValidationPassed.value = user.value.username.trim() !== "";
      passwordValidationPassed.value = user.value.password.trim() !== "";
      let fail = false;

      if (!usernameValidationPassed.value || !passwordValidationPassed.value) {
        error.value = "You haven't set your password or username"
        fail = true
      }
    
      validateEmail()
      
      if (!emailValidationPassed.value) {
        error.value = "Your email is incorrect"
        fail = true
      }

      if (!accept_toc.value) {
        error.value = "You haven't accepted our terms and conditions"
        fail = true
      }

      if (!fail) {
        const response = await authStore.registerUser(user.value);
        if (response === "Successful") {
          router.push('/laenutamine')
        }
        else {
          error.value = response
        }
      }
    }
    const validateEmail = async () => {
      emailValidationPassed.value = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(user.value.email);
    }
    return {authStore, register, user, usernameValidationPassed, passwordValidationPassed, emailValidationPassed, accept_toc, error}
  }
}
</script>


<style scoped>
.button-background {
  background-color: #b4beef;
}

#accept_toc {
  transform: scale(2);
  accent-color: #b4beef;
}
.control {
  font-family: arial;
  display: block;
  position: relative;
  padding-left: 30px;
  margin-bottom: 5px;
  padding-top: 3px;
  cursor: pointer;
  font-size: 16px;
}
.control input {
  position: absolute;
  z-index: -1;
  opacity: 0;
}
.control_indicator {
  position: absolute;
  top: 2px;
  left: 0;
  height: 20px;
  width: 20px;
  background: #e1e1e1;
  border: 0px solid #000000;
  border-radius: 5px;
}
.control:hover input ~ .control_indicator,
.control input:focus ~ .control_indicator {
  background: #e1e1e;
}
.control input:checked ~ .control_indicator {
  background: #b4beef;
}
.control:hover input:not([disabled]):checked ~ .control_indicator,
.control input:checked:focus ~ .control_indicator {
  background: #b4beef;
}
.control input:disabled ~ .control_indicator {
  background: #e6e6e6;
  opacity: 0.6;
  pointer-events: none;
}
.control_indicator:after {
  box-sizing: unset;
  content: '';
  position: absolute;
  display: none;
}
.control input:checked ~ .control_indicator:after {
  display: block;
}
.control-checkbox .control_indicator:after {
  left: 8px;
  top: 4px;
  width: 3px;
  height: 8px;
  border: solid #fbfbfb;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
.control-checkbox input:disabled ~ .control_indicator:after {
  border-color: #7b7b7b;
}
.border-red-500 {
  border-color: #ef4444;
}

.background {
  background-image: url("../assets/background.png");
}
</style>
