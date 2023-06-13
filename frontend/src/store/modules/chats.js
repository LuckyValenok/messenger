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
    async getChats({commit, rootState}) {
        let res = await axios.get('chat/me', {
            headers: {
                Authorization: 'Bearer ' + rootState.accessToken
            }
        });
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