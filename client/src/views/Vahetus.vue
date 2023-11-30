<template>
  <div class="min-h-screen flex flex-col background">
    <Navbar />
    <div class="flex flex-col h-screen items-center justify-center">
      <div class="text-5xl mb-8 w-2/3">Vahetus</div>
      <div class="bg-white p-8 rounded shadow-2xl w-2/3 text-3xl">
        <div class="">Vahetus tuleb meie veebilehele aastal 2044. Loodetavasti...</div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style scoped>
.background {
  background-image: url("../assets/background.png");
}
</style>
