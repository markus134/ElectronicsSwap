<template>
  <div class="relative h-screen w-full bg-gray-100">
    <navbar></navbar>
    <div
      class="relative h-full w-full pt-[175px] lg:pt-[150px] lg:pb-[30px] px-[15px] md:px-[75px] flex flex-col-reverse lg:flex-row gap-4 lg:gap-8"
    >
      <ul
        class="bg-white flex lg:h-full flex-row lg:flex-col justify-evenly lg:justify-start gap-4 rounded-t-lg lg:rounded-lg lg:px-1.5 lg:py-4"
      >
        <li :key="tab" v-for="tab in tabs">
          <button
            class="transition-all px-1 py-2 lg:px-8 lg:py-4 text-sm lg:text-base font-semibold rounded-lg capitalize"
            :class="
              activeTab == tab
                ? 'text-blue-600 lg:bg-gray-100'
                : 'lg:hover:bg-gray-100 text-gray-950'
            "
            @click="activeTab = tab"
          >
            {{ tab }}
          </button>
        </li>
      </ul>
      <div class="relative w-full h-full flex flex-col gap-y-4 lg:gap-y-8">
        <div class="w-full">
          <h1 class="text-2xl text-blue-600 font-semibold capitalize">
            {{ activeTab }}
          </h1>
        </div>
        <div class="w-full flex gap-x-3">
          <input
            type="text"
            class="w-full py-2 px-4 xl:py-4 xl:px-8 outline-none rounded-lg"
            placeholder="Otsi"
          />
          <button class="down-arrow text-lg outline-none">Sorteeri</button>
        </div>
        <div class="relative w-full h-full overflow-hidden">
          <div class="w-full h-full overflow-y-auto pr-3 custom-scrollbar">
            <!-- Users table -->
            <table
              class="relative w-full table-fixed"
              v-if="activeTab == 'kasutajad'"
            >
              <tr class="sticky top-0 left-0">
                <th
                  class="text-black/40 bg-blue-100 text-start py-6 pl-6 sm:pl-16 rounded-tl-lg"
                >
                  #
                </th>
                <th class="text-black/40 bg-blue-100 text-start">Kasutaja</th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden md:table-cell"
                >
                  Roll
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden lg:table-cell"
                >
                  Loomiskuupäev
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-end rounded-tr-lg pr-6 sm:pr-16"
                >
                  Tegevus
                </th>
              </tr>
              <tr
                class="transition-all border-b cursor-pointer hover:brightness-[.96]"
                :key="i"
                v-for="(row, i) in userRows"
                @click="selectedRow = row"
              >
                <td class="pl-6 sm:pl-16 text-start bg-white">{{ i + 1 }}</td>
                <td
                  class="flex flex-col h-full w-full gap-y-2 py-6 bg-white text-start justify-center"
                >
                  <h5 class="truncate text-sm font-semibold">
                    {{ row.username }}
                  </h5>
                  <p class="truncate text-xs hidden sm:block">
                    {{ row.email }}
                  </p>
                </td>
                <td class="bg-white hidden md:table-cell text-center">
                  <badge :status="row.role"></badge>
                </td>
                <td class="bg-white hidden lg:table-cell text-center">
                  <p class="truncate">{{ row.createdAt }}</p>
                </td>
                <td class="bg-white text-end text-end pr-6 sm:pr-16">
                  <button><img src="@/assets/edit.svg" alt="" /></button>
                </td>
              </tr>
            </table>
            <!-- Reports table -->
            <table
              class="relative w-full table-fixed"
              v-if="activeTab == 'kaebused'"
            >
              <tr class="sticky top-0 left-0">
                <th
                  class="text-black/40 bg-blue-100 text-start py-6 pl-6 sm:pl-16 rounded-tl-lg"
                >
                  #
                </th>
                <th class="text-black/40 bg-blue-100 text-start">Pealkiri</th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden md:table-cell"
                >
                  Süüdistatu
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden md:table-cell"
                >
                  Teavitaja
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden lg:table-cell"
                >
                  Kategooria
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-center hidden lg:table-cell"
                >
                  Tõsidus
                </th>
                <th
                  class="text-black/40 bg-blue-100 text-end rounded-tr-lg pr-6 sm:pr-16"
                >
                  <p>Tegevus</p>
                </th>
              </tr>
              <tr
                class="border-b"
                :key="i"
                v-for="(row, i) in reportsRows"
                @click="selectedRow = row"
              >
                <td class="pl-6 sm:pl-16 text-start bg-white">{{ i + 1 }}</td>
                <td class="bg-white text-start">
                  <p class="truncate">{{ row.title }}</p>
                </td>
                <td class="bg-white hidden md:table-cell text-center">
                  <p class="truncate">{{ row.accused }}</p>
                </td>
                <td class="bg-white hidden md:table-cell text-center">
                  <p class="truncate">{{ row.informer }}</p>
                </td>
                <td class="bg-white hidden lg:table-cell text-center">
                  <p class="truncate">{{ row.category }}</p>
                </td>
                <td class="bg-white hidden lg:table-cell text-center">
                  <p class="truncate">{{ row.severity }}</p>
                </td>
                <td class="bg-white text-end pr-6 sm:pr-16 py-3">
                  <button
                    class="transition-all px-3 py-1 sm:px-6 sm:py-2 bg-blue-600/10 hover:bg-blue-600/30 active:bg-blue-600/60 text-blue-600 rounded-lg"
                  >
                    Vaata rohkem
                  </button>
                </td>
              </tr>
            </table>
          </div>
        </div>
        <div
          class="flex justify-center items-center gap-x-3 md:gap-x-6 lg:gap-x-12"
        >
          <p class="text-sm text-gray-600/50 hidden sm:block">
            Kirjed lehekülje kohta
          </p>
          <select
            class="bg-transparent text-sm cursor-pointer outline-none"
            name="pages"
            id="pages"
            v-model="selectedUsersAmount"
          >
            <option value="6">6</option>
            <option value="9">9</option>
            <option value="12">12</option>
            <option value="16">16</option>
          </select>
          <p class="text-sm text-gray-600/50">1-2 10st</p>
          <button class="p-3">
            <img src="@/assets/arrowright.svg" class="rotate-180" alt="" />
          </button>
          <button class="p-3">
            <img src="@/assets/arrowright.svg" alt="" />
          </button>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div
      class="absolute top-0 left-0 w-full h-screen flex items-center justify-center z-[1000]"
      v-if="selectedRow"
    >
      <div
        class="relative max-h-[90%] w-11/12 md:w-10/12 lg:w-9/12 bg-white rounded-lg text-lg font-semibold z-[1001] overflow-auto"
      >
        <div
          class="w-full flex items-center justify-between p-6 border-b border-gray-100 gap-x-6"
        >
          <h3 class="capitalize">{{ activeTab }}</h3>
          <button
            class="transition-all p-3 hover:bg-gray-100 rounded-lg"
            @click="selectedRow = null"
          >
            <img src="@/assets/cross.svg" alt="" />
          </button>
        </div>


        <div class="p-6 flex flex-col gap-y-6 border-b border-gray-100">
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Kasutajanimi</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.username }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Email</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.email }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Kirjeldus</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.description }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Roll</label>
            <label class="transition-all capitalize text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.role }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Loomiskuupäev</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.createdAt }}</label>
          </div>
          

        </div>
        <div
          class="w-full px-6 py-4 flex flex-col sm:flex-row flex-wrap items-start sm:items-center gap-y-3 gap-x-6"
        >
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular py-2 px-6 text-gray-400/90 bg-gray-200/30 hover:text-white/90 hover:bg-gray-600/80 rounded-lg"
            @click="selectedRow = null"
          >
            Katkesta
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kasutajad'"
          >
            Muuda adminiks
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Kontakteeru Süüdistatuga
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Kontakteeru teavitajaga
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Vaata postitust
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Kustuta positutus
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Märgi lahendatuna
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
          >
            Ajutine keeld (14 päeva)
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-red-200/30 hover:text-white/90 hover:bg-red-600/80 rounded-lg"
          >
            Kustuta konto
          </button>
        </div>
      </div>
      <div
        class="absolute top-0 left-0 w-full h-full bg-gray-950/70 cursor-pointer"
        @click="selectedRow = null"
      ></div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Badge from '@/components/Badge.vue';
import { useAdminStore } from "../store/modules/admin";

export default {
  name: 'admin-page',

  components: {
    Navbar,
    Badge,
  },

  async created() {
    const adminStore = useAdminStore();
    await adminStore.getAllUsers();
    this.userRows = adminStore.allUsers;
    
  },
  data: () => ({
    selectedUsersAmount: 6,
    tabs: ['kasutajad', 'kaebused'],
    activeTab: 'kasutajad',
    userRows: [
      {
        username: 'David Wagner',
        email: 'davig_wagner@example.com',
        role: 'super admin',
        createdAt: '24 Okt, 2015',
      },
      {
        username: 'Ina Hogan',
        email: 'windler.warren@runte.net',
        role: 'admin',
        createdAt: '25 Okt, 2015',
      },
      {
        username: 'Lena Page',
        email: 'camila_ledner@gmail.com',
        role: 'kasutaja',
        createdAt: '27 Okt, 2015',
      },
    ],
    reportsRows: [
      {
        title: 'pealkiri',
        accused: 'süüdistatu',
        informer: 'teavitaja',
        category: 'kategooria',
        severity: 'tõsidus',
      },
      {
        title: 'pealkiri',
        accused: 'süüdistatu',
        informer: 'teavitaja',
        category: 'kategooria',
        severity: 'tõsidus',
      },
      {
        title: 'pealkiri',
        accused: 'süüdistatu',
        informer: 'teavitaja',
        category: 'kategooria',
        severity: 'tõsidus',
      },
    ],
    selectedRow: null,
    enToEe: {
      username: 'kasutajanimi',
      email: 'meil',
      role: 'roll',
      createdAt: 'loomiskuupäev',
      title: 'pealkiri',
      accused: 'süüdistatu',
      informer: 'teavitaja',
      category: 'kategooria',
      severity: 'tõsidus',
    },
    inputs: {
      username: '',
      email: '',
      role: '',
      createdAt: '',
    },
  }),

  watch: {
    selectedUsersAmount(value) {
      this.selectedUsersAmount = +value;
    },
  },
};
</script>
