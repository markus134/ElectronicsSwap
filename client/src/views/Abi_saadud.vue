<template>
  <div class="min-h-screen flex items-center justify-center background text-3xl">
    <div class="bg-white flex flex-col p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full items-center">
      <p class="mb-6">Varsti sinuga võetakse ühendust.</p>
      <button @click="login" class="button-background text-white py-2 px-4 max-w-xl rounded-xl">
        Tagasi esilehele
      </button>
    </div>
  </div>
</template>

<script>
import router from "@/router/index.js";

export default {
  methods: {
    login() {
      router.push('/');
    }
  }
};
</script>

<style scoped>
.background {
  background-image: url("../assets/background.png");
}
.button-background {
  background-color: #b4beef;
}
</style>
