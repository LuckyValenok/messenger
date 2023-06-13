import axios from 'axios';

const state = {
    chats: null,
    selectChatId: localStorage.getItem('selectChatId'),
    selectChat: null,
    filter: null
};

const getters = {
    chats: state => state.chats,
    selectChatId: state => state.selectChatId,
    selectChat: state => state.selectChat,
    filter: state => state.filter
};

const actions = {
    async getChats({commit}) {
        let res = await axios.get('chat/me');
        await commit('setChats', res.data);
    },
    async selectChat({commit}, id) {
        if (id == null) {
            return;
        }
        let res = await axios.get('chat/get/' + id);
        await commit('setSelectChat', res.data);
    },
    clearMessages({commit}) {
        commit('clearState');
    },
    async sendMessage({rootState}, text) {
        if (!rootState.chats.selectChat) {
            return;
        }
        await axios.post('message/new', null, {
            params: {
                chat_id: rootState.chats.selectChat.id,
                text: text
            }
        })
    }
};

const mutations = {
    setChats(state, chats) {
        state.chats = chats;
    },
    setSelectChat(state, chat) {
        state.selectChat = chat;
        state.selectChatId = chat.id;
        localStorage.setItem('selectChatId', chat.id);
    },
    setFilter(state, filter) {
        state.filter = filter
    },
    clearState(state) {
        state.chats = null;
        state.selectChatId = null;
        state.selectChat = null;
        state.filter = null;
        localStorage.removeItem('selectChatId');
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};