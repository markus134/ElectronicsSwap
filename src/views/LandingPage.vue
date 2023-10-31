<template>
  <div class="landing-page">
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
          <a
            href=""
            class="px-6 py-2 sm:px-9 sm:py-3 bg-white rounded-lg text-[1.5em] sm:text-[3em] md:text-[4em] sm:whitespace-nowrap"
            >Alusta kasutamist</a
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
      <!-- 
      Popular devices block
      
      TODO: Create normal scrolling
      ? Add scrolling animation with parallax
      -->
      <div
        class="relative w-full h-screen pl-[30px] py-[75px] sm:pl-[75px] sm:py-[150px] flex flex-col justify-center gap-y-[30px]"
      >
        <h2 class="text-[1.5em] sm:text-[3em] md:text-[4em] pr-[30px]">
          Kõige populaarsemad seadmed laenutamiseks
        </h2>
        <!-- Devices list -->
        <ul
          class="stylize-scrollbar relative whitespace-nowrap overflow-x-auto overflow-y-clip"
          @drag="drag"
        >
          <li
            class="mx-3 inline-block h-full w-10/12 lg:w-1/4 aspect-square bg-black rounded-lg"
            :key="i"
            v-for="i in 5"
          >
            <a
              href=""
              class="w-full h-full flex items-center justify-center text-2em xl:text-[3em] text-white"
              >Iphone 15 Pro</a
            >
          </li>
        </ul>
        <div class="w-full flex justify-end pr-[30px] sm:pr-[75px]">
          <a href="#" class="transition-all text-[16px] sm:text-[32px] see-more"
            >sirvi rohkem</a
          >
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
          <a
            href="#"
            class="transition-all text-center bg-gray-100 px-6 sm:px-12 py-3 sm:py-6 rounded-lg text-xl sm:text-3xl hover:bg-[#B4BEEF] hover:text-white"
            >Ole esimene! Jätta tagasiside!</a
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
            <li><a href="" class="text-[32px] text-white">Meist</a></li>
            <li><a href="" class="text-[32px] text-white">Küsida Abi</a></li>
            <li><a href="" class="text-[32px] text-white">Tagasiside</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import FlameSvg from '@/assets/flame.svg';
import CheckSvg from '@/assets/check.svg';
import FlipSvg from '@/assets/flip.svg';
import RobotSvg from '@/assets/robot.svg';
export default {
  name: 'landing-page',

  data: () => ({
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
    drag(e) {
      console.log(e.offsetX);
    },
  },
};
</script>

<style lang="scss">
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
</style>
