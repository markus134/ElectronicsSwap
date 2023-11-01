import axios from 'axios';

const authService = axios.create({
  baseURL: import.meta.env.VITE_AUTH_URL,
  withCredentials: true, // We need this because Flask and Vue are running on separate ports (because of that they will be cross origin requests)
  xsrfCookieName: 'csrf_access_token'
});

// Add an interceptor to handle 401 errors without logging
authService.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      // Handle the 401 error as needed
      return Promise.resolve(error.response);
    }
    return Promise.reject(error);
  }
);

export { authService };