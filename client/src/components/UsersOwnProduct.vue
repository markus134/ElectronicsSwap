<template>
    <div class="flex mx-auto">
      <div :style="productStyle" class="product h-96 w-80 mb-10">
        <router-link :to="{ name: 'item-page', query: { post_id: product.post_id } }">
          <div class="h-full flex flex-col justify-end">
              <p class="text-white ml-5 text-xl">{{ product.title }}</p>
              <p class="text-gray-400 ml-5 mt-3">{{ product.description }}</p>
              <div class="flex justify-between ml-5 mb-5 mt-4">
                <button v-if="isOwnProfile" class="bg-white py-3 px-6 rounded-md hover:bg-[#B4BEEF] " @click.prevent="deleteProduct">Kustuta</button>
                <button v-else class="bg-white py-3 px-6 rounded-md hover:bg-[#B4BEEF] " @click.prevent="addToCart">Lisa</button>

                <p class="text-white self-center mr-6">{{ product.price }} EUR/KUUS</p>
              </div>
          </div>
        </router-link>
      </div>
    </div>
  </template>
    

<script>
export default {
    props: ['product'],
    computed: {
      productStyle() {
        // Use linear gradient with an overlay effect
        return {
          backgroundImage: `linear-gradient(to bottom, rgba(0,0,0,0) 20%, rgba(0,0,0,1)), url('${this.product.image_url}')`,
        };
      },
      isOwnProfile() {
        const user_id = this.$route.query.user_id;
        const my_id = localStorage.getItem('userId')
    
        return user_id === my_id;
      },
    },
    methods: {
        deleteProduct() {
            this.$emit('deleteProduct', this.product);
        },
        addToCart() {
          console.log("here")
          this.$emit('addToCart', this.product);
        }
    },
};
</script>
  
  <style scoped>
  .product {
  background-image: url("../assets/product.png");
  background-size: cover;
  }
  </style>
    