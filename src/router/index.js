import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Login from '@/views/Login.vue';
import Registration from '@/views/Registration.vue';
import Tagasiside from '@/views/Tagasiside.vue'; // Import the Login component

const routes = [
  {
    name: 'landing-page',
    path: '/',
    component: LandingPage,
  },
  {
    name: 'login',
    path: '/login',
    component: Login,
  },
  {
    name: 'tagasiside',
    path: '/tagasiside',
    component: Tagasiside,
  },
  {
    name: 'registration',
    path: '/registration',
    component: Registration
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
