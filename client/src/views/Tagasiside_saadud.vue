<template>
  <div class="min-h-screen flex items-center justify-center background">
    <div class="bg-white flex flex-col p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full text-center">
      <p class="text-base mb-6 text-lg">Aitäh tagasiside eest!</p>
      <button @click="login" class="button-background text-white font-regular py-2 px-4 rounded">
        Mine laenutamise lehele
      </button>
    </div>
  </div>
</template>

<script>
import router from "@/router/index.js";

export default {
  methods: {
    login() {
      router.push('/laenutamine');
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
