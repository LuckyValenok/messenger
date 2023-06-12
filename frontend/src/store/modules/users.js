import axios from 'axios';

const state = {
    login: null,
};

const getters = {
    isAuthenticated: state => !!state.login,
};

const actions = {
    async signUp({dispatch}, form) {
        await axios.post('user/new', form);
        let UserForm = new FormData();
        UserForm.append('username', form.login);
        UserForm.append('password', form.password);
        await dispatch('logIn', UserForm);
    },
    async logIn({dispatch}, user) {
        await axios.post('login', user);
        await dispatch('viewMe');
    }
};

const mutations = {
    setUser(state, login) {
        state.login = login;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};