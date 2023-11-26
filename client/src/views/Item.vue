<template>
  <div >
    <Navbar :disabled="modalActive"/>
    <div
      class="relative w-full pt-[150px] pb-[30px] px-[30px] sm:px-[75px] flex flex-col lg:flex-row gap-8 lg:gap-8"
    >
      <div
        class="w-full lg:w-1/4 flex flex-col gap-y-8 border-b pb-6 lg:pb-0 lg:border-none"
      >
        <div class="flex flex-col gap-y-4">
          <img
            class="w-full aspect-[4/3] bg-gray-300 object-cover rounded-t-lg border-none cursor-zoom-in"
            :src="selectedImage"
            @click="isImageScaled = true"
          />
          <div class="w-full grid gap-4" :class="`grid-cols-${imagesCols}`">
            <img
              class="transition-all w-full aspect-square object-cover bg-gray-300"
              :class="
                selectedImage == image
                  ? 'border'
                  : 'cursor-pointer hover:scale-105'
              "
              :src="image"
              :key="i"
              v-for="(image, i) in images"
              ref="images"
              @click="selectedImage = image"
            />
          </div>
        </div>
        <h3 class="text-4xl text-black">{{ post.price }} EUR/kuus</h3>
        <div class="w-full flex flex-col 2xl:flex-row gap-8" v-if="isLoggedIn">
          <div class="flex w-full">
            <button
              class="transition-all text-xl w-12 h-12 2xl:h-full 2xl:aspect-square bg-gray-200 hover:bg-red-500 flex items-center justify-center rounded-l-lg"
              @click="counter -= 1"
            >
              -
            </button>
            <div
              class="transition-all text-xl w-12 h-12 2xl:h-full 2xl:aspect-square bg-gray-200 flex items-center justify-center"
            >
              {{ counter }}
            </div>
            <button
              class="transition-all text-xl text-black hover:text-white w-12 h-12 2xl:h-full 2xl:aspect-square bg-gray-200 hover:bg-[#B4BEEF] flex items-center justify-center rounded-r-lg"
              @click="counter += 1"
            >
              +
            </button>
          </div>
          <button
            class="transition-all text-black hover:text-white px-12 py-4 bg-gray-200 hover:bg-[#B4BEEF] rounded-lg"
          >
            Lisa
          </button>
        </div>
      </div>
      <div class="w-full lg:w-3/4 flex flex-col gap-y-8">
        <div class="w-full flex items-center justify-between">
          <router-link class="flex gap-x-2 items-center" :to="{ path: '/user', query: { user_id: post.author.user_id } }">
            <img 
              :src="post.author.profile_picture_url"
              class="w-9 h-9 sm:w-12 sm:h-12 rounded-full"
              alt="profile picture"
            />
            <h2 class="text-xl sm:text-2xl text-black">{{ post.author.username }}</h2>
          </router-link>
          <button
            @click="reportPressed"
            class="hidden md:block transition-all text-xl bg-red-500 hover:bg-red-600 px-8 py-2.5 rounded-lg"
            v-if="isLoggedIn"
          >
            Kaeba
          </button>
          <Kaebus :modalActive="modalActive" @close-modal="reportPressed" />
        </div>
        <div class="flex flex-col gap-y-4">
          <h1 class="text-4xl sm:text-6xl text-black">{{ post.title }}</h1>
          <p class="text-2xl sm:text-3xl text-black/60">
            {{ post.short_description }}
          </p>
        </div>
        <div class="flex flex-col rounded-lg overflow-hidden">
          <div class="w-full flex">
            <button
              class="transition-all text-sm sm:text-base w-full py-4 outline-none capitalize"
              :class="
                tab == activeTab
                  ? 'bg-gray-100'
                  : 'bg-gray-200 hover:bg-gray-300'
              "
              :key="tab"
              v-for="tab in tabs"
              @click="activeTab = tab"
            >
              {{ tab }}
            </button>
          </div>
          <div class="w-full p-8 bg-gray-100" v-if="activeTab == 'kirjeldus'">
            <p class="text-xl">{{ post.long_description }}</p>
          </div>
          <div class="w-full p-8 bg-gray-100" v-if="activeTab == 'materjalid'">
            <div
              class="w-full grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4"
            >
              <iframe
                :src="post.youtube_url"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen
                class="w-full aspect-video bg-gray-300 rounded-lg"
               
              >
              </iframe>
            </div>
          </div>
          <div
            class="w-full p-8 bg-gray-100"
            v-if="activeTab == 'tehniline info'"
          >
            <div class="w-full flex flex-col xl:grid xl:grid-cols-2 gap-8">
              <section class="flex flex-col gap-y-4" :key="i" v-for="(pair, i) in getKeyValuePairs()">
                <h5 class="text-2xl sm:text-3xl">{{ pair.key }}</h5>
                <div
                  class="flex flex-col sm:flex-row sm:items-center gap-x-4 gap-y-2"
                >
                  <h6 class="text-lg sm:text-xl">{{ pair.key }}</h6>
                  <div
                    class="hidden sm:block h-px w-full border border-dashed border-black/5"
                  ></div>
                  <p class="text-lg sm:text-xl">{{ pair.value }}</p>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="absolute top-0 left-0 w-full h-screen flex items-center justify-center z-[1000]"
      v-if="isImageScaled"
    >
      <img
        class="w-11/12 md:w-1/2 aspect-video object-contain z-[1001]"
        :src="selectedImage"
        alt=""
      />
      <div
        class="absolute top-0 left-0 w-full h-full bg-gray-950/75 cursor-zoom-out"
        @click="isImageScaled = false"
      ></div>
    </div>
  </div>
</template>

<script>
// images
import Iphone151 from '@/assets/iphone15.jpg';
import Iphone152 from '@/assets/iphone15_2.jpg';
import Iphone153 from '@/assets/iphone15_3.jpg';
import Iphone154 from '@/assets/iphone15_4.jpg';
import Iphone155 from '@/assets/iphone15_5.jpg';
// components
import Navbar from '@/components/Navbar.vue';
// store
import { useAuthStore } from '@/store/modules/auth';
import { usePostsStore } from '../store/modules/posts';
// modules
import { mapGetters } from 'pinia';
// kaebus
import Kaebus from '@/components/Kaebus.vue'

export default {
  name: 'item-page',

  components: {
    Kaebus,
    Navbar,
  },

  data: () => ({
    imagesCols: 0,
    tabs: ['kirjeldus', 'materjalid', 'tehniline info'],
    activeTab: 'kirjeldus',
    counter: 1,
    images: [Iphone151, Iphone152, Iphone153, Iphone154, Iphone155],
    selectedImage: Iphone151,
    isImageScaled: false,
    post: {author: {}},
    modalActive: false,
    authStore: useAuthStore(),
  }),
  computed: {
    ...mapGetters(useAuthStore, ['isLoggedIn']),
  },

  watch: {
    counter() {
      if (this.counter < 1) {
        this.counter = 1;
      }
    },

    isImageScaled(value) {
      if (value) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = 'auto';
      }
    },
  },
  methods: {
    getKeyValuePairs() {
      try {
          const keyValuePairArray = JSON.parse(this.post.key_value_pairs || '[]');
          return keyValuePairArray;
      } catch (error) {
          console.error('Error parsing key-value pairs:', error);
          return [];
      }
    },
    reportPressed() {
      this.authStore.modalActive = !this.modalActive;
      return this.modalActive = !this.modalActive;
    }
  },
  async mounted() {
    // Assuming the post ID is available as a query parameter in the URL
    const postId = this.$route.query.post_id;
    const postsStore = usePostsStore();

    if (postId && /^\d+$/.test(postId)) {
      // Call the getPost action with the retrieved post ID
      await postsStore.getPost(postId);
      this.post = postsStore.post;
      
      if (this.post.image_urls && this.post.image_urls.length > 0) {
        this.images = this.post.image_urls.length > 1 ? this.post.image_urls : [];
        this.selectedImage = this.post.image_urls[0];
      } else {
        console.error('Post has no images.');
      }
    } else {
      console.error('Invalid post ID');
    }

    const images = this.images.length;
    this.imagesCols = images > 5 ? 5 : images;
  },

};
</script>
