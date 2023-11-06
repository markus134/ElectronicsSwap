<template>
  <div>
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
            Failid
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
          <div v-if="selectedButton === 'materjalid'" class="w-full h-40 p-2">
            <div class="w-full h-8 text-gray-400">Siia saad lisada failid</div>
            <div class="file-list">
              <div v-for="(file, index) in fileBoxes[currentBoxIndex]" :key="index" class="file-box">
                <div class="file-box-content">{{ file.name }}</div>
                <button class="delete-button" @click="deleteFile(index)">Delete</button>
              </div>
              <div class="file-box add-file h-28 w-28" @click="openFileInput">
                +
                <input
                  type="file"
                  style="display: none"
                  @change="handleFileChange"
                  ref="fileInput"
                />
              </div>
            </div>
          </div>
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
            <textarea v-model="price" placeholder="hind" class="ml-2 w-24 h-10 p-2"></textarea>
            <span class="ml-2">eur/kuus</span>
          </div>
        </div>
        <div class="flex bg-white rounded shadow-2xl w-1/6 h-4/5 mt-4 p-4 ml-auto mr-32">
          <button class="button-background w-full h-full p-2 ml-2">Loo pakkumine</button>
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
      productTitle: "",
      selectedButton: "kirjeldus",
      kirjeldus: "",
      tehnilineInfo: "",
      price: "",
      fileBoxes: [[]], // Array of arrays for each file box
      showFileModal: false,
      currentBoxIndex: 0, // Index of the currently active box
    };
  },
  methods: {
    openWindow(button) {
      this.selectedButton = button;
    },
    openFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      const files = event.target.files;
      console.log(files)
      this.fileBoxes[this.currentBoxIndex].push(...files);
      console.log(...this.fileBoxes)
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

.button-active {
  background-color: #b4bfff;
}

.file-list {
  display: flex;
  flex-wrap: wrap;
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
  background-color: #ff6666;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 5px;
}

.add-file {
  background-color: #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
