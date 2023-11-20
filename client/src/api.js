import axios from 'axios';

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
      if (error.response.status === 401) {
        // Handle the 401 error as needed
        return Promise.resolve(error.response);
      }
      return Promise.reject(error);
    }
  );

  return instance;
};

const authService = createAxiosInstance(import.meta.env.VITE_AUTH_URL);
const profileService = createAxiosInstance(import.meta.env.VITE_PROFILE_URL);

export { authService, profileService };
