import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Email_sent from '@/views/Email_sent.vue'

const routes = [
  { name: 'landing-page', path: '/', component: LandingPage },
  { name: 'email_sent', path: '/email_sent', component: Email_sent}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
