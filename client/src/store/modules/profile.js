import { defineStore } from 'pinia';
import { profileService } from '@/api';

export const useProfileStore = defineStore('profileStore', {
  state: () => ({
    userProfile: {},
    loans: [],
    sales: [],
    purchases: [],
  }),
  getters: {
    id: (state) => state.userProfile.id,
    username: (state) => state.userProfile.username,
    email: (state) => state.userProfile.email,
    description: (state) => state.userProfile.description || '',
    image_url: (state) => state.userProfile.image_url,
    get_loans: (state) => state.loans,
    get_sales: (state) => state.sales,
    get_purchases: (state) => state.purchases,
  },
  actions: {
    async updateProfile(profileData) {
      try {
        const response = await profileService.post('/change_user_info', profileData);
        if (response.status === 200) {
          return response.data.image_url;
        } else {
          console.error('Failed to update user profile:', response.statusText);
        }
      } catch (error) {
        console.error('Error updating user profile:', error);
      }
    },
    async getUserInfo(id) {
      try {
        const response = await profileService.post('/get_user', { id });
        if (response.status === 200) {
          this.userProfile = response.data;
        } else {
          console.error('Failed to get user info:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching user info:', error);
      }
    },
    async getLoans() {
      try {
        const response = await profileService.post('/get_loans');
        if (response.status === 200) {
          this.loans = response.data;
        } else {
          console.error('Failed to get loans:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching loans:', error);
      }
    },
    async getSales() {
      try {
        const response = await profileService.post('/get_sales');
        if (response.status === 200) {
          this.sales = response.data;
        } else {
          console.error('Failed to get sales:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching sales:', error);
      }
    },
    async getPurchases() {
      try {
        const response = await profileService.post('/get_purchases');
        if (response.status === 200) {
          this.purchases = response.data;
        } else {
          console.error('Failed to get purchases:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching purchases:', error);
      }
    },
  },
});
