<template>
  <div class="min-h-screen flex flex-col ml-16">
    <Navbar />
    <!-- ... your existing code ... -->

    <div class="mt-16">
      <p class="font-medium text-xl">Mida ma teistele hetkel laenan</p>
      <div class="flex flex-row mt-8">
        <Product
          v-for="(product, index) in products"
          :key="index"
          :product="product"
          @add-to-cart="addToCart"
          :class="index > 0 ? 'ml-4' : ''"
        />
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
import Product from "@/components/Product.vue"; 

export default {
  components: {
    Navbar,
    Product, 
  },
  data() {
    return {
      products: [
        {
          title: "Käekellad",
          description: "Siin on mingi kirjeldus nendele ägedatele käekelladele",
          price: "14 EUR/kuus",
        },
        {
          title: "Teine toode",
          description: "Teise toote kirjeldus",
          price: "19 EUR/kuus",
        },
        // Add more product objects as needed
      ],
    };
  },
  methods: {
    addToCart(product) {
      console.log(product)
    },
  },
};
</script>

<style scoped>
.button-background {
  background-color: #b4beef;
}
</style>
