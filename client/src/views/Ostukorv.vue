<template>
  <div class="min-h-screen flex flex-col">
    <div class="mb-32">
    <Navbar />
    </div>
    <div class="ml-16 mr-16">
      <div>
        <p class="mt-16 font-medium text-5xl">OSTUKORV</p>
        <hr class="w-64 h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
      </div>
      <div class="mt-8 w-full bg-gray-200">
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
          <button @click="clearShoppingCart" class="mr-8 text-lg px-10 py-4 border-black border-2">Tühista ostukorv</button>
          <button @click="proceedWithPayment" class="bg-zinc-600 text-white text-lg px-10 py-4">Esita tellimus</button>
        </div>
      </div>

      </div>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import ShoppingCartProduct from '@/components/ShoppingCartProduct.vue';

export default {
  components: {
    Navbar,
    ShoppingCartProduct,
  },
  data() {
    return {
      shopping_cart_products: [
        {
          title: 'KÄEKELLAD',
          seller: 'KASUTAJA',
          price: 14,
          amount: 1,
        },
        {
          title: 'KÄEKELLAD',
          seller: 'KASUTAJA',
          price: 34,
          amount: 1,
        },
        {
          title: 'KÄEKELLAD',
          seller: 'KASUTAJA',
          price: 14,
          amount: 1,
        },
      ],
      total_price: 0,
    }
  },
  computed: {
    calculateTotalPrice() {
      return this.shopping_cart_products.reduce((total, product) => {
        return total + product.price * product.amount;
      }, 0);
    },
  },
  watch: {
    shopping_cart_products: {
      handler: 'updateTotalPrice',
      deep: true,
    },
  },
  created() {
    this.updateTotalPrice();
  },
  methods: {
    updateAmount(product, amount) {
      const index = this.shopping_cart_products.findIndex(p => p === product);
      if (index !== -1) {
        this.shopping_cart_products[index] = {
          ...product,
          amount: product.amount + amount
        };
      }
    },
    updateTotalPrice() {
      this.total_price = this.calculateTotalPrice;
    },
    clearShoppingCart() {
      this.shopping_cart_products = [];
    },
    proceedWithPayment() {
      this.$router.push('/payment')
    },
    deleteProduct(shopping_cart_product) {
      const index = this.shopping_cart_products.findIndex(p => p === shopping_cart_product);
      if (index !== -1) {
        this.shopping_cart_products.splice(index, 1);
      }
    },
  }
};
</script>


