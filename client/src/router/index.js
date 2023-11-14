import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Login from '@/views/Login.vue';
import Registration from '@/views/Registration.vue';
import Tagasiside from '@/views/Tagasiside.vue';
import Forgot_password from '@/views/Forgot_password.vue'
import Email_sent from '@/views/Email_sent.vue'
import Tagasiside_saadud from "@/views/Tagasiside_saadud.vue";
import Vahetus from "@/views/Vahetus.vue";
import Kinnitus from "@/views/Kinnitus.vue";
import Usaldus from "@/views/Usaldus.vue";
import Laenutamine from "@/views/Laenutamine.vue";
import Loo_pakkumine from "@/views/Loo_pakkumine.vue";
import User from "@/views/User.vue";
import Ostukorv from "@/views/Ostukorv.vue";
import Payment from "@/views/Payment.vue"

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
  },
  {
    name: 'tagasiside_saaadud',
    path: '/tagasiside2',
    component: Tagasiside_saadud
  },
  {
    name: 'vahetus',
    path: '/vahetus',
    component: Vahetus
  },
  {
    name: 'kinnitus',
    path: '/kinnitus',
    component: Kinnitus
  },
  {
    name: 'usaldus',
    path: '/usaldus',
    component: Usaldus
  },
  {
    name: 'laenutamine',
    path: '/laenutamine',
    component: Laenutamine
  },
  {
    name: 'ostukorv',
    path: '/ostukorv',
    component: Ostukorv
  },
  {
    name: 'user',
    path: '/user',
    component: User
  },
  {
    name: 'loo_pakkumine',
    path: '/loo_pakkumine',
    component: Loo_pakkumine
  },
  {
    name: 'payment',
    path: '/payment',
    component: Payment
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
