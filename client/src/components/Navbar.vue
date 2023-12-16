<template>
  <nav
    class="transition-all w-full fixed top-0 px-[30px] sm:px-[75px] py-[30px] flex flex-col lg:flex-row items-center justify-between z-[999]"
    :class="[inbetweenValue ? 'brightness-[0.7] shadow-none transition duration-300': '' ,scrollY > 0 || windowX < 1024 ? `bg-white shadow-sm` : '']"
  >
    <div class="w-full flex justify-between items-center lg:w-auto">
      <router-link to="/" :class="['flex', 'gap-x-[15px]', 'items-center', { 'pointer-events-none': modalActive }]">
        <img src="@/assets/logowithouttext.png" alt=""
        :style="{ opacity: disabled ? 0.3 : 1, disabled: disabled}"/>
        <h3
          class="transition-all text-3xl text-medium hidden xl:block"
          :class="
            scrollY > 0 || windowX < 1024 ? 'text-black' : `text-${textColor}`
          "
        >
          ElectronicsSwap
        </h3>
      </router-link>
      <button class="flex lg:hidden" @click="isMenuOpened = !isMenuOpened">
        <img src="@/assets/menu.svg" alt="" />
      </button>
    </div>
    <ul
      class="flex flex-col w-full items-center lg:w-auto lg:flex-row gap-[30px]"
      :class="{ 'p-12': windowX < 1024 }"
      v-if="isMenuOpened"
    >
      <li v-if="isAdmin && isLoggedIn">
        <router-link
          to="/admin"
          :class="['text-black', 'hover:text-gray-800', 'text-xl', { 'pointer-events-none': modalActive }]"
          >admin</router-link
        >
      </li>
      <li>
        <router-link
          to="/laenutamine"
          :class="['text-black', 'hover:text-gray-800', 'text-xl', { 'pointer-events-none': modalActive }]"
          
          >laenutamine</router-link
        >
      </li>
      <li>
        <router-link
          to="/vahetus"
          :class="['text-black', 'hover:text-gray-800', 'text-xl', { 'pointer-events-none': modalActive }]"
          >vahetus</router-link
        >
      </li>
      <li v-if="isLoggedIn">
        <router-link
          to="/loo_pakkumine"
          :class="['text-black', 'hover:text-gray-800', 'text-xl', { 'pointer-events-none': modalActive }]"
        >
          loo pakkumine
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link
          to="/ostukorv"
          :class="['text-black', 'hover:text-gray-800', 'text-xl', { 'pointer-events-none': modalActive }]"
          >ostukorv</router-link
        >
      </li>
      <li class="relative" v-if="isLoggedIn">
        <router-link
          :to="{path: '/user', query: { user_id: getUserId() }}"
          :class="['lg:dropdown-btn', 'text-black', 'hover:text-gray-800', 'text-xl', 'flex', 'items-center', 'gap-x-3', { 'pointer-events-none': modalActive }]"
        >
          <img
            :src="image_url !== '' ? image_url : profileImagePlaceholder"
            class="w-9 h-9 rounded-full bg-gray-100 object-cover"
            alt=""
            :style="{ opacity: disabled ? 0.3 : 1}"
          />
          <span>{{ username }}</span>
          <img
            src="@/assets/arrowright.svg"
            class="hidden lg:block rotate-90 mt-px"
            alt=""
          />
          <ul
            class="dropdown-menu absolute bottom-0 right-1/2 translate-y-full translate-x-1/2 pt-4"
          >
            <li
              class="transition-all py-3 px-6 bg-gray-100 hover:bg-gray-200 rounded-t-lg"
            >
              <router-link class="w-full h-full text-lg" :to="{path: '/user', query: { user_id: getUserId() }}"
                >Profiil</router-link
              >
            </li>
            <li class="transition-all bg-gray-100 hover:bg-red-600 rounded-b-lg shadow-sm flex items-center justify-center">
              <button class="text-lg py-3 px-6" @click.prevent="logout">Väljalogimine</button>
            </li>
          </ul>
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <button
        @click="logout" class="transition-all block lg:hidden w-full h-full text-lg px-6 py-3 text-xl bg-red-500 hover:bg-red-600 rounded-lg"
        >
          Väljalogimine
        </button>
      </li>
      <li v-if="!isLoggedIn">
        <router-link
          to="/login"
          class="text-white text-base py-[9px] px-[18px] bg-gray-950 hover:bg-gray-800 active:bg-gray-700 rounded-lg"
          >sisselogimine</router-link
        >
      </li>
      <li v-if="!isLoggedIn">
        <router-link
          to="/registration"
          class="text-black text-base py-[9px] px-[18px] border border-gray-950 hover:bg-gray-950/5 active:bg-gray-950/10 rounded-lg"
          >registreerimine</router-link
        >
      </li>
    </ul>
  </nav>
</template>

<script>
import { useAuthStore } from '@/store/modules/auth';
import { mapGetters } from 'pinia'
import profileImagePlaceholder from '@/assets/user.png';
import router from '../router';

export default {
  props: {
    textColor: {
      type: String,
      required: false,
      default: 'black',
    },
    disabled: {
      type: Boolean,
    }
  },

  data: () => ({
    isMenuOpened: true,
    scrollY: 0,
    windowX: 0,
    profileImagePlaceholder: profileImagePlaceholder,
    authStore: useAuthStore(),
    inbetweenValue: false
  }),

  computed: {
    ...mapGetters(useAuthStore, ['isLoggedIn', 'username', 'image_url', 'modalActive', 'isAdmin']),
  },


  watch: {
    windowX() {
      if (this.windowX > 1024) {
        this.isMenuOpened = true;
      } else {
        this.isMenuOpened = false;
      }
    },
    modalActive(newVal) {
      // Clear existing timeout if any
      clearTimeout(this.delayedClassTimeout);

      // Set a new timeout to apply the class after 300 milliseconds
      this.delayedClassTimeout = setTimeout(() => {
        this.inbetweenValue = newVal;
      }, 55);
    },
  },

  mounted() {
    window.scrollTo(0, 0);
    this.handleScroll();
    this.handleSize();

    window.addEventListener('scroll', this.handleScroll);
    window.addEventListener('resize', this.handleSize);
  },

  unmounted() {
    window.removeEventListener('scroll', this.handleScroll);
  },

  methods: {
    getUserId() {
      return localStorage.getItem('userId')
    },
    handleScroll() {
      this.scrollY = window.scrollY;
    },

    handleSize() {
      this.windowX = window.innerWidth;
    },
    async logout() {
        router.push('/');
        this.authStore.logoutUser();
      
    },
  },
};
</script>

<style lang="scss" scoped>
.nav-button {
  background-color: transparent;
  border: none;
  color: #2d3748;
  cursor: pointer;
  margin-right: 10px;
}

.nav-button:hover {
  background-color: #e2e8f0;
}
</style>
