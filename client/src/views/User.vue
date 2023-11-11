<template>
  <div class="min-h-screen flex flex-col">
    <div class="mb-24">
      <Navbar />
    </div>
    <div class="ml-16 mr-16">
    <div class="mt-10">
      <div class="flex flex-row justify-between">
        <div class="flex flex-row">
          <img src="@/assets/user.png" alt="User image" />
          <div class="flex flex-col ml-10">
            <p class="font-medium text-lg mt-2">Usaldusväärsus - {{ user.trustworthiness }}</p>
            <p class="mt-2 font-medium text-6xl">{{ user.username }}</p>
          </div>
        </div>
        <button
          class="self-center button-background text-white py-4 px-4 w-2/12 rounded-md mr-12"
          @click="updateData"
        >
          Uuenda andmeid
        </button>
      </div>
    </div>

    <div class="mt-16">
      <p class="font-medium text-xl">Kontaktandmed</p>
      <p class="mt-4">{{ user.email }}</p>
      <p class="font-medium text-xl mt-8">Minu kirjeldus</p>
      <p class="mt-4">{{ user.description }}</p>
    </div>

    <div class="mt-16">
      <p class="font-medium text-xl">Mida mina pakun</p>
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

    <div>
      <p class="font-medium text-xl">Mida ma teistele hetkel laenan</p>
      <div class="mt-8 w-full bg-gray-200">
        <LoanProduct
          v-for="(loan_product, index) in loan_products"
          :key="index"
          :loan_product="loan_product"
        />
      </div>
    </div>

    <div class="mt-16">
      <p class="font-medium text-xl">Uued tellimused (keegi maksis, nüüd tuleb temaga ühendust võtta)</p>
      <div class="mt-8 w-full bg-gray-200">
        <NewOrderProduct
          v-for="(new_order_product, index) in new_order_products"
          :key="index"
          :new_order_product="new_order_product"
          @acceptTrade="acceptTrade"
        />
      </div>
    </div>

    <div class="mt-16 mb-40">
      <p class="font-medium text-xl">Mille eest ma ise maksan</p>
      <div class="mt-8 w-full bg-gray-200">
        <LendingFromProduct
          v-for="(lending_from_product, index) in lending_from_products"
          :key="index"
          :lending_from_product="lending_from_product"
        />
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Product from "@/components/Product.vue";
import LoanProduct from "@/components/LoanProduct.vue";
import NewOrderProduct from "@/components/NewOrderProduct.vue"
import LendingFromProduct from "@/components/LendingFromProduct.vue";

export default {
  components: {
    Navbar,
    Product,
    LoanProduct,
    NewOrderProduct,
    LendingFromProduct
  },
  data() {
    return {
      user: {
        trustworthiness: "KESKMINE",
        username: "MINGI KASUTAJA",
        email: "kasutaja@gmail.com",
        description: "Olen juba selle platvormi kasutaja 3 aastat, palju häid hinnanguid. Seadmeid ei vaheta"

      },
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
        {
          title: "Teine toode",
          description: "Teise toote kirjeldus",
          price: "19 EUR/kuus",
        },
        {
          title: "Teine toode",
          description: "Teise toote kirjeldus",
          price: "19 EUR/kuus",
        },
      ],
      loan_products: [
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
      ],

      new_order_products: [
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
      ],
      lending_from_products: [
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
        {
          title: "KÄEKELLAD",
          borrower: "KASUTAJA",
          price: "14 EUR/kuus",
          amount: "1",
          loan_time: "11.09.2023"
        },
      ],
    };
  },
  methods: {
   addToCart(product) {
      console.log(product)
   },
   acceptTrade(product) {
      console.log(product)
   }
  },
};
</script>

<style scoped>
.button-background {
  background-color: #b4beef;
}
</style>
