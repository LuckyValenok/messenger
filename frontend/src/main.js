import {createApp} from 'vue'
import axios from 'axios';

import './assets/styles/main.css'
import App from './App.vue'
import router from './router';
import store from './store';

const app = createApp(App)

axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.headers.common["Authorization"] = "Bearer " + localStorage.getItem("access_token");

axios.interceptors.response.use(undefined,
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

app.mixin({
    methods: {
        convertDateTimeFull: datetime => {
            let date = new Date(Date.parse(datetime) - new Date().getTimezoneOffset() * 60000);
            const options = {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: 'numeric',
                minute: 'numeric'
            };
            return date.toLocaleDateString('en-US', options);
        },
        convertDateTime: datetime => {
            let now = new Date();
            let date = new Date(Date.parse(datetime) - now.getTimezoneOffset() * 60000);

            const diff = now - date;

            const seconds = Math.floor(diff / 1000);
            const minutes = Math.floor(seconds / 60);
            const hours = Math.floor(minutes / 60);
            const days = Math.floor(hours / 24);

            if (diff < 0) {
                return 'Message from the future!';
            } else if (seconds < 60) {
                return 'Just now';
            } else if (minutes < 60) {
                return `${minutes} minutes ago`;
            } else if (hours < 24) {
                return `${hours} hours ago`;
            } else if (days === 1) {
                return 'Yesterday';
            } else if (days < 7) {
                return `${days} days ago`;
            } else {
                const options = {year: 'numeric', month: 'long', day: 'numeric', timeZone: 'Asia/Yekaterinburg'};
                return date.toLocaleDateString('en-US', options);
            }
        },
        capitalize: word => word.charAt(0).toUpperCase() + word.slice(1),
    },
})

app.use(router)
app.use(store)
app.mount('#app')