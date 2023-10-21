import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Login from '@/views/Login.vue'; // Import the Login component

const routes = [
  { name: 'landing-page', path: '/', component: LandingPage },
  { name: 'login', path: '/login', component: Login }, // Add a new route for the login page
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
