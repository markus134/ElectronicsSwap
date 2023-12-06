import { defineStore } from 'pinia';
import { authService } from '@/api';
import router from '../../router';

export const useAuthStore = defineStore('authStore', {
  state: () => ({
    authUser: {},
    modalActive: false,
  }),
  getters: {
    user: (state) => state.authUser,
    username: (state) => state.authUser.username || '',
    image_url: (state) => state.authUser.image_url,
    isLoggedIn: (state) => !!Object.keys(state.authUser).length,
    isAdmin: (state) => state.authUser.role === "admin" || state.authUser.role === "super admin"

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
        localStorage.setItem('userId', this.authUser.user_id);
        localStorage.setItem('image_url', this.authUser.image_url)
        localStorage.setItem('isLoggedIn', true);
        localStorage.setItem('role', this.authUser.role);
        return 'Successful';
      }
    },

    async logoutUser() {
      this.authUser = {};
      localStorage.removeItem('username');
      localStorage.removeItem('image_url')
      localStorage.removeItem('userId')
      localStorage.setItem('isLoggedIn', false);
      localStorage.removeItem('role');
      router.push("/");
      await authService.post('/logout');
    },

    async checkLoginStatus() {
      // Check if the username is already in the localStorage
      const storedUsername = localStorage.getItem('username');
      const storedImage = localStorage.getItem('image_url');
      const isLoggedIn = localStorage.getItem('isLoggedIn');
      const userRole = localStorage.getItem('role')
      if (storedUsername && isLoggedIn) {
        // If the username is stored, update the authUser
        this.authUser = { username: storedUsername, image_url: storedImage , role: userRole};
      } else if (!isLoggedIn) {
        // If not, make a request to get the username and store it in localStorage if token is validated
        try {
          const response = await authService.post('/check_token');
          if (response.status === 200) {
            this.authUser = { username: response.data.username, image_url: response.data.image_url, role: response.data.role };
           
            localStorage.setItem('username', response.data.username);
            localStorage.setItem('image_url', response.data.image_url);
            localStorage.setItem('userId', response.data.user_id)
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
