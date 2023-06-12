import {createRouter, createWebHistory} from 'vue-router'
import SignUp from "@/components/SignUp";
import LogIn from "@/components/LogIn";
import Messenger from "@/components/MessengerVue";
import store from "@/store";

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
            path: '/',
            name: 'messenger',
            component: Messenger,
            meta: {
                requiresAuth: true
            }
        }
    ]
})

router.beforeEach((to, _, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters.isAuthenticated) {
            next();
            return;
        }
        next({name: 'login'});
    } else {
        next();
    }
});

export default router