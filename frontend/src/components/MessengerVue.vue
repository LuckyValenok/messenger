<template>
  <header>
  </header>

  <main>
    <MessageChat v-if="chat"/>
    <ChatList v-if="user"/>

  </main>
</template>

<script>
import ChatList from "@/components/ChatList.vue";
import MessageChat from "@/components/MessageChat.vue";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "MessengerVue",
  components: {MessageChat, ChatList},
  computed: {
    ...mapGetters({user: "user", chat: "selectChatId", accessToken: "accessToken"}),
  },
  created: async function () {
    if (!this.user && this.accessToken) {
      await this.viewMe()
      await this.selectChat(this.chat)
    }
  },
  methods: {
    ...mapActions(['viewMe', 'selectChat'])
  }
}
</script>