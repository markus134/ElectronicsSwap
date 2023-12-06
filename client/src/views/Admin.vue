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
                  class="text-black/40 bg-blue-100 text-center hidden xl:table-cell"
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
                <td class="bg-white hidden xl:table-cell text-center">
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
                  <p class="truncate">{{ row.accused_username }}</p>
                </td>
                <td class="bg-white hidden md:table-cell text-center">
                  <p class="truncate">{{ row.accuser_username }}</p>
                </td>
                <td class="bg-white hidden lg:table-cell text-center">
                  <p class="truncate">{{ row.category }}</p>
                </td>
                <td class="bg-white hidden lg:table-cell text-center">
                  <p class="truncate">{{ convertSeverityToEstonian(row.severity) }}</p>
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


        <div v-if="activeTab == 'kasutajad'" class="p-6 flex flex-col gap-y-6 border-b border-gray-100">
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


        <div v-if="activeTab == 'kaebused'" class="p-6 flex flex-col gap-y-6 border-b border-gray-100">
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Pealkiri</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.title }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Kategooria</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.category }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Süüdistatu</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.accused_username }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Teavitaja</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.accuser_username }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Teavitaja kommentaarid</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ selectedRow.reporters_complaints }}</label>
          </div>
          <div class="flex flex-col gap-y-3">
            <label class="flex flex-col">Tõsidus</label>
            <label class="transition-all text-sm p-2 font-normal border outline-none rounded-lg border-gray-200 focus:border-gray-400 placeholder:text-gray-900/30 text-gray-900 p-3">{{ convertSeverityToEstonian(selectedRow.severity) }}</label>
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
            @click="changeRole(selectedRow.role, selectedRow.id)"
          >
            {{ selectedRow.role === "user" ? "Muuda adminiks" : "Muuda kasutajaks" }}
          </button>
          <a
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
            :href="'mailto:' + selectedRow.accuser_email"
            target="_blank"
          >
            Kontakteeru Süüdistatuga
          </a>
          <a
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
            :href="'mailto:' + selectedRow.accused_email"
          >
            Kontakteeru teavitajaga
          </a>
          <button 
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused' && !(!selectedRow.post_exists && selectedRow.is_post_complaint)"
            @click="selectedRow.is_post_complaint ? viewPost(selectedRow.post_or_user_id) : viewUser(selectedRow.post_or_user_id)"
          >
            {{ selectedRow.is_post_complaint === true ? "Vaata postitust" : "Vaata kasutajat" }}
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused' && selectedRow.is_post_complaint && selectedRow.post_exists"
            @click="deleteProduct(selectedRow.id, selectedRow.post_or_user_id); selectedRow.post_exists = false;"
          >
            Kustuta positutus
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="activeTab == 'kaebused'"
            @click="deleteComplaint(selectedRow.id); selectedRow = null;"
          >
            Märgi lahendatuna
          </button>
          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-red-200/30 hover:text-white/90 hover:bg-red-600/80 rounded-lg"
            v-if="!selectedRow.is_banned"
            @click="banUser(activeTab === 'kasutajad' ? selectedRow.id : selectedRow.accused_id, Math.floor(Date.now() / 1000) + 60 * 60 * 24 * 14); selectedRow.is_banned = true"
          >
            Ajutine keeld (14 päeva)
          </button>

          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-red-200/30 hover:text-white/90 hover:bg-red-600/80 rounded-lg"
            v-if="!selectedRow.is_banned"
            @click="banUser(activeTab === 'kasutajad' ? selectedRow.id : selectedRow.accused_id); selectedRow.is_banned = true;"
          >
            Deaktiveeri konto
          </button>

          <button
            class="transition-all text-xs sm:text-sm md:text-base font-regular capitalize py-2 px-6 text-gray-400/90 bg-blue-200/30 hover:text-white/90 hover:bg-blue-600/80 rounded-lg"
            v-if="selectedRow.is_banned"
            @click="unBanUser(activeTab === 'kasutajad' ? selectedRow.id : selectedRow.accused_id); selectedRow.is_banned = false"
          >
            Aktiveeri konto
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
import { useAdminStore } from '../store/modules/admin';
import { usePostsStore } from '../store/modules/posts';
import router from '../router';

export default {
  name: 'admin-page',

  components: {
    Navbar,
    Badge,
  },

  async created() {
    await this.fetchData();
  },

  methods: {
    async fetchData() {
      try {
        const adminStore = useAdminStore();
        await Promise.all([adminStore.getAllUsers(), adminStore.getComplaints()]);
        this.userRows = adminStore.allUsers;
        this.reportsRows = adminStore.allComplaints;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    convertSeverityToEstonian(severity) {
      const severityMap = {
        low: 'Madal',
        medium: 'Keskmine',
        high: 'Kõrge',
      };

      return severityMap[severity];
    },

    async changeRole(role, targetUserId) {
      const adminStore = useAdminStore();

      try {
        const response =
          role === 'user'
            ? await adminStore.changeRoleToAdmin(targetUserId)
            : await adminStore.demoteToUser(targetUserId);

        if (response === 'Success') {
          const updatedUser = this.userRows.find((user) => user.id === targetUserId);
          if (updatedUser) {
            updatedUser.role = role === 'user' ? 'admin' : 'user';
          }
        }
      } catch (error) {
        console.error('Error changing role:', error);
      }
    },

    async banUser(userId, timeExpiry = null) {
      const adminStore = useAdminStore();

      try {
        await adminStore.banUser(userId, timeExpiry);
      } catch (error) {
        console.error('Error banning user:', error);
      }
    },

    async unBanUser(userId) {
      const adminStore = useAdminStore();

      try {
        await adminStore.unbanUser(userId);
      } catch (error) {
        console.error('Error unbanning user:', error);
      }
    },

    async viewPost(id) {
      router.push('/item?post_id=' + id)
    },

    async viewUser(id) {
      router.push('/user?user_id=' + id)
    },

    async deleteProduct(postId) {
      const postsStore = usePostsStore();

      try {
        await postsStore.deleteUserPost(postId);
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    },

    async deleteComplaint(complaintId) {
      const adminStore = useAdminStore();

      try {
        await adminStore.deleteComplaint(complaintId);
        this.reportsRows = this.reportsRows.filter((complaint) => complaint.id !== complaintId);
      } catch (error) {
        console.error('Error deleting complaint:', error);
      }
    },
  },

  data: () => ({
    selectedUsersAmount: 6,
    tabs: ['kasutajad', 'kaebused'],
    activeTab: 'kasutajad',
    userRows: [],
    reportsRows: [],
    selectedRow: null,
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

