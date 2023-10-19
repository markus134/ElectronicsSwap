import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';

const routes = [{ name: 'landing-page', path: '/', component: LandingPage }];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
