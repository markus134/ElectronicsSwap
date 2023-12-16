<template>
  <div class="min-h-screen flex items-center justify-center background text-xl">
    <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
      <p class="mb-10 text-center">Makse õnnestus. Toote pakkuja varsti võtab sinuga ühendust.</p>
        <div class="flex items-center justify-center mb-8">
          <button @click="redirectToLogin" class="button-background text-white py-2 px-4 w-full rounded-md">Vaata teisi pakkumisi</button>
        </div>
        <div class="flex items-center justify-center mb-4">
          <button @click="redirectToTagasiside" class="button-background text-white py-2 px-4 w-full rounded-md">Jäta tagasiside</button>
        </div>
    </div>
  </div>
</template>

<script>
import router from "../router/index.js";

export default {
  methods: {
    redirectToLogin() {
      router.push('/laenutamine')
    },
    redirectToTagasiside() {
      router.push('/tagasiside')
    },
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
