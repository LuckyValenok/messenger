import { createApp } from 'vue'
import App from './App.vue'


import './assets/styles/main.css'
import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import SignUp from "@/components/SignUp/SignUp.vue";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'root',
            component: HelloWorld
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignUp
        }
    ]
})


const app = createApp(App)
app.use(router)
app.mount('#app')