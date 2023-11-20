import { defineStore } from 'pinia';
import { profileService } from '@/api';

export const useProfileStore = defineStore('profileStore', {
  state: () => ({
    userProfile: {},
  }),
  getters: {
    id: (state) => state.userProfile.id,
    username: (state) => state.userProfile.username,
    email: (state) => state.userProfile.email,
    description: (state) => state.userProfile.description || '',
    image_url: (state) => state.userProfile.image_url,
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
  },
});
