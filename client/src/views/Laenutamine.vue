<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />
    <div class="flex-row p-4 mt-10">
      <div class="flex">
        <div class="flex-col mr-4" style="width: 80%;">
          <div class="flex-row mb-4">
            <div class="flex justify-between">
              <div class="w-full">
                <input v-model="searchInput" placeholder="Kirjuta siia midagi" class="p-2 border rounded ml-10" />
                <button @click="search" class="ml-2 p-2 bg-blue-500 text-white rounded">Otsi</button>
              </div>
              <div class="flex flex-row">
                <label for="sort" class="ml-4 mt-2 mr-2">Sorteerimine:</label>
                <select v-model="sortOption" id="sort" class="p-2 border rounded">
                  <option value="kallimad">Kallimad enne</option>
                  <option value="odavad">Odavad enne</option>
                  <option value="uued">Uued enne</option>
                  <option value="vanad">Vanad enne</option>
                </select>
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-4 ml-10 mt-10">
            <div v-for="item in filteredItems" :key="item.id" class="border p-2 rounded">
              {{ item.name }} - {{ item.price }} eur
            </div>
          </div>
        </div>
        <div class="border p-4" style="width: 20%; height: 20%;">
          <div class="flex items-center mb-4">Hind</div>
          <div class="flex flex-row justify-between mb-4">
            <input placeholder="0€" style="width: 30%" class="mx-auto border-black border-2 text-center"/>
            <div class="">-</div>
            <input placeholder="10000€" style="width: 30%" class="mx-auto  border-black border-2 text-center">
          </div>
          <button @click="toggleSublist('Käekellad')" class="mb-4 flex w-full justify-center border-black items-center border-2 h-12">
            Käekellad
          </button>
          <div v-if="categories.find(cat => cat.name === 'Käekellad').showSublist">
            <div v-for="subitem in categories.find(cat => cat.name === 'Käekellad').sublist" :key="subitem.id" style="width: 80%" class="mb-4 flex justify-center border-black items-center border-2 h-8 mx-auto">
              {{ subitem.name }}
            </div>
          </div>
          <button @click="toggleSublist('Printerid')" class="mb-4 flex w-full justify-center border-black items-center border-2 h-12">
            Printerid
          </button>
          <div v-if="categories.find(cat => cat.name === 'Printerid').showSublist">
            <div v-for="subitem in categories.find(cat => cat.name === 'Printerid').sublist" :key="subitem.id" style="width: 80%" class="mb-4 flex justify-center border-black items-center border-2 h-8 mx-auto">
              {{ subitem.name }}
            </div>
          </div>
          <button @click="toggleSublist('Kõrvaklapid')" class="mb-4 flex w-full justify-center border-black items-center border-2 h-12">
            Kõrvaklapid
          </button>
          <div v-if="categories.find(cat => cat.name === 'Kõrvaklapid').showSublist">
            <div v-for="subitem in categories.find(cat => cat.name === 'Kõrvaklapid').sublist" :key="subitem.id" style="width: 80%" class="mb-4 flex justify-center border-black items-center border-2 h-8 mx-auto">
              {{ subitem.name }}
            </div>
          </div>
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
      searchInput: "",
      sortOption: "kallimad",
      categories: [
        { id: 1, name: "Käekellad", description: "Description 1", showSublist: false, sublist: [
            { id: 11, name: "Mehaanilised" },
            { id: 12, name: "Kvartskelld" },
            { id: 13, name: "Hübriidilised" },
          ]
        },
        { id: 2, name: "Printerid", description: "Description 2", showSublist: false, sublist: [
            { id: 21, name: "Laserprinterid" },
            { id: 22, name: "Tindiprinterid" },
            { id: 23, name: "3D-printerid" },
          ]
        },
        { id: 3, name: "Kõrvaklapid", description: "Description 3", showSublist: false, sublist: [
            { id: 31, name: "Kõrvapealsed" },
            { id: 32, name: "Sisemised" },
          ]
        },
      ],
      items: [
        { id: 1, name: "Item 1", price: 20 },
        { id: 2, name: "Item 2", price: 15 },
        { id: 3, name: "Item 3", price: 25 },
        { id: 4, name: "Item 4", price: 25 },
        { id: 5, name: "Item 5", price: 30 },
      ],
    };
  },
  computed: {
    filteredItems() {

      return this.items;
    },
  },
  methods: {
    search() {

    },
    toggleSublist(categoryName) {
      const category = this.categories.find(cat => cat.name === categoryName);
      if (category) {
        category.showSublist = !category.showSublist;
      }
    },
  },
};
</script>

<style scoped>

</style>
