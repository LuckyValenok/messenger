import {createStore} from "vuex";
import createPersistedState from "vuex-plugin-persistedstate";

import users from './modules/users';
import chats from './modules/chats';

export default createStore({
    state: {
        accessToken: null
    },
    getters: {
        accessToken: state => state.accessToken,
    },
    actions: {
        clearAccessToken({commit}) {
            commit('setAccessToken', null);
        }
    },
    mutations: {
        setAccessToken(state, token) {
            state.accessToken = token;
        },
    },
    modules: {
        users,
        chats,
    },
    plugins: [createPersistedState()]
});