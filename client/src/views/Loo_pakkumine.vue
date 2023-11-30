<template>
    <Navbar />
    <div class="flex flex-col h-screen items-center background">
      <div class="text-5xl mb-8 w-5/6 mt-32">Loo pakkumine</div>

      <div class="bg-white p-8 rounded shadow-2xl w-5/6">
        <input
          v-model="productTitle"
          placeholder="Kirjuta toote tiitel"
          class="transition ease-in-out delay-150 w-full p-2 border-b-2 border-black text-3xl
          focus:outline-none focus:border-indigo-300 duration-300"
        />
      </div>

      <div class="flex flex-col rounded-lg overflow-hidden w-5/6 h-1/2 mt-8">
        <div class="w-full flex">
          <button
            class="transition-all text-3xl w-full py-4 outline-none capitalize"
            :class="tab === activeTab ? 'bg-gray-100' : 'bg-gray-200 hover:bg-gray-300'"
            :key="tab"
            v-for="tab in tabs"
            @click="activeTab = tab"
          >
            {{ tab }}
          </button>
        </div>

        <div class="w-full h-60 p-6 bg-gray-100" v-if="activeTab === 'kirjeldus'">
          <div
            class="w-full h-10 text-2xl bg-gray-100 text-gray-400"
          >
            Siia saad lisada lühema kirjelduse, mis ilmub toote nime all
          </div>
          <input v-model="shortDescription" class="w-full text-2xl rounded-xl" />
          <div class="w-full h-10 text-2xl bg-gray-100 text-gray-400 mt-2">
            Siia saad lisada pikema kirjelduse
          </div>
          <textarea
            v-model="longDescription"
            class="w-full text-2xl rounded-xl"
            style="resize: none"
          ></textarea>
        </div>

        <div class="w-full h-60 flex flex-col p-6 bg-gray-100" v-if="activeTab === 'failid'">
          <div class="w-full h-full text-gray-400 text-2xl">Siia saad lisada lingi youtube'ist</div>
          <input v-model="youtubeUrl" class="w-full text-2xl rounded-xl mt-2" />
          <div class="w-full text-gray-400 text-2xl mt-2">Siia saad lisada pildid</div>

          <div class="mt-2 w-full flex flex-col xl:grid xl:grid-cols-4 gap-8">
            <div
              v-for="(file, index) in fileBoxes[currentBoxIndex]"
              :key="index"
              class="file-box h-20 flex-col rounded-2xl"
            >
              <div class="file-box-content">{{ file.name }}</div>
              <button class="delete-button w-full" @click="deleteFile(index)">Kustuta</button>
            </div>

            <div v-if="fileBoxes[currentBoxIndex].length < 4" class="file-box add-file h-20 w-20 text-4xl text-white rounded-2xl" @click="openFileInput">
              +
              <input type="file" style="display: none" @change="handleFileChange" ref="fileInput" />
            </div>
          </div>
        </div>

        <div class="w-full overflow-y-auto p-6 bg-gray-100" v-if="activeTab === 'kategooria'">
          <div class="w-full flex flex-col text-2xl text-gray-400 xl:grid xl:grid-cols-2 gap-2">
            <div class="flex flex-row mx-auto h-full items-center">
              <label>Vali kategooria:</label>
              <select class="ml-8 border rounded text-white" style="background-color: #b4beef;" v-model="currentCategory">
                <option v-for="category in categories" :key="category.id" :value="category.name">{{ category.name }}</option>
              </select>
            </div>

            <div class="flex flex-row mx-auto h-full items-center">
              <label>Vali alamkategooria:</label>
              <select v-model="currentSubCategory" class="ml-8 border rounded text-white" style="background-color: #b4beef;">
                <option v-for="subitem in filteredSubitems" :key="subitem.id" :value="subitem.name">{{ subitem.name }}</option>
              </select>
            </div>
          </div>
        </div>

        <div class="w-full h-60 p-6 bg-gray-100" v-if="activeTab === 'tehniline info'">
          <div class="flex-col text-2xl">
            <div class="flex flex-row justify-around">
              <p class="text-2xl text-gray-400">
                Siia saad lisada tehnilise info kujul key - value. Näiteks operatsioonisüsteem: IOS.
              </p>
              <button @click="addPair(index)" class="ml-10 button-background">Lisa plokk</button>
            </div>
            <div class="h-40 overflow-y-auto">
                <div v-for="(pair, index) in keyValuePairs" :key="index" class="grid grid-cols-2 mt-6">
                  <div class="flex flex-row justify-evenly">
                    <input v-model="pair.key" placeholder="Key" class="ml-8 border rounded" />
                    : <input v-model="pair.value" placeholder="Value" class="ml-8 border rounded" />
                  </div>

                  <div class="flex justify-evenly">
                    <button @click="removePair(index)" class="button-background"
                      style="background: #ceb4ef"
                    >Eemalda plokk</button>
                  </div>
                </div>
              </div>
          </div>
        </div>
      </div>

      <div class="flex-row flex w-5/6 justify-between text-xl mb-6">
        <div class="flex bg-white rounded shadow-2xl p-4">
          <div class="flex justify-center items-center">
            <span class="mr-4">Hind:</span>
            <input v-model="price" placeholder="hind" class="w-16 h-full capitalize text-2xl justify-center" />
            <span class="ml-2">eur/kuus</span>
          </div>
        </div>

        <div class="flex rounded shadow-2xl">
          <button @click="createOffer" class="button-background w-full h-full p-4 text-2xl">Loo pakkumine</button>
        </div>
      </div>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import { categories, products } from "@/components/data.js";
import { usePostsStore } from  "../store/modules/posts"
import router from '@/router';

export default {
  components: {
    Navbar,
  },
  data() {
    return {
      productTitle: "",
      currentCategory: "Käekellad",
      currentSubCategory: "",
      tabs: ["kirjeldus", "failid", "kategooria", "tehniline info"],
      activeTab: "kirjeldus",
      price: "",
      fileBoxes: [[]],
      keyValuePairs: [],
      showFileModal: false,
      currentBoxIndex: 0,
      maxFileBoxes: 4,
      categories: categories,
      shortDescription: "",
      longDescription: "",
      youtubeUrl: "",
    };
  },
  computed: {
    filteredSubitems() {
      const selectedCategoryObj = this.categories.find((cat) => cat.name === this.currentCategory);
      return selectedCategoryObj ? selectedCategoryObj.sublist : [];
    },
  },
  methods: {
    products() {
      return products;
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
    addPair(index) {
      this.keyValuePairs.splice(index + 1, 0, { key: "", value: "" });
    },
    removePair(index) {
      if (this.keyValuePairs.length > 0) this.keyValuePairs.splice(index, 1);
    },
    removePairContent(index) {
      this.keyValuePairs.splice(index, 1, { key: "", value: "" });
    },

    async createOffer() {
      const postStore = usePostsStore();

      // Prepare data to send to the createPost action
      const postData = new FormData();
      postData.append('productTitle', this.productTitle);
      postData.append('price', this.price);
      postData.append('short_description', this.shortDescription);
      postData.append('long_description', this.longDescription);
      postData.append('youtube_url', this.youtubeUrl);
      postData.append('category', this.currentCategory);
      postData.append('sub_category', this.currentSubCategory);
      postData.append('key_value_pairs', JSON.stringify(this.keyValuePairs));
      
      // Append image files to FormData
      this.fileBoxes[this.currentBoxIndex].forEach((file, index) => {
        postData.append(`file${index}`, file);
      });

      try {
        const res = await postStore.createPost(postData);
        if (res === "Success") {
          console.log("Post created successfully");
          router.push("/laenutamine");
        } else {
          console.log("Post creation failed:", res);
        }
      } catch (error) {
        console.error('Error creating post:', error);
      }
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
  padding-right: 4px;
  padding-left: 4px;
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
