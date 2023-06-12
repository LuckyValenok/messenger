<template>
  <header>
  </header>

  <main>
    <ChatList v-if="user"/>
    <MessageChat v-if="chat"/>
  </main>
</template>

<script>
import ChatList from "@/components/ChatList.vue";
import MessageChat from "@/components/MessageChat.vue";
import {mapGetters} from "vuex";

export default {
  name: "MessengerVue",
  components: {MessageChat, ChatList},
  computed: {
    ...mapGetters({user: "user", chat: "selectChat"}),
  }
}
</script>