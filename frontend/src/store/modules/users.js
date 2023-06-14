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
    async viewMe({commit}) {
        let res = await axios.get('user/me');
        if (res.data) {
            await commit('setUser', res.data);
        }
    },
    logOut({commit}) {
        commit('setUser', null);
    },
    async changeName({commit, state}, newName) {
        let res = await axios.put('user/change_name', {
            new_name: newName
        });
        if (res.data && state.user.name === res.data) {
            await commit('setName', newName);
        }
    }
};

const mutations = {
    setUser(state, user) {
        state.user = user;
    },
    setName(state, newName) {
        state.user.name = newName;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};