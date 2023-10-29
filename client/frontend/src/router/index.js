import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Login from '@/views/Login.vue';
import Registration from '@/views/Registration.vue';
import Tagasiside from '@/views/Tagasiside.vue';
import Forgot_password from '@/views/Forgot_password.vue'
import Email_sent from '@/views/Email_sent.vue'

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
  },
  {
    name: 'forgot_password',
    path: '/forgot_password',
    component: Forgot_password
  },
  {
    name: 'email_sent',
    path: '/email_sent',
    component: Email_sent
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
