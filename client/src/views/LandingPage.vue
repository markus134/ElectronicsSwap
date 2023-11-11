<template>
  <div class="landing-page">
    <!-- Navbar -->
    <navbar text-color="white"></navbar>
    <!-- Header -->
    <header class="header-background">
      <div
        class="w-full h-screen flex items-center justify-start px-[30px] py-[75px] sm:px-[75px] sm:py-[150px]"
      >
        <div
          class="relative max-w-[90%] sm:max-w-[50%] h-full flex flex-col justify-center md:justify-between gap-y-[30px] items-start z-[2]"
        >
          <!-- Header text content -->
          <h1
            class="text-[2em] sm:text-[3em] md:text-[4em] text-black sm:text-white leading-tight"
          >
            laenuta endale seade või vaheta teiste kasutajatega seadmed meie
            platvormiga
          </h1>
          <router-link
            to="/registration"
            class="px-6 py-2 sm:px-9 sm:py-3 text-white bg-black sm:text-black sm:bg-white rounded-lg text-[1.5em] sm:text-[3em] lg:text-[4em] sm:whitespace-nowrap"
            >Alusta kasutamist</router-link
          >
        </div>
      </div>
      <img
        src="@/assets/iphone.png"
        class="hidden md:block absolute right-[10%] bottom-0"
        alt=""
      />
    </header>
    <!-- Main -->
    <main>
      <!-- Popular devices block -->
      <div
        class="relative w-full h-screen pl-[30px] py-[75px] sm:pl-[75px] sm:py-[150px] flex flex-col justify-center gap-y-[30px] overflow-hidden"
      >
        <h2 class="text-[1.5em] sm:text-[3em] md:text-[4em] pr-[30px]">
          Kõige populaarsemad seadmed laenutamiseks
        </h2>
        <!-- Devices list -->
        <ul
          class="hide-scrollbar custom-transition relative whitespace-nowrap select-none max-[956px]:overflow-x-scroll"
          :style="`transform: translateX(-${trackMargin}px)`"
          ref="ul"
        >
          <li
            class="relative mx-3 inline-block h-full w-10/12 lg:w-1/4 aspect-square bg-black rounded-lg"
            :key="i"
            v-for="(value, i) in carousel"
          >
            <a
              href=""
              class="relative w-full h-full flex items-center justify-center text-center text-2em xl:text-[3em] text-white bg-gray-950/75 z-[1]"
              draggable="false"
              >{{ value.title }}</a
            >
            <img
              class="custom-transition image rounded-lg"
              :style="`object-position: ${objectPosition}% center`"
              :src="value.image"
              alt=""
              draggable="false"
              ref="image"
            />
          </li>
        </ul>
        <div class="w-full justify-end pr-[30px] sm:pr-[75px] hidden sm:flex">
          <button @click="moveImagesForward()">
            <img class="w-6 h-6" src="@/assets/arrowright.svg" alt="" />
          </button>
        </div>
      </div>
      <!-- About block -->
      <div class="about-background">
        <div
          class="w-full p-[15px] sm:p-[30px] sm:p-[75px] md:py-[150px] flex flex-col md:flex-row items-center gap-[30px]"
        >
          <div class="w-full flex flex-col gap-y-[75px]">
            <h2 class="text-[2em] sm:text-[3em] md:text-[4em] text-white">
              Miks kasutada meie platvormi?
            </h2>
            <p class="text-[32px] text-white/60 hidden md:block">
              Meie platvorm omandab funktsioone, mida ei saa leida teistes
              kohtades
            </p>
          </div>
          <div
            class="w-full flex flex-col sm:grid sm:grid-cols-2 sm:grid-rows-2 md:grid md:grid-cols-1 xl:grid-rows-2 xl:grid-cols-2 gap-[30px]"
          >
            <div
              class="w-full h-full flex flex-col justify-between p-6 gap-y-[15px] sm:gap-y-[30px] bg-white rounded-lg"
              :key="i"
              v-for="(data, i) in about"
            >
              <div>
                <img class="w-8 h-8 lg:w-16 lg:h-16" :src="data.image" alt="" />
              </div>
              <div>
                <h5 class="sm:text-[32px]">{{ data.title }}</h5>
                <p class="sm:text-[20px]">{{ data.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Feedback block -->
      <div
        class="w-full h-[50vh] px-[75px] py-8 flex flex-col justify-center gap-y-[64px]"
      >
        <div class="w-full flex justify-center">
          <h2 class="text-[1.5em] sm:text-[3em] md:text-[4em] text-center">
            Platvormi tagasiside
          </h2>
        </div>
        <div class="w-full flex items-center justify-center">
          <router-link
            to="/tagasiside"
            class="transition-all text-center bg-gray-100 px-6 sm:px-12 py-3 sm:py-6 rounded-lg text-xl sm:text-3xl hover:bg-[#B4BEEF] hover:text-white"
            >Ole esimene! Jäta tagasiside!</router-link
          >
        </div>
      </div>
      <!-- Action block -->
      <div class="w-full h-[50vh] flex">
        <div class="w-full h-full bg-[#B4BEEF] bg-image">
          <a
            href="#"
            class="w-full h-full flex items-center justify-center text-[1em] sm:text-[3em] md:text-[4em] text-white"
            >laenuta</a
          >
        </div>
        <div class="w-full h-full bg-[#CEB4EF] bg-image">
          <a
            href="#"
            class="w-full h-full flex items-center justify-center text-center text-[1em] sm:text-[3em] md:text-[4em] text-white"
            >loo pakkumine</a
          >
        </div>
      </div>
    </main>
    <!-- Footer -->
    <footer>
      <div class="w-full h-[50vh] flex gap-x-[30] bg-gray-900">
        <div class="w-full flex items-center justify-center">
          <img src="@/assets/logo.png" alt="" />
        </div>
        <div class="w-full flex items-center justify-center gap-x-[30]">
          <ul class="flex flex-col gap-y-[30px]">
            <li>
              <a href="" class="text-xl sm:text-[32px] text-white">Meist</a>
            </li>
            <li>
              <a href="" class="text-xl sm:text-[32px] text-white"
                >Küsida Abi</a
              >
            </li>
            <li>
              <a href="" class="text-xl sm:text-[32px] text-white"
                >Tagasiside</a
              >
            </li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
// components
import Navbar from '@/components/Navbar.vue';
// import icons
import FlameSvg from '@/assets/flame.svg';
import CheckSvg from '@/assets/check.svg';
import FlipSvg from '@/assets/flip.svg';
import RobotSvg from '@/assets/robot.svg';
// import images
import AppleWatch from '@/assets/applewatch.jpg';
import Camera from '@/assets/sony.jpg';
import WatchFive from '@/assets/watch5.jpg';
import Galaxy from '@/assets/phone.jpg';
import Macbook from '@/assets/macbook.jpg';
export default {
  name: 'landing-page',

  components: {
    Navbar,
  },

  data: () => ({
    trackMargin: 0,
    objectPosition: 0,
    carousel: [
      { title: 'Apple Watch', image: AppleWatch },
      { title: 'Sony FX30', image: Camera },
      { title: 'Watch 5', image: WatchFive },
      { title: 'Galaxy S23 Ultra', image: Galaxy },
      { title: 'Macbook Air M1', image: Macbook },
    ],
    about: [
      {
        title: 'disain',
        description: 'ilus ja kasutajasõbralik disain',
        image: FlameSvg,
      },
      {
        title: 'lai valik',
        description: 'laenuta ükskõik mis elektroonikaseade',
        image: CheckSvg,
      },
      {
        title: 'vahetamine',
        description: 'kasuta võimalust vahetada oma seade teisega',
        image: FlipSvg,
      },
      {
        title: 'abi',
        description: 'küsi abi ja saa vastust päeva jooksul',
        image: RobotSvg,
      },
    ],
  }),

  methods: {
    moveImagesForward() {
      const width = this.$refs.image.reduce(
        (prevVal, val) => val.width + prevVal + 45,
        0
      );
      const step = width / 8;
      if (this.trackMargin >= width / 4) {
        this.trackMargin = 0;
      } else {
        this.trackMargin += step;
      }
      this.objectPosition = (this.trackMargin / width) * 3 * 100;
    },
  },
};
</script>

<style lang="scss">
* {
  user-select: none;
}

.see-more {
  position: relative;
  padding-right: 28px;
  background-image: url('@/assets/arrowright.svg');
  background-repeat: no-repeat;
  background-position: 98% 58%;

  &:hover {
    background-position: 100% 58%;
  }
}

.bg-image {
  background-image: url('@/assets/background.png');
  background-size: 100%;
  background-position: 50% 50%;
  transition: all 0.25s ease-in;

  &:hover {
    background-size: 110%;
    background-position: 50% 50%;
  }
}

.image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.custom-transition {
  transition: all 0.5s cubic-bezier(0, 0, 0, 1);
}
</style>
