import axios from 'axios';
import {connect} from "@/utils";

const state = {
    chats: [],
    selectChatId: localStorage.getItem('selectChatId'),
    selectChat: null,
    filter: null,
    connectionForMessages: null,
    connectionForChats: null,
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
    async sendMessage({state}, text) {
        if (!state.selectChat) {
            return;
        }
        await axios.post('message/new', null, {
            params: {
                chat_id: state.selectChat.id,
                text: text
            }
        });
    },
    async createChat({commit}, data) {
        let res = await axios.post('chat/new', data);
        await commit('setSelectChat', res.data);
    },
    async addMember({state}, username) {
        await axios.post('chat/add_member/' + state.selectChat.id, null, {
            params: {
                username: username
            }
        });
    }
};

const mutations = {
    setChats(state, chats) {
        state.chats = chats;

        if (state.connectionForChats) {
            state.connectionForChats.close();
        }

        state.connectionForChats = connect("ws://localhost:8000/ws/user?token=" + localStorage.getItem('access_token'), "chats", event => {
            let newChat = JSON.parse(event.data);
            state.chats = state.chats.filter(chat => chat.id !== newChat.id);
            if (!newChat.removed) {
                state.chats.push(newChat);
            }
        });
    },
    setSelectChat(state, chat) {
        state.selectChat = chat;
        state.selectChatId = chat.id;
        localStorage.setItem('selectChatId', chat.id);

        if (state.connectionForMessages) {
            state.connectionForMessages.close();
        }

        state.connectionForMessages = connect("ws://localhost:8000/ws/chat/" + chat.id + "?token=" + localStorage.getItem('access_token'), "messages", event => {
            let data = JSON.parse(event.data);
            state.selectChat.messages.push(data);
        });
    },
    setFilter(state, filter) {
        state.filter = filter
    },
    clearState(state) {
        state.chats = [];
        state.selectChatId = null;
        state.selectChat = null;
        state.filter = null;
        state.connectionForMessages = null;
        state.connectionForChats = null;
        localStorage.removeItem('selectChatId');
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};