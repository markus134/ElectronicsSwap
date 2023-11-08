<template>
    <div class="flex flex-row">
        <img src="../assets/product2.png">
        <div class="flex flex-row justify-between w-full mr-20">
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">Toote nimi</p>
                <p class="font-medium text-2xl">{{ loan_product.title }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kellele</p>
                <p class="font-medium text-2xl">{{ loan_product.borrower }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">hind</p>
                <p class="font-medium text-2xl">{{ loan_product.price }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kogus</p>
                <p class="font-medium text-2xl">{{ loan_product.amount }}</p>
            </div>
            <div class="flex flex-col justify-evenly ml-6">
                <p class="text-gray-400 text-lg">kuni</p>
                <p class="font-medium text-2xl">{{ loan_product.loan_time }}</p>
            </div>
        </div>
    </div>
   
</template>

<script>
export default {
    props: ['loan_product'],
};
</script>