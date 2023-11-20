import { createPinia } from 'pinia';

export const pinia = createPinia();

// Import your store modules
import { useAuthStore } from './modules/auth';
import { useProfileStore } from './modules/profile';

// Register the store modules
pinia.use(useAuthStore);
pinia.use(useProfileStore);

