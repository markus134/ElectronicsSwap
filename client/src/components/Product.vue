<template>
  <div class="flex mx-auto">
    <div class="product h-96 w-80 mb-10">
      <router-link :to="{ name: 'item-page', params: { id: product.id } }">
        <div class="h-full flex flex-col justify-end">
          <p class="text-white ml-5 text-xl">{{ product.title }}</p>
          <p class="text-gray-400 ml-5 mt-3">{{ product.description }}</p>
          <div class="flex justify-between ml-5 mb-5 mt-4">
            <button class="bg-white py-3 px-6 rounded-md" @click.prevent="addToCart">Lisa</button>
            <p class="text-white self-center mr-6">{{ product.price }}</p>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  props: ['product'],
  methods: {
    addToCart() {
      this.$emit('add-to-cart', this.product);
    },
  },
};
</script>

<style scoped>
.product {
  position: relative;
  background-image: url("../assets/product.png");
  background-size: cover;
}
</style>
