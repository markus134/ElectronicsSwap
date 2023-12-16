<template>
    <div class="flex flex-row">
        <div class="p-4 h-40 w-60">
          <img
            :src="loan_product.post_info.image_url != null ? loan_product.post_info.image_url : productPlaceholder"
            class="aspect-ratio object-cover h-full w-full rounded-lg"
          />
        </div>
        <div class="flex flex-row justify-between w-full mr-20">
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote nimi</p>
                <p class="font-medium text-2xl">{{ loan_product.post_info.title }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote pakkuja</p>
                <p class="font-medium text-2xl">{{ loan_product.seller }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">hind</p>
                <p class="font-medium text-2xl">{{ loan_product.post_info.price }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kogus</p>
                <p class="font-medium text-2xl">{{ loan_product.quantity }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kuni</p>
                <p class="font-medium text-2xl">{{ loan_product.loan_time }}</p>
            </div>
        </div>
    </div>
   
</template>

<script>
import productPlaceholder from '@/assets/placeholder_product.png';

export default {
  props: ['loan_product'],
  data() {
    return {
      productPlaceholder: productPlaceholder,
    };
  },
  
};
</script>
