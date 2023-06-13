import axios from 'axios';

const state = {
    chats: null,
    selectChatId: localStorage.getItem('selectChatId'),
    selectChat: null,
    filter: null,
    connection: null,
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

        if (state.connection) {
            state.connection.close();
        }

        console.log("Starting connection to WebSocket Server")
        state.connection = new WebSocket("ws://localhost:8000/ws/chat/" + chat.id + "?token=" + localStorage.getItem('access_token'));

        state.connection.onmessage = event => {
            let data = JSON.parse(event.data);
            state.selectChat.messages.push(data);
        };
    },
    setFilter(state, filter) {
        state.filter = filter
    },
    clearState(state) {
        state.chats = null;
        state.selectChatId = null;
        state.selectChat = null;
        state.filter = null;
        state.connection = null;
        localStorage.removeItem('selectChatId');
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};