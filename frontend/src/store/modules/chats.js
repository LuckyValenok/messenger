import axios from 'axios';

const state = {
    chats: null,
    selectChat: null,
    selectChatMessages: null,
};

const getters = {
    chats: state => state.chats,
    selectChat: state => state.selectChat,
    selectChatMessages: state => state.selectChatMessages
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
    async loadMessages({commit, state}) {
        let res = await axios.get('message/get/' + state.selectChat.id);
        await commit('setMessages', res.data);
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
    setMessages(state, messages) {
        state.selectChatMessages = messages;
    },
    clearChats(state) {
        state.chats = null;
        state.selectChat = null;
        state.selectChatMessages = null;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};