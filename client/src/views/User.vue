<template>
  <div class="min-h-screen flex flex-col ml-16">
    <Navbar />
    <div class="mt-10">
      <div class="flex flex-row">
        <img src="../assets/user.png" alt="User image">
        <div class="flex flex-col ml-10">
          <p class="font-medium text-lg mt-2">Usaldusväärsus - keskmine</p>
          <p class="mt-2 font-medium text-6xl">MINGI KASUTAJA</p>
        </div>
        <div class="flex-grow"></div>
        <button class="self-center button-background text-white py-4 px-4 w-2/12 rounded-md mr-12">
          Uuenda andmeid
        </button>
      </div>
    </div>
    <div class="mt-16">
      <p class="font-medium text-xl">Kontaktandmed</p>
      <p class="mt-4">kasutaja@gmail.com</p>
      <p class="font-medium text-xl mt-8">Minu kirjeldus</p>
      <p class="mt-4">Olen juba selle platvormi kasutaja 3 aastat, palju häid hinnanguid. Seadmeid ei vaheta</p>
    </div>

    <div class="mt-16">
      <p class="font-medium text-xl">Mida mina pakun</p>
      <div class="flex flex-row mt-8">
        <div class="product h-96 w-80 mb-20 flex flex-col justify-between items-start relative">
          <div class="flex-grow"></div>
          <p class="text-white ml-5 text-xl">Käekellad</p>
          <p class="text-gray-400 ml-5 mt-3">Siin on mingi kirjeldus nendele ägedatele käekelladele</p>

          <div class="flex flex-row ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md">Lisa</button>
            <div class="flex-grow"></div>
            <p class="text-white self-center absolute right-0 mr-6">13 EUR/kuus</p>
          </div>
        </div>
        <div class="product ml-6 h-96 w-80 mb-20 flex flex-col justify-between items-start relative">
          <div class="flex-grow"></div>
          <p class="text-white ml-5 text-xl">Käekellad</p>
          <p class="text-gray-400 ml-5 mt-3">Siin on mingi kirjeldus nendele ägedatele käekelladele</p>

          <div class="flex flex-row ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md">Lisa</button>
            <div class="flex-grow"></div>
            <p class="text-white self-center absolute right-0 mr-6">13 EUR/kuus</p>
          </div>
        </div>
        <div class="product ml-6 h-96 w-80 mb-20 flex flex-col justify-between items-start relative">
          <div class="flex-grow"></div>
          <p class="text-white ml-5 text-xl">Käekellad</p>
          <p class="text-gray-400 ml-5 mt-3">Siin on mingi kirjeldus nendele ägedatele käekelladele</p>

          <div class="flex flex-row ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md">Lisa</button>
            <div class="flex-grow"></div>
            <p class="text-white self-center absolute right-0 mr-6">13 EUR/kuus</p>
          </div>
        </div>
        <div class="product ml-6 h-96 w-80 mb-20 flex flex-col justify-between items-start relative">
          <div class="flex-grow"></div>
          <p class="text-white ml-5 text-xl">Käekellad</p>
          <p class="text-gray-400 ml-5 mt-3">Siin on mingi kirjeldus nendele ägedatele käekelladele</p>

          <div class="flex flex-row ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md">Lisa</button>
            <div class="flex-grow"></div>
            <p class="text-white self-center absolute right-0 mr-6">13 EUR/kuus</p>
          </div>
        </div>
        <div class="product ml-6 h-96 w-80 mb-20 flex flex-col justify-between items-start relative">
          <div class="flex-grow"></div>
          <p class="text-white ml-5 text-xl">Käekellad</p>
          <p class="text-gray-400 ml-5 mt-3">Siin on mingi kirjeldus nendele ägedatele käekelladele</p>

          <div class="flex flex-row ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md">Lisa</button>
            <div class="flex-grow"></div>
            <p class="text-white self-center absolute right-0 mr-6">13 EUR/kuus</p>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-16">
      <p class="font-medium text-xl">Mida ma teistele hetkel laenan</p>
      <div class="flex flex-row mt-8">
        
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
.button-background {
  background-color: #b4beef;
}

.product {
  background-image: url("../assets/product.png");
  background-size: cover;
}
</style>
