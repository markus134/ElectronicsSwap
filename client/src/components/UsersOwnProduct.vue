<template>
    <div class="flex mx-auto">
        <router-link :to="{ name: 'item-page', params: { id: product.id } }">
          <div class="product h-96 w-80 mb-10 flex flex-col justify-end self-end">
            <p class="text-white ml-5 text-xl">{{ product.title }}</p>
            <p class="text-gray-400 ml-5 mt-3">{{ product.description }}</p>
            <div class="flex justify-between ml-5 mb-5 mt-4">
              <button class="bg-white py-3 px-6 rounded-md" @click.prevent="deleteProduct">Kustuta</button>
              <p class="text-white self-center mr-6">{{ product.price }}</p>
            </div>
          </div>
        </router-link>
    </div>
  </template>
    

<script>
export default {
    props: ['product'],
    methods: {
        deleteProduct() {
            this.$emit('deleteProduct', this.product);
        },
    },
};
</script>
  
  <style scoped>
  .product {
  background-image: url("../assets/product.png");
  background-size: cover;
  }
  </style>
    