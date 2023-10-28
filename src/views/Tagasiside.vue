<template>
  <div class="min-h-screen flex flex-col">
    <!-- Navigation Bar -->
    <div class="p-4">
      <div class="flex justify-between items-center">
        <!-- Bigger ElectronicsSwap button -->
        <button class="nav-button" style="font-size: 1.5rem; padding: 1rem;">ElectronicsSwap</button>
        <div class="flex space-x-4 items-center">
          <button class="nav-button">Laenutamine</button>
          <button class="nav-button">Vahetus</button>
          <button class="nav-button">Loo pakkumine</button>
          <button class="nav-button">Ostukorv</button>
          <!-- Circular container for user picture -->
          <div class="h-10 w-10 rounded-full overflow-hidden">
            <!-- Placeholder for user picture or an actual image source -->
            <img src="@/assets/man.jpg" alt="User Picture" class="h-full w-full object-cover" />
          </div>
          <button class="nav-button">Username</button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
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
export default {
  data() {
    return {
      feedback: '',
    };
  },
  methods: {
    submitFeedback() {
      console.log("Feedback: " + this.feedback);
      // Add logic to send feedback to your backend or perform any other actions
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

.nav-button {
  background-color: transparent;
  border: none;
  color: #2d3748;
  cursor: pointer;
  margin-right: 10px; /* Adjust the margin as needed */
}

.nav-button:hover {
  background-color: #e2e8f0; /* Light gray for hover effect */
}
</style>
