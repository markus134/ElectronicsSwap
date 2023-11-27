<template>
  <div class="min-h-screen flex flex-col ">
    <Navbar />
    <div class="flex-row pt-[150px] px-[75px]">
      <div class="flex">
        <div class="flex-col mr-4" style="width: 80%">
          <div class="flex-row mb-4">
            <div class="flex justify-between text-xl">
              <div class="flex flex-row">
                <input v-model="searchInput" placeholder="Otsi" @keyup.enter="search" class="p-2 border rounded h-11 ml-10" />
                <button @click="search" class="ml-2 custom-button">Otsi</button>
              </div>
              <div class="flex flex-row">
                <label for="sort" class="ml-4 mt-2 mr-2">Sorteerimine:</label>
                <select @change="search" v-model="sortOption" id="sort" class="p-2 h-11 border rounded text-white" style="background-color: #9aa2ea;">
                  <option value="kallimad">Kallid enne</option>
                  <option value="odavad">Odavad enne</option>
                  <option value="uued">Uued enne</option>
                  <option value="vanad">Vanad enne</option>
                </select>
              </div>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-8 ml-10 mt-4">
            <div v-for="(product, index) in filteredProducts" :key="index" class="">
              <Product :product="product" @add-to-cart="addToCart"/>
            </div>
        </div>
        </div>
        <div class="border p-4 text-xl" style="width: 20%; height: 20%">
          <div class="flex items-center mb-4">Hind</div>
          <div class="flex flex-row justify-between mb-8">
            <input @input="search" placeholder="0€" v-model="bottom" style="width: 30%" class="mx-auto border-black border-2 text-center"/>
            <div class="">-</div>
            <input @input="search" placeholder="10000€" v-model="top" style="width: 30%" class="mx-auto border-black border-2 text-center">
          </div>
        <div class="flex flex-row justify-between">
          <button @click="removeFilters()" class="custom-button" style="background: #EEEFB4; color: black">Eemalda filtrid</button>
        </div>
          <div v-for="category in categories" :key="category.id">
            <button @click="toggleSublist(category.name)" class="custom-button">
              {{ category.name }}
            </button>
            <div class="sublist-container" :style="{ maxHeight: category.sublistHeight }">
              <div class="flex flex-col justify-center items-center">
                <div v-for="subitem in category.sublist" :key="subitem.id" style="width: 80%">
                  <button @click="filterBySubCategory(subitem.name)" class="custom-subbutton">{{ subitem.name }}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Product from "@/components/Product.vue";
import { categories} from '@/components/data.js';
import { usePostsStore } from "../store/modules/posts";

export default {
  components: {
    Navbar,
    Product,
  },
  data() {
    return {
      searchInput: "",
      bottom: null,
      top: null,
      sortOption: "kallimad",
      filteredProducts: [],
      categories: categories,
      products: [],
      selectedCategory: null,
      selectedSubCategory: null,
    };
  },
  async mounted() {
      const postStore = usePostsStore();
      await postStore.getPosts(false)
      this.products = postStore.all_posts 
      this.search()
  },
  
  methods: {
    search() {
      const searchTerm = this.searchInput.toLowerCase();
      const minPrice = parseInt(this.bottom) || 0;
      const maxPrice = parseInt(this.top) || 10000;

      let filteredProducts = this.products.filter((product) => {
        const titleMatches = product.title.toLowerCase().includes(searchTerm);
        const priceInRange =
          parseInt(product.price) >= minPrice && parseInt(product.price) <= maxPrice;
        const subcategoryMatches = !this.selectedSubCategory || product.subcategory === this.selectedSubCategory;
        return titleMatches && priceInRange && subcategoryMatches;
      });
      if (this.sortOption === "kallimad") {
          filteredProducts.sort((a, b) => parseInt(b.price) - parseInt(a.price));
      } else if (this.sortOption === "odavad") {
          filteredProducts.sort((a, b) => parseInt(a.price) - parseInt(b.price));
      } else if (this.sortOption === "uued") {
          filteredProducts.sort((a, b) => b.date - a.date);
      } else if (this.sortOption === "vanad") {
          filteredProducts.sort((a, b) => a.date - b.date);
      }
      this.filteredProducts = filteredProducts;
    },
    calculateSublistHeight(category) {
      const itemHeight = 60;
      const itemCount = category.sublist.length;
      return itemHeight * itemCount;
    },
    toggleSublist(categoryName) {
      this.categories.forEach((category) => {
        if (category.name === categoryName) {
          category.showSublist = !category.showSublist;
          category.sublistHeight = category.showSublist ? `${this.calculateSublistHeight(category)}px` : 0;
        } else {
          category.showSublist = false;
          category.sublistHeight = 0;
        }
      });
    },
    filterBySubCategory(subcategoryName) {
      this.selectedSubCategory = subcategoryName;
      this.search();
    },
    removeFilters() {
      this.sortOption = "kallimad";
      this.bottom = null;
      this.top = null;
      this.selectedCategory = null;
      this.selectedSubCategory = null;
      this.searchInput = "";
      this.search();
      this.toggleSublist();
    },
    async addToCart(product) {
      try {
        const postStore = usePostsStore();
        await postStore.addToCart(product.post_id);
      } catch (error) {
        console.error('Error adding product to the cart:', error);
      }
    },
  },
};
</script>

<style scoped>
.custom-button {
  width: 100%;
  transition: background-color 0.5s ease, border-color 0.5s ease,
    color 0.5s ease, transform 0.5s ease;
  padding: 8px 16px;
  margin-bottom: 16px;
  display: inline-block;
  background-color: #9aa2ea;
  color: #fff;
  cursor: pointer;
  border-radius: 8px;
}
.custom-button:hover {
  background-color: #ceb4ef;
  color: white;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transform: scale(1.25);
}
.custom-subbutton {
  width: 100%;
  transition: background-color 0.5s ease, border-color 0.5s ease,
    color 0.5s ease, transform 0.5s ease;
  padding: 8px 16px;
  margin-bottom: 8px;
  display: inline-block;
  background-color: #b4beef;
  color: #fff;
  cursor: pointer;
  border-radius: 8px;
}
.custom-subbutton:hover {
  background-color: #ceb4ef;
  color: white;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transform: scale(1.25);
}
.sublist-container {
  overflow: hidden;
  max-height: 0;
  transition: max-height 0.3s ease-out;
}
</style>
