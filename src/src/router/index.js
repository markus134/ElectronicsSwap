import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Forgot_password from '@/views/Forgot_password.vue'
const routes = [
  { name: 'landing-page', path: '/', component: LandingPage },
  { name: 'forgot_password', path: '/forgot_password', component: Forgot_password}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
