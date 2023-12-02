import axios from 'axios';
import router from './router';

const createAxiosInstance = (baseURL) => {
  const instance = axios.create({
    baseURL,
    withCredentials: true,
    xsrfCookieName: 'csrf_access_token',
  });

  // Add an interceptor to handle 401 errors without logging
  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response.status === 401 || error.response.status === 400) {
        // Handle the 401 error as needed
        return Promise.resolve(error.response);
      }
      return Promise.reject(error);
    }
  );

  // Add an interceptor to handle 422 errors
  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response.status === 422 || error.response.status === 403) {
        localStorage.setItem('isLoggedIn', false);
        localStorage.removeItem('username');
        localStorage.removeItem('image_url');
        localStorage.removeItem('userId');
        localStorage.removeItem('role');
        router.push('/login');
      }
      return Promise.reject(error);
    }
  );

  return instance;
};

const authService = createAxiosInstance(import.meta.env.VITE_AUTH_URL);
const profileService = createAxiosInstance(import.meta.env.VITE_PROFILE_URL);
const postsService = createAxiosInstance(import.meta.env.VITE_POSTS_URL);
const adminService = createAxiosInstance(import.meta.env.VITE_ADMIN_URL);

export { authService, profileService, postsService, adminService };
