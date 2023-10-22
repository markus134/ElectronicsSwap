import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Registration from '@/views/Registration.vue'

const routes = [
  { name: 'landing-page', path: '/', component: LandingPage },
  { name: 'registration', path: '/registration', component: Registration}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
