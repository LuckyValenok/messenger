<template>
  <main v-if="chat">
    <section>
      <div v-if="chat.messages">
        <div v-for="message in chat.messages" :key="message.id">
          <ChatMessage v-bind:message="message"/>
        </div>
      </div>
    </section>
    <header>
      <ChatHeader/>
    </header>
    <footer>
      <MessageInput/>
    </footer>
  </main>
</template>

<script>
import ChatMessage from "@/components/ChatMessage.vue";
import ChatHeader from "@/components/ChatHeader.vue";
import MessageInput from "@/components/MessageInput.vue";
import {mapGetters} from "vuex";

export default {
  name: "MessageChat",
  components: {ChatMessage, ChatHeader, MessageInput},
  computed: {
    ...mapGetters({chat: "selectChat", token: "accessToken", chatId: "selectChatId"}),
  },
  data() {
    return {
      connection: null,
    }
  },
  created: function () {
    if (!this.chatId) {
      return;
    }
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("ws://localhost:8000/ws/chat/" + this.chatId + "?token=" + this.token)

    this.connection.onmessage = event => {
      let data = JSON.parse(event.data);
      this.chat.messages.push(data);
    }
  }
}
</script>

<style lang="less" scoped>
.flex-column-reverse {
  display: flex;
  flex-direction: column-reverse;
}

.flex-column {
  display: flex;
  flex-direction: column;
}

.default {
  top: 0;
  right: 0;
  width: 70%;
  padding: 30px;
  position: fixed;
  background: #ffffff;
}

header {
  .flex-column();
  .default();
  height: 10%;
}


section {
  .flex-column-reverse();
  .default();
  height: 100%;
  padding-bottom: 120px;
  padding-top: 70px;
  overflow: auto;
}

footer {
  .flex-column-reverse();
  .default();
  bottom: 0;
  top: auto;
  position: fixed;
  height: 10%;
}
</style>