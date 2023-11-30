<template>
  <div class="min-h-screen flex flex-col background">
    <div class="mb-32">
    <Navbar />
    </div>
    <div class="ml-16 mr-16">
      <div>
        <p class="mt-16 text-5xl">Ostukorv</p>
        <hr class="w-52 h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
      </div>
      <div class="mt-8 w-full bg-gray-200" v-if="shopping_cart_products.length > 0">
        <ShoppingCartProduct
          v-for="(shopping_cart_product, index) in shopping_cart_products"
          :key="index"
          :shopping_cart_product="shopping_cart_product"
          @updateAmount="updateAmount"
          @deleteProduct="deleteProduct"
        />
      </div>
      <div class="mt-6 flex flex-row justify-between items-center">
        <div class="flex flex-row">
          <p class="text-lg self-end">Kogu hind:</p>
          <p class="ml-4 text-3xl font-medium">{{ total_price }} EUR/KUUS</p>
        </div>
        <div class="flex flex-row">
          <button @click="clearShoppingCart" class="mr-8 text-lg
          px-10 py-4 border-#b4beef border-2
          color2 rounded-xl"
          >Tühista ostukorv</button>
          <button @click="proceedWithPayment" class="color text-white text-lg px-10 py-4 rounded-xl">Esita tellimus</button>
        </div>
      </div>

      </div>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import ShoppingCartProduct from '@/components/ShoppingCartProduct.vue';
import { usePostsStore } from "../store/modules/posts";

export default {
  components: {
    Navbar,
    ShoppingCartProduct,
  },
  data() {
    return {
      shopping_cart_products: [],
      total_price: 0,
      postsStore: usePostsStore()
    }
  },
  computed: {
  calculateTotalPrice() {
    if (Array.isArray(this.shopping_cart_products) && this.shopping_cart_products.length > 0) {
      return this.shopping_cart_products.reduce((total, product) => {
        return total + product.price * product.quantity;
      }, 0);
      
    }
    else {
      return 0;
    }
  },
},
  watch: {
    shopping_cart_products: {
      handler: 'updateTotalPrice',
      deep: true,
    },
  },
  async created() {
    await this.postsStore.getCart()
    this.shopping_cart_products = this.postsStore.shopping_cart
    this.updateTotalPrice();
    
  },
  methods: {
    updateAmount(product, quantity) {
      const index = this.shopping_cart_products.findIndex(p => p === product);
      if (index !== -1) {
        this.shopping_cart_products[index] = {
          ...product,
          quantity: product.quantity + quantity
        };
        this.postsStore.updateQuantity(product.post_id, quantity)
      
      }
    },
    updateTotalPrice() {
      this.total_price = this.calculateTotalPrice;
    },
    clearShoppingCart() {
      this.shopping_cart_products = [];
      this.postsStore.deleteAllProducts();

    },
    proceedWithPayment() {
      this.$router.push('/payment')
    },
    deleteProduct(shopping_cart_product) {
      const postsStore = usePostsStore();
      const index = this.shopping_cart_products.findIndex(p => p === shopping_cart_product);
      if (index !== -1) {
        this.shopping_cart_products.splice(index, 1);
        postsStore.deleteProduct(shopping_cart_product.post_id);

      }
    },
  }
};
</script>

<style>
.background {
  background-image: url("../assets/background.png");
}
.color {
  background: #b4beef;
}
.color2 {
  background: white;
  color: #b4beef;
}
</style>

