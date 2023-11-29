import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/views/LandingPage.vue';
import Login from '@/views/Login.vue';
import Registration from '@/views/Registration.vue';
import Tagasiside from '@/views/Tagasiside.vue';
import Forgot_password from '@/views/Forgot_password.vue';
import Email_sent from '@/views/Email_sent.vue';
import Tagasiside_saadud from '@/views/Tagasiside_saadud.vue';
import Vahetus from '@/views/Vahetus.vue';
import Kinnitus from '@/views/Kinnitus.vue';
import Usaldus from '@/views/Usaldus.vue';
import Laenutamine from '@/views/Laenutamine.vue';
import Loo_pakkumine from '@/views/Loo_pakkumine.vue';
import User from '@/views/User.vue';
import Ostukorv from '@/views/Ostukorv.vue';
import Item from '@/views/Item.vue';
import Payment from '@/views/Payment.vue';
import Admin from '@/views/Admin.vue';
import { useAuthStore } from '../store/modules/auth';

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
    component: Registration,
  },
  {
    name: 'forgot_password',
    path: '/forgot_password',
    component: Forgot_password,
  },
  {
    name: 'email_sent',
    path: '/email_sent',
    component: Email_sent,
  },
  {
    name: 'tagasiside_saaadud',
    path: '/tagasiside2',
    component: Tagasiside_saadud,
  },
  {
    name: 'vahetus',
    path: '/vahetus',
    component: Vahetus,
  },
  {
    name: 'kinnitus',
    path: '/kinnitus',
    component: Kinnitus,
  },
  {
    name: 'usaldus',
    path: '/usaldus',
    component: Usaldus,
  },
  {
    name: 'laenutamine',
    path: '/laenutamine',
    component: Laenutamine,
  },
  {
    name: 'ostukorv',
    path: '/ostukorv',
    component: Ostukorv,
    meta: { requiresAuth: true },
  },
  {
    name: 'user',
    path: '/user',
    component: User,
  },
  {
    name: 'loo_pakkumine',
    path: '/loo_pakkumine',
    component: Loo_pakkumine,
    meta: { requiresAuth: true },
  },
  {
    name: 'item-page',
    path: '/item',
    component: Item,
  },
  {
    name: 'payment',
    path: '/payment',
    component: Payment,
  },
  {
    name: 'admin',
    path: '/admin',
    component: Admin,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

/// Add a beforeEach route navigation guard
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();

  try {
    // Check login status before navigating to a protected route
    await authStore.checkLoginStatus();

    if (to.meta.requiresAuth) {
      // If the route requires authentication
      if (!authStore.isLoggedIn) {
        // Redirect to the login page if not authenticated
        next('/login');
      } else if (to.name === 'admin' && !authStore.isAdmin) {
        // Redirect to another page if the user is not an admin
        next('/');
      } else {
        // Continue with the navigation
        next();
      }
    } else {
      // Continue with the navigation for public routes
      next();
    }
  } catch (error) {
    console.error(error);
    next();
  }
});

export default router;
