import { createPinia } from 'pinia';

export const pinia = createPinia();

// Import your store modules
import { useAuthStore } from './modules/auth';

// Register the store modules
pinia.use(useAuthStore);
