<template>
  <div class="min-h-screen flex items-center justify-center background">
    <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-4/5 min-h-full">
      <h1 class="text-2xl font-semibold mb-4">ElectronicsSwap</h1>
      <p class="text-base mb-6 text-lg">Parooli taastamine</p>
      <form @submit.prevent="forgot_password">
        <div class="mb-6">
          <input
            type="email"
            id="email"
            v-model="email"
            placeholder="Kirjuta oma email"
            :class="{ 'border-red-500': emailValidationFailed }"
            class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
          />
        </div>
        <div class="flex items-center justify-center mb-8">
          <button
            type="submit"
            class="button-background text-white py-2 px-4 w-full rounded-md"
          >
            Taasta
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      emailValidationFailed: false,
    };
  },
  methods: {
    forgot_password() {
      if (this.email.trim() === "") {
        this.emailValidationFailed = true;
      } else {
        // Redirect to /email_sent
        this.$router.push("/email_sent");
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
}
</style>
