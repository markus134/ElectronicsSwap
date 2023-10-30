<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <div class="flex-grow flex items-center justify-center background mt-8">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4">
        <h1 class="text-2xl font-semibold mb-4">Vahetus</h1>
        <div class="">Vahetus tuleb meie veebilehele aastal 2044.</div>
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
