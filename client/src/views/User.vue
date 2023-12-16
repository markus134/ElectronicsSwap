<template>
  <div class="min-h-screen flex flex-col background">
    <div class="mb-24">
      <Navbar :disabled="modalActive" style="transition: opacity0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02)"/>
    </div>
    <div class="ml-16 mr-16">
      <div class="mt-10">
        <div class="flex flex-row justify-between">
          <div class="flex flex-row items-center">
            <input
              v-if="editMode"
              type="file"
              accept="image/*"
              @change="handleImageChange"
              class="hidden"
              ref="imageInput"
            />
            <img
              :src="editMode ? user.profileImage || profileImagePlaceholderEditMode : user.profileImage || profileImagePlaceholder"
              alt="User image"
              class="rounded-full h-32 w-32"
              :class="{ 'cursor-pointer': editMode }" 
              @click="editMode ? handleImageClick() : null"
            />
            <div class="flex flex-col ml-4">
              <p class="font-medium text-lg mt-2">
                Usaldusväärsus - {{ user.trustworthiness }}
              </p>
              <button class="w-1/2 border-2 border-gray rounded-xl" @click="goToUsaldus">Mis see on?</button>
              <p class="mt-2 font-medium text-6xl">{{ user.username }}</p>
            </div>
          </div>
          <div v-if="isOwnProfile">
            <button
              v-if="!editMode"
              class="self-center button-background text-white py-4 px-4 w-2/12 w-full rounded-md"
              @click="toggleEditMode"
            >
              Uuenda andmeid
            </button>
            <button
              v-else
              class="self-center button-background text-white py-4 px-4 w-2/12 w-full rounded-md"
              @click="updateUserData"
            >
              Salvesta muudatused
            </button>
          </div>
          <div v-if="!isOwnProfile">
            <button

              class="hidden md:block transition-all text-xl bg-red-500 hover:bg-red-600 px-8 py-2.5 rounded-lg"
              @click="reportPressed(); isImageScaled(modalActive)"
            >
              Kaeba
            </button>
            <Kaebus :modalActive="modalActive" @close-modal="reportPressed(); isImageScaled(modalActive)"
            />
          </div>
        </div>
      </div>

      <div v-if="!editMode" class="mt-16">
        <p class="font-medium text-xl mt-8">Minu kirjeldus</p>
        <p class="mt-4">{{ user.description }}</p>
      </div>

      <div v-if="editMode" class="mt-16">
        <form class="mt-4">
          <div class="mb-4">
            <label class="font-medium text-xl">
              Email:
            </label>
            <input
              v-model="user.email"
              type="email"
              class="w-full border rounded-md py-2 px-3 focus:outline-none focus:shadow-outline mt-4"
            />
          </div>
          <div class="mb-4">
            <label class="font-medium text-xl">
              Kirjeldus:
            </label>
            <textarea
              v-model="user.description"
              class="w-full border rounded-md py-2 px-3 focus:outline-none focus:shadow-outline mt-4"
            ></textarea>
          </div>
        </form>
      </div>

      <div class="mt-16">
        <p class="font-medium text-xl">Mida mina pakun</p>
        <div class="grid grid-cols-4 mt-14">
            <div v-for="(product, index) in products" :key="index" class="">
              <UsersOwnProduct :product="product" @deleteProduct="deleteProduct" @addToCart="addToCart"/>
            </div>
          </div>
      </div>

      <div v-if="isOwnProfile">
        <p class="font-medium text-xl">Mida ma teistele hetkel laenan</p>
        <div class="mt-8 w-full bg-gray-200">
          <LoanProduct
            v-for="(loan_product, index) in loan_products"
            :key="index"
            :loan_product="loan_product"
          />
        </div>
      </div>

      <div class="mt-16" v-if="isOwnProfile">
        <p class="font-medium text-xl">
          Uued tellimused (keegi maksis, nüüd tuleb temaga ühendust võtta)
        </p>
        <div class="mt-8 w-full bg-gray-200">
          <NewOrderProduct
            v-for="(new_order_product, index) in new_order_products"
            :key="index"
            :new_order_product="new_order_product"
            @acceptTrade="acceptTrade();"
          />
        </div>
      </div>


      <div class="mt-16 mb-40" v-if="isOwnProfile">
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
    <ProfileModal v-if="isOwnProfile" :modalActive="modalActive" @close-modal="reportPressed(); isImageScaled()"></ProfileModal>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import UsersOwnProduct from '@/components/UsersOwnProduct.vue';
import LoanProduct from '@/components/LoanProduct.vue';
import NewOrderProduct from '@/components/NewOrderProduct.vue';
import LendingFromProduct from '@/components/LendingFromProduct.vue';
import profileImagePlaceholder from '@/assets/user.png';
import profileImagePlaceholderEditMode from '@/assets/user_placeholder_edit.png'
import { useProfileStore } from '@/store/modules/profile';
import { useAuthStore } from '@/store/modules/auth';
import { usePostsStore } from '../store/modules/posts';
import router from "../router/index.js";
import Kaebus from '@/components/Kaebus.vue'
import ProfileModal from "../components/ProfileModal.vue";


export default {
  components: {
    Navbar,
    UsersOwnProduct,
    LoanProduct,
    NewOrderProduct,
    LendingFromProduct,
    Kaebus,
    ProfileModal
  },
  data() {
    return {
      modalActive: false,
      authStore: useAuthStore(),
      user: {
        trustworthiness: 'KESKMINE',
        username: 'MINGI KASUTAJA',
        email: 'kasutaja@gmail.com',
        description:
          'Olen juba selle platvormi kasutaja 3 aastat, palju häid hinnanguid. Seadmeid ei vaheta',
        profileImage: null,
      },
      profileImagePlaceholder: profileImagePlaceholder,
      profileImagePlaceholderEditMode: profileImagePlaceholderEditMode,
      editMode: false,
      products: [
        {
          title: 'Käekellad',
          description: 'Siin on mingi kirjeldus nendele ägedatele käekelladele',
          price: '14 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
        {
          title: 'Teine toode',
          description: 'Teise toote kirjeldus',
          price: '19 EUR/kuus',
        },
      ],
      loan_products: [
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
      ],

      new_order_products: [
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
      ],
      lending_from_products: [
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
        {
          title: 'KÄEKELLAD',
          borrower: 'KASUTAJA',
          price: '14 EUR/kuus',
          amount: '1',
          loan_time: '11.09.2023',
        },
      ],
    };
  },
  computed: {
    isOwnProfile() {
      const user_id = this.$route.query.user_id;
      const my_id = localStorage.getItem('userId')
  
      return user_id === my_id;
    },
  },
  methods: {
    isImageScaled() {
      if (this.modalActive) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = 'auto';
      }
    },
    toggleEditMode() {
      this.editMode = !this.editMode;
    },
    goToUsaldus() {
      router.push("/usaldus");
    },
    reportPressed() {
      this.authStore.modalActive = !this.modalActive;
      this.modalActive = !this.modalActive
      return this.modalActive
    },
    async updateUserData() {
      this.editMode = false;

      try {
        const profileStore = useProfileStore();
        const authStore = useAuthStore();
        const formData = new FormData();
        formData.append('email', this.user.email);
        formData.append('description', this.user.description);
        formData.append('file', this.$refs.imageInput.files[0]); 

        const response = await profileStore.updateProfile(formData);

        const current_id = localStorage.getItem("userId");

        if (current_id == profileStore.id) { // If we are viewing our own profile and updating the data, then change the navbar image as well
          authStore.authUser.image_url = response;
          localStorage.setItem("image_url", response);
        }
        
        this.editMode = false;
      } catch (error) {
        console.error('Error updating user data:', error);
      }
    },
  
    handleImageClick() {
      this.$refs.imageInput.click();
    },
    handleImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          this.user.profileImage = reader.result;
        };
        reader.readAsDataURL(file);
      }
    },

    acceptTrade(product) {
      this.reportPressed()
      this.isImageScaled()
    },
    deleteProduct(product) {
      const postsStore = usePostsStore();
      postsStore.deleteUserPost(product.post_id);
      const index = this.products.findIndex(p => p === product);
      if (index !== -1) {
        this.products.splice(index, 1);
      }
    },
    addToCart(product) {
      try {
        const postStore = usePostsStore();
        postStore.addToCart(product.post_id, 1);
      } catch (error) {
        console.error('Error adding product to the cart:', error);
      }
    },
    async initializeUserData(user_id) {
      console.log(user_id)
      const profileStore = useProfileStore();
      if (user_id) {
        await profileStore.getUserInfo(user_id);
        
        this.user.username = profileStore.username;
        this.user.email = profileStore.email;
        this.user.description = profileStore.description;
        this.user.profileImage = profileStore.image_url;
      }
      const postsStore = usePostsStore();
      await postsStore.getUserPosts(user_id);
      this.products = postsStore.all_posts

    },
  },
  created () {
    this.initializeUserData(this.$route.query.user_id);
  },
  beforeRouteUpdate(to, from, next) {
    this.initializeUserData(to.query.user_id)
    next()
  }
};
</script>

<style scoped>
.button-background {
  background-color: #b4beef;
}
.background {
  background-image: url("../assets/background.png");
}

</style>
