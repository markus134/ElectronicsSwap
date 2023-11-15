<template>
  <div class="min-h-screen flex flex-col">
    <div class="mb-28">
    <Navbar />
    </div>
    <div class="background">
      <div class="text-5xl mb-2 p-4 ml-28 background ">Loo pakkumine</div>
      <div class="flex flex-col items-center justify-center background">
        <div class="bg-white p-8 rounded shadow-2xl w-5/6 h-4/5">
          <div class="text-2xl">
            <input
              v-model="productTitle"
              placeholder="Kirjuta toote tiitel"
              class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black focus:outline-none focus:border-indigo-300 duration-300"
            />
          </div>
        </div>
        <div class="flex p-4"></div>
        <div class="flex flex-col rounded-lg overflow-hidden w-5/6 shadow-2xl">
          <div class="w-full flex">
            <button
              class="transition-all text-3xl w-full py-4 outline-none capitalize"
              :class="
                tab == activeTab
                  ? 'bg-gray-100'
                  : 'bg-gray-200 hover:bg-gray-300'
              "
              :key="tab"
              v-for="tab in tabs"
              @click="activeTab = tab"
            >
              {{ tab }}
            </button>
          </div>
          <div class="w-full p-8 bg-gray-100" v-if="activeTab == 'kirjeldus'">
            <textarea
            placeholder="Siia saad lisada kirjelduse"
            class="w-full h-40 text-2xl bg-gray-100"
          ></textarea>
          </div>
          <div class="w-full flex flex-col p-8 bg-gray-100" v-if="activeTab == 'failid'">
            <div class="w-full h-8 text-gray-400 text-2xl mb-4">Siia saad lisada pildid</div>
              <div class="w-full flex flex-col xl:grid xl:grid-cols-4 gap-8">
              <div v-for="(file, index) in fileBoxes[currentBoxIndex]"
                   :key="index"
                   class="file-box h-24 flex-col rounded-2xl">
                <div class="file-box-content">
                  {{ file.name }}
                </div>
                <div class="file-box-buttons">
                  <button class="delete-button w-full" @click="deleteFile(index)">Delete</button>
                </div>
              </div>
              <div class="file-box add-file h-24 w-24 text-4xl text-white border-2 border-black rounded-2xl" v-if="fileBoxes[currentBoxIndex].length < 4" @click="openFileInput">
                +
                <input type="file" style="display: none" @change="handleFileChange" ref="fileInput" />
              </div>
          </div>
          </div>
          <div
            class="w-full p-8 bg-gray-100"
            v-if="activeTab == 'tehniline info'"
          >
            <div class="w-full flex flex-col text-2xl text-gray-400 bg-gray-100 xl:grid xl:grid-cols-2 gap-2 h-40">
             <div class="flex flex-row mx-auto h-12 items-center">
              <label class="">Vali kategooria:</label>
                <select class="ml-8 border rounded text-white"
                        style="background-color: #b4beef;"
                        v-model="currentCategory"
                >
                  <option v-for="category in categories"
                          :key="category.id"
                          :value="category.name"
                  >
                    {{ category.name }}
                  </option>
                </select>
             </div>
             <div class="flex flex-row mx-auto h-12 items-center">
                <label class="">Vali alamkategooria:</label>
                <select class="ml-8 border rounded text-white" style="background-color: #b4beef;">
                  <option v-for="subitem in filteredSubitems"
                          :key="subitem.id"
                          :value="subitem.name"
                  >
                    {{ subitem.name }}
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>
      <div class="flex-row flex w-5/6 justify-between mt-8 text-xl mb-4">
        <div class="flex bg-white rounded shadow-2xl p-4">
          <div class="flex justify-center items-center">
            <span class="mr-4">Hind:</span>
            <textarea v-model="price" placeholder="hind" class="w-16 h-8 capitalize text-2xl justify-center"></textarea>
            <span class="ml-2">eur/kuus</span>
          </div>
        </div>
        <div class="flex rounded shadow-2xl">
          <button class="button-background w-full h-full p-4 text-2xl">Loo pakkumine</button>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import {categories, products} from '@/components/data.js';

export default {
  components: {
    Navbar,
  },
  data() {
    return {
      productTitle: "",
      currentCategory: 'Käekellad',
      tabs: ['kirjeldus', 'failid', 'tehniline info'],
      activeTab: 'kirjeldus',
      price: "",
      fileBoxes: [[]],
      showFileModal: false,
      currentBoxIndex: 0,
      maxFileBoxes: 4,
      categories: categories,
    };
  },
  computed: {
    filteredSubitems() {
      const selectedCategoryObj = this.categories.find(cat => cat.name === this.currentCategory);
      return selectedCategoryObj ? selectedCategoryObj.sublist : [];
    },
  },
  methods: {
    products() {
      return products
    },
    openFileInput() {
      if (this.fileBoxes.length < this.maxFileBoxes) {
        this.$refs.fileInput.click();
      }
    },
    handleFileChange(event) {
      const files = event.target.files;
      this.fileBoxes[this.currentBoxIndex].push(...files);
    },
    deleteFile(index) {
      this.fileBoxes[this.currentBoxIndex].splice(index, 1);
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
.file-box {
  border: 1px solid #ccc;
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 10px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
}

.file-box-content {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.delete-button {
  background-color: #b4beef;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 5px;
}

.add-file {
  background-color: #b4beef;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
