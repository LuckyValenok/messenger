<template>
  <header>
  </header>

  <main>
    <ChatNavbar/>
    <ChatSearch/>
    <div v-if="chats">
      <div v-for="chat in chats" :key="chat.id" class="chats">
        <ChatListItem v-bind:id="chat.id" v-bind:name="chat.name"/>
      </div>
    </div>

    <button type="submit">+</button>
  </main>
</template>

<script>
import ChatListItem from "@/components/ChatListItem.vue";
import ChatSearch from "@/components/ChatSearch.vue";
import ChatNavbar from "@/components/ChatListNavbar.vue";
import {mapGetters} from "vuex";

export default {
  name: "ChatList",
  components: {ChatSearch, ChatListItem, ChatNavbar},
  created: function () {
    return this.$store.dispatch('getChats');
  },
  computed: {
    ...mapGetters({chats: 'chats'}),
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

button{
  min-width: 50px;
  width: 50px;
  height: 50px;
  border-radius: 100%;
  position: fixed;
  bottom: 0;
  left: 25%;
}
</style>