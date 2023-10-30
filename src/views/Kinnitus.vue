<template>
  <div class="min-h-screen flex items-center justify-center background">
    <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
      <p class="text-base mb-6 text-lg">Makse õnnestus. Toote pakkuja varsti võtab sinuga ühendust.</p>
      <form @submit.prevent>
        <div class="flex items-center justify-center mb-8">
          <button @click="redirectToLogin" class="button-background text-white py-2 px-4 w-full rounded-md">Mine tagasi</button>
        </div>
        <div class="flex items-center justify-center mb-8">
          <button @click="redirectToTagasiside" class="button-background text-white py-2 px-4 w-full rounded-md">Jäta tagasiside</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import router from "@/router/index.js";

export default {
  methods: {
    redirectToLogin() {
      router.push('/login')
    },
    redirectToTagasiside() {
      router.push('/tagasiside')
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
