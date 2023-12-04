<template>
  <div class="min-h-screen flex flex-col background">
    <Navbar />
    <div class="flex flex-col justify-center h-screen items-center">
      <div class="text-5xl mb-8 w-3/5">Q&A</div>
      <div class="flex flex-col bg-white shadow-2xl w-3/5 h-1/2">
        <div class="flex flex-col bg-white items-center p-4 text-3xl h-full">
          <textarea
            v-model="feedback"
            :class="{ 'border-red-500': !feedbackValidationPassed }"
            placeholder="Kirjuta oma küsimus siia"
            class="p-2 border-2 border-gray mt-2 transition-all duration-300 w-full rounded-xl h-full"
            style="resize: none"
          ></textarea>
          <button
              @click="submitFeedback"
              class="button-background text-white py-2 px-4 mt-4 rounded-md max-w-2xl"
          >
            Saada
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
      this.feedbackValidationPassed = this.feedback.trim() !== '';

      if (this.feedbackValidationPassed) {
        console.log("Küsimus: " + this.feedback);
        router.push("/abi_saadud");
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
  transition: border-color 0.3s ease-in-out;
}
</style>
