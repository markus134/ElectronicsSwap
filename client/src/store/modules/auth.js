import { defineStore } from 'pinia';
import { authService } from '@/api';

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    authUser: {},
  }),
  getters: {
    user: (state) => state.authUser,
    isLoggedIn: (state) => !!Object.keys(state.authUser).length,
  },
  actions: {
    async registerUser(user) {
      const response = await authService.post('/registration', user);
      if (response.status === 401) {
        return response.data.message;
      } else {
        return 'Successful';
      }
    },
    async loginUser(user) {
      const response = await authService.post('/login', user);
      if (response.status === 401) {
        return response.data.message;
      } else {
        this.authUser = user;

        return 'Successful';
      }
    },
  },
});
