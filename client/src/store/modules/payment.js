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
    async makePayment(paymentDetails) {
      try {
        await paymentService.post('/make_payment', paymentDetails);
      } catch (error) {
        console.error('Error making payment:', error);
      }
    },
  },
});
