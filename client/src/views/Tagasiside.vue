<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <div class="flex-grow flex items-center justify-center background mt-8">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4">
        <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
        <div class="text-center">
          <p class="font-regular">Siia saad lisada oma tagasiside</p>
          <textarea
            v-model="feedback"
            :class="{ 'border-red-500': !feedbackValidationPassed }"
            placeholder="Kirjuta oma tagasiside siia"
            class="w-full p-2 border-2 border-black mt-2 transition-all duration-300"
          ></textarea>
          <button
            @click="submitFeedback"
            class="button-background text-white py-2 px-4 mt-4 rounded-md w-full font-regular"
          >
            Saada tagasiside
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import router from "@/router/index.js";

export default {
  components: {
    Navbar,
  },
  data() {
    return {
      feedback: '',
      feedbackValidationPassed: true,
    };
  },
  methods: {
    submitFeedback() {
      // Check if feedback is empty
      this.feedbackValidationPassed = this.feedback.trim() !== '';

      // Perform feedback submission logic if validation passes
      if (this.feedbackValidationPassed) {
        console.log("Feedback: " + this.feedback);
        router.push("/tagasiside2");
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

/* Red border style with smooth transition */

.border-red-500 {
  border-color: #ef4444;
  transition: border-color 0.3s ease-in-out;
}
</style>
