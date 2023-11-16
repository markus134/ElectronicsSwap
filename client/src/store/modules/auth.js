import { defineStore } from 'pinia';
import { authService } from '@/api';
import router from '../../router';

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    authUser: {},
  }),
  getters: {
    user: (state) => state.authUser,
    username: (state) => state.authUser.username || '',
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
        this.authUser = response.data.user;
        localStorage.setItem('username', user.username);
        localStorage.setItem('isLoggedIn', true);
        return 'Successful';
      }
    },

    async logoutUser() {
      await authService.post('/logout');
      this.authUser = {};
      localStorage.removeItem('username');
      localStorage.setItem('isLoggedIn', false);
      router.push("/");
    },

    async checkLoginStatus() {
      // Check if the username is already in the localStorage
      const storedUsername = localStorage.getItem('username');
      const isLoggedIn = localStorage.getItem('isLoggedIn');
      if (storedUsername && isLoggedIn) {
        // If the username is stored, update the authUser
        this.authUser = { username: storedUsername };
      } else if (!isLoggedIn) {
        // If not, make a request to get the username and store it in localStorage if token is validated
        try {
          const response = await authService.post('/check_token');
          if (response.status === 200) {
            this.authUser = { username: response.data.username };
            localStorage.setItem('username', response.data.username);
            localStorage.setItem('isLoggedIn', true);
          } else {
            localStorage.setItem('isLoggedIn', false);
          }
        } catch (error) {
          console.error('Token validation failed:', error);
        }
      }
    }
    
  },
});
