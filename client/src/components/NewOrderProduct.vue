<template>
     <div class="flex flex-row">
        <div class="p-4 h-40 w-60">
          <img
            :src="new_order_product.post_info.image_url != null ? new_order_product.post_info.image_url : productPlaceholder"
            class="aspect-ratio object-cover h-full w-full rounded-lg"
          />
        </div>
        <div class="flex flex-row justify-between w-full mr-20">
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote nimi</p>
                <p class="font-medium text-2xl">{{ new_order_product.post_info.title }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote ostja</p>
                <p class="font-medium text-2xl">{{ new_order_product.borrower_username }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">hind</p>
                <p class="font-medium text-2xl">{{ new_order_product.post_info.price }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kogus</p>
                <p class="font-medium text-2xl">{{ new_order_product.quantity }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kuni</p>
                <p class="font-medium text-2xl">{{ new_order_product.loan_date_str }}</p>
            </div>
            <div class="self-center">
                <button class="self-center button-background text-white py-4 px-4 w-2/12 w-full rounded-md" @click="viewMore">Vaata rohkem</button>
            </div>
        </div>
    </div>
   
</template>

<script>
import productPlaceholder from '@/assets/placeholder_product.png';
import { useProfileStore } from '../store/modules/profile';
export default {
    props: ['new_order_product'],
    methods: {
        viewMore() {
            this.profileStore.selected_product = this.new_order_product;
            this.$emit('acceptTrade', this.new_order_product);
        },
    },
    data() {
        return {
            productPlaceholder: productPlaceholder,
            profileStore: useProfileStore(),
        };
    },
};
</script>

<style>
.button-background {
  background-color: #b4beef;
}
</style>