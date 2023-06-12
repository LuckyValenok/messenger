<template>
  <header>
  </header>

  <main>
    <ChatList/>
    <MessageChat/>
  </main>
</template>

<script>
import ChatList from "@/components/ChatList.vue";
import MessageChat from "@/components/MessageChat.vue";

export default {
  name: "MessengerVue",
  components: {MessageChat, ChatList}
}
</script>