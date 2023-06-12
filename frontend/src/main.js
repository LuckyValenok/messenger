import {createApp} from 'vue'
import axios from 'axios';

import './assets/styles/main.css'
import App from './App.vue'
import router from './router';
import store from './store';

const app = createApp(App)

axios.defaults.baseURL = 'http://localhost:8000/';

axios.interceptors.response.use(config => {
        let token = localStorage.getItem('access_token');

        if (token) {
            config.headers['Authorization'] = 'Bearer ' + token
        }

        return config;
    },
    error => {
        if (error) {
            const originalRequest = error.config;
            if (error.response.status === 401 && !originalRequest._retry) {
                originalRequest._retry = true;
                store.dispatch('logOut');
                store.dispatch('clearMessages');
                store.dispatch('clearAccessToken');
                return router.push('/login')
            }
        }
    }
)


app.use(router)
app.use(store)
app.mount('#app')