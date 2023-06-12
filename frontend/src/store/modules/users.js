import axios from 'axios';

const state = {
    user: null,
};

const getters = {
    isAuthenticated: state => !!state.user,
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
        let res = await axios.post('login', user);
        await localStorage.setItem('access_token', res.data.access_token);
        await dispatch('viewMe');
    },
    async viewMe({commit}) {
        let data = await axios.get('user/me', {
            headers: {
                Authorization: 'Bearer ' + localStorage.getItem('access_token')
            }
        })
        await commit('setUser', data);
    },
    async logOut({commit}) {
        let user = null;
        localStorage.removeItem('access_token')
        commit('setUser', user);
    }
};

const mutations = {
    setUser(state, user) {
        state.user = user;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};