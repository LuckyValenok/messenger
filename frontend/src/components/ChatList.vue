<template>
  <header>
  </header>

  <main>
    <ChatNavbar/>
    <ChatSearch/>
    <div v-if="chats">
      <div v-for="chat in filteredChats" :key="chat.id" class="chats">
        <ChatListItem v-bind:chat="chat"/>
      </div>
    </div>

    <div class="page">
      <button type="submit" @click="showModal">+</button>
      <NewChatModal ref="modal"></NewChatModal>
    </div>
  </main>
</template>

<script>
import ChatListItem from "@/components/ChatListItem.vue";
import ChatSearch from "@/components/ChatSearch.vue";
import ChatNavbar from "@/components/ChatListNavbar.vue";
import {mapGetters} from "vuex";
import NewChatModal from "@/components/NewChatModal.vue";

export default {
  name: "ChatList",
  components: {NewChatModal, ChatSearch, ChatListItem, ChatNavbar},
  methods: {
            showModal: function () {
                this.$refs.modal.show = true
            }
  },
  created: async function () {
    try {
      await this.$store.dispatch('getChats');
    } catch (e) {
      console.log(e);
    }
  },
  computed: {
    ...mapGetters({chats: 'chats', filter: 'filter'}),
    filteredChats() {
      return this.filter == null || this.filter === '' ? this.chats : this.chats.filter(chat => {
        return chat.name.toLowerCase().includes(this.filter.toLowerCase())
      })
    }
  },
}
</script>

<style lang="less" scoped>
main {
  background: #F3F3F7;
  position: fixed;
  top: 0;
  left: 0;
  width: 30%;
  height: 100%;
  padding: 30px 30px 0 30px;
  overflow: auto;
}

button {
  min-width: 50px;
  width: 50px;
  height: 50px;
  border-radius: 100%;
  position: fixed;
  bottom: 0;
  left: 25%;
}
</style>