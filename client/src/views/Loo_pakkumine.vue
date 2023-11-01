<template>
  <Navbar />
  <div class="background">
  <div class="text-4xl font-bold mb-8 p-4 ml-28 background">Loo pakkumine</div>
  <div class="flex flex-col items-center justify-center background">
    <div class="bg-white p-8 rounded shadow-2xl w-5/6 h-4/5 min-h-full">
      <div class="text-xl">
        <input
          v-model="productTitle"
          placeholder="Kirjuta toote tiitel"
          class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
        />
      </div>
    </div>
    <div class="p-4"></div>
    <div class="flex bg-white rounded shadow-2xl w-5/6 h-4/5 min-h-full">
      <button
        :class="{ 'button-active': selectedButton === 'kirjeldus' }"
        @click="openWindow('kirjeldus')"
        class="flex-grow button-background text-xl p-8 text-white w-full"
      >
        Kirjeldus
      </button>
      <button
        :class="{ 'button-active': selectedButton === 'materjalid' }"
        @click="openWindow('materjalid')"
        class="flex-grow button-background text-xl p-8 text-white w-full"
      >
        Materjalid
      </button>
      <button
        :class="{ 'button-active': selectedButton === 'tehniline_info' }"
        @click="openWindow('tehniline_info')"
        class="flex-grow button-background text-xl p-8 text-white w-full"
      >
        Tehniline Info
      </button>
    </div>
    <div class="flex bg-white rounded shadow-2xl w-5/6 h-4/5">
      <textarea
        v-if="selectedButton === 'kirjeldus'"
        v-model="kirjeldus"
        placeholder="Siia saad lisada kirjelduse"
        class="w-full h-40 p-2"
      ></textarea>
      <textarea
        v-if="selectedButton === 'materjalid'"
        v-model="materjalid"
        placeholder="Siia saad lisada materjalide info"
        class="w-full h-40 p-2"
      ></textarea>
      <textarea
        v-if="selectedButton === 'tehniline_info'"
        v-model="tehnilineInfo"
        placeholder="Siia saad lisada tehnilise info"
        class="w-full h-40 p-2"
      ></textarea>
    </div>
    <div class="p-2"></div>
    </div>
    <div class="flex flex-row justify-center">
    <div class="flex bg-white rounded shadow-2xl w-1/6 h-4/5 mt-4 p-4 ml-32">
      <div class="flex items-center">
        <span class="mr-2">Hind:</span>
        <textarea v-model="price" placeholder='hind' class="ml-2 w-24 h-10 p-2"></textarea>
        <span class="ml-2">eur/kuus</span>
      </div>
    </div>
    <div class="flex bg-white rounded shadow-2xl w-1/6 h-4/5 mt-4 p-4 ml-auto mr-32">
        <button class="button-background w-full h-full p-2 ml-2">Loo pakkumine</button>
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
      productTitle: "",
      selectedButton: "kirjeldus",
      kirjeldus: "",
      materjalid: "",
      tehnilineInfo: "",
      price: "",
    };
  },
  methods: {
    openWindow(button) {
      this.selectedButton = button;
    },
  },
};
</script>

<style scoped>
.background {
  background-image: url("../assets/background.png");
}

.button-background {
  background-color: #b4beef;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.button-active {
  background-color: #b4bfff;
}

/* Red border style with smooth transition */
.border-red-500 {
  border-color: #b4beef;
  transition: border-color 0.3s ease-in-out;
}
</style>
