import { defineStore } from 'pinia';
import { profileService } from '@/api';

export const useProfileStore = defineStore('profileStore', {
  state: () => ({
    userProfile: {},
    loans: [],
    sent_sales: [],
    sales: [],
    selected_product: [],
  }),
  getters: {
    id: (state) => state.userProfile.id,
    username: (state) => state.userProfile.username,
    email: (state) => state.userProfile.email,
    description: (state) => state.userProfile.description || '',
    image_url: (state) => state.userProfile.image_url,
    get_loans: (state) => state.loans,
    get_sales: (state) => state.sales,
    get_sent_sales: (state) => state.sent_sales,
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
        const response = await profileService.post('/get_sales', { sent_sales: true });
        const response2 = await profileService.post('/get_sales', { sent_sales: false });

        if (response.status === 200) {
          this.sent_sales = response.data;
          this.sales = response2.data;
        } else {
          console.error('Failed to get sales:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching sales:', error);
      }
    },
    async markSaleAsSent(saleId) {
      try {
        const response = await profileService.post('/mark_sale_as_sent', { sale_id: saleId });
    
        if (response.status === 200) {
          const index = this.sales.findIndex(sale => sale.sale_id === saleId);
    
          if (index !== -1) {
            const sale = this.sales.splice(index, 1)[0]; // Remove the sale from 'sales' and get the removed sale
            sale.is_sent = true;
            this.sent_sales.push(sale);
          } else {
            console.error(`Sale with ID ${saleId} not found in 'sales' array.`);
          }
        } else {
          console.error('Failed to mark sale as sent:', response.statusText);
        }
      } catch (error) {
        console.error('Error marking sale as sent:', error);
      }
    },
  },
});
