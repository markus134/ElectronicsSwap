import { createPinia } from 'pinia';
import { defineStore } from 'pinia';
import { provide } from 'vue';

export const pinia = createPinia();

// Import your store modules
import { useAuthStore } from './modules/auth';

// Register the store modules
pinia.use(useAuthStore);

