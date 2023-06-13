import axios from 'axios';

const state = {
    chats: null,
    selectChat: null,
    filter: null
};

const getters = {
    chats: state => state.chats,
    selectChat: state => state.selectChat,
    filter: state => state.filter
};

const actions = {
    async getChats({commit, rootState}) {
        let res = await axios.get('chat/me', {
            headers: {
                Authorization: 'Bearer ' + rootState.accessToken
            }
        });
        await commit('setChats', res.data);
    },
    async selectChat({commit}, id) {
        let res = await axios.get('chat/get/' + id);
        await commit('selectChat', res.data);
    },
    clearMessages({commit}) {
        commit('clearChats', { root: true });
    }
};

const mutations = {
    setChats(state, chats) {
        state.chats = chats;
    },
    selectChat(state, chat) {
        state.selectChat = chat;
    },
    setFilter(state, filter) {
        state.filter = filter
    },
    clearChats(state) {
        state.chats = null;
        state.selectChat = null;
        state.selectChatMessages = null;
        state.filter = null;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};