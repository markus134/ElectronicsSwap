import { createApp } from 'vue';
import App from './App.vue';
import '@/style/style.scss';
import router from '@/router';
import store from '@/store';

createApp(App)
  .use(router)
  .use(store)
  .mount('#app');
