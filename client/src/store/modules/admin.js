import { defineStore } from 'pinia';
import { adminService } from '@/api';  // Import adminService from your API

export const useAdminStore = defineStore('adminStore', {
  state: () => ({
    all_users: [],
  }),
  getters: {
    allUsers: (state) => state.all_users,
  },
  actions: {
    async getAllUsers() {
      try {
        const response = await adminService.get('/get_all_users');
        if (response.status === 200) {
          this.all_users = response.data;
        }
      } catch (error) {
        console.error('Failed to get all users:', error);
      }
    },
  },
});
