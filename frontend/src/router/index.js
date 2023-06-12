import {createRouter, createWebHistory} from 'vue-router'
import SignUp from "@/components/SignUp";
import LogIn from "@/components/LogIn";
import Messenger from "@/components/MessengerVue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/signup',
            name: 'signup',
            component: SignUp
        },
        {
            path: '/login',
            name: 'login',
            component: LogIn
        },
        {
            path: '/messenger',
            name: 'messenger',
            component: Messenger
        }
    ]
})

export default router