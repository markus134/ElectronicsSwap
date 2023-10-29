<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <div class="flex-grow flex items-center justify-center background mt-8">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4">
        <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
        <div class="text-center">
          <p class="font-regular">Siia saad lisada oma tagasiside</p>
          <textarea v-model="feedback" placeholder="Kirjuta oma tagasiside siia" class="w-full p-2 border-2 border-black mt-2"></textarea>
          <button @click="submitFeedback" class="button-background text-white py-2 px-4 mt-4 rounded-md font-regular">Saada tagasiside</button>
        </div>
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
  data() {
    return {
      feedback: '',
    };
  },
  methods: {
    submitFeedback() {
      console.log("Feedback: " + this.feedback);
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
</style>
