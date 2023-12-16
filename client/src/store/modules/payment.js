import { defineStore } from 'pinia';
import { paymentService } from '@/api';

export const usePaymentStore = defineStore('paymentStore', {
  state: () => ({
    totalCartPrice: null,
  }),
  getters: {
    getTotalCartPrice: (state) => state.totalCartPrice,
  },
  actions: {
    async fetchTotalCartPrice() {
        try {
          const response = await paymentService.post('/get_total_price');
          this.totalCartPrice = response.data.total_price;
        } catch (error) {
          console.error('Error fetching total cart price:', error);
        }
      },
      async makePayment(paymentDetails) {
        try {
          const response = await paymentService.post('/make_payment', paymentDetails);
          // Assuming the API response indicates a successful payment
          console.log(response);
          // You may want to perform additional actions or handle success in your application
        } catch (error) {
          console.error('Error making payment:', error);
          // Handle errors or show appropriate messages to the user
        }
      },
  },
});
