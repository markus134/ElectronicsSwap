<template>
    <div class="flex flex-row">
        <div class="p-4 h-40 w-60">
          <img
            :src="lending_from_product.post_info.image_url != null ? lending_from_product.post_info.image_url : productPlaceholder"
            class="aspect-ratio object-cover h-full w-full rounded-lg"
          />
        </div>
        <div class="flex flex-row justify-between w-full mr-20">
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote nimi</p>
                <p class="font-medium text-2xl">{{ lending_from_product.post_info.title }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">toote pakkuja</p>
                <p class="font-medium text-2xl">{{ lending_from_product.lender_username }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">hind</p>
                <p class="font-medium text-2xl">{{ lending_from_product.post_info.price }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kogus</p>
                <p class="font-medium text-2xl">{{ lending_from_product.quantity }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kuni</p>
                <p class="font-medium text-2xl">{{ lending_from_product.loan_time }}</p>
            </div>
        </div>
    </div>
   
</template>

<script>
import productPlaceholder from '@/assets/placeholder_product.png';

export default {
  props: ['lending_from_product'],
  data() {
    return {
      productPlaceholder: productPlaceholder,
    };
  },
  
};
</script>
