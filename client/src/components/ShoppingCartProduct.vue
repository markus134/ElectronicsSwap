<template>
    <div class="flex flex-row">
        <div class="p-4 h-40 w-60">
          <img
            :src="shopping_cart_product.image_url != null ? shopping_cart_product.image_url : productPlaceholder"
            class="aspect-ratio object-cover h-full w-full rounded-lg"
          />
        </div>
        <div class="flex flex-row justify-between w-full mr-20">
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote nimi</p>
                <p class="font-medium text-2xl">{{ shopping_cart_product.title }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote pakkuja</p>
                <p class="font-medium text-2xl">{{ shopping_cart_product.seller }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">hind</p>
                <p class="font-medium text-2xl">{{ shopping_cart_product.price }} EUR/kuus</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg mt-2">kogus</p>
                <div class="flex flex-row">
                    <button @click="decrementAmount" class=" px-4 text-white rounded-button-1"
                    style="background: #b4beef">-</button>
                    <p class="font-medium text-2xl py-2 px-4 text-white"
                    style="background: #9aa2ea">{{ shopping_cart_product.quantity }}</p>
                    <button @click="incrementAmount" class=" px-4 text-white rounded-button-2"
                    style="background: #b4beef">+</button>
                </div>
            </div>
            <div class="flex flex-col justify-evenly ml-6 items-end">
              <button @click="deleteProduct" class="delete_button px-4 py-4"></button>
            </div>
        </div>
    </div>
   
</template>

<script>
import productPlaceholder from '@/assets/placeholder_product.png';

export default {
  props: ['shopping_cart_product'],
  data() {
    return {
      productPlaceholder: productPlaceholder,
    };
  },
  methods: {
    incrementAmount() {
      this.$emit('updateAmount', this.shopping_cart_product, 1);
    },
    decrementAmount() {
      if (this.shopping_cart_product.quantity > 1) {
        this.$emit('updateAmount', this.shopping_cart_product, -1);
      }
    },
    deleteProduct() {
      this.$emit('deleteProduct', this.shopping_cart_product);
    },
  },
};
</script>


<style scoped>
  .delete_button {
  background-image: url("../assets/delete.png");
  background-size: cover;
  }
  .rounded-button-1 {
    border-radius: 10px 0 0 10px;
  }
  .rounded-button-2 {
    border-radius: 0 10px 10px 0;
  }
</style>