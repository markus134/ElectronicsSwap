<template>
  <div class="flex items-center justify-center">
    <div :style="productStyle" class="product h-96 w-80 mb-10">
      <router-link :to="{ name: 'item-page', query: { post_id: product.post_id } }">
        <div class="h-full flex flex-col justify-end">
          <p class="text-white text-xl">{{ product.title }}</p>
          <p class="text-gray-400 mt-3">{{ product.short_description }}</p>
          <div class="flex justify-between mb-5 mt-4">
            <button v-if='product.user_id != number' class="bg-white py-3 px-6 rounded-md hover:bg-[#B4BEEF] " @click.prevent="addToCart">Lisa</button>
            <button v-else class="bg-white py-3 px-6 rounded-md hover:bg-[#B4BEEF] ">Vaata</button>
            <p class="text-white self-center ">{{ product.price }} eur/kuus</p>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>



<script>
import { useAuthStore } from '@/store/modules/auth';
import { mapGetters } from 'pinia';
export default {
  props: ['product'],
  computed: {
     ...mapGetters(useAuthStore, ['isLoggedIn']),
    productStyle() {
      // Use linear gradient with an overlay effect
      return {
        backgroundImage: `linear-gradient(to bottom, rgba(0,0,0,0) 20%, rgba(0,0,0,1)), url('${this.product.image_url}')`,
      };

    },
  },
  methods: {
    addToCart() {
      this.$emit('add-to-cart', this.product);
    },
  },
  data: () => ({
    authStore: useAuthStore(),
    number: localStorage.getItem("userId"),
  })
};
</script>

<style scoped>
.product {
  position: relative;
  background-size: cover;
}

/* Optional: add styles for the content inside the product component */
.product .h-full {
  padding: 20px; /* Adjust padding according to your design */
}

.product img {
  border-radius: 8px; /* Optional: add border-radius to the image */
}
</style>
