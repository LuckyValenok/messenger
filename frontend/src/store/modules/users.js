import axios from 'axios';

const state = {
    user: null,
};

const getters = {
    user: state => state.user,
};

const actions = {
    async signUp({dispatch}, form) {
        await axios.post('user/new', form);
        let UserForm = new FormData();
        UserForm.append('username', form.login);
        UserForm.append('password', form.password);
        await dispatch('logIn', UserForm);
    },
    async logIn({dispatch, commit}, user) {
        let res = await axios.post('login/', user);
        await commit('setAccessToken', res.data.access_token, {root: true})
        await dispatch('viewMe');
    },
    async viewMe({commit, rootState}) {
        let res = await axios.get('user/me', {
            headers: {
                Authorization: 'Bearer ' + rootState.accessToken
            }
        });
        await commit('setUser', res.data);
    },
    logOut({commit}) {
        commit('setUser', null);
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