<script setup>
import './chat-list.less';
</script>

<template>
  <header>
  </header>

  <main>
    <ChatNavbar/>
    <ChatSearch/>
    <ChatListItem />

  </main>
</template>

<script>
import ChatListItem from "@/components/ChatListItem/ChatListItem.vue";
import ChatSearch from "@/components/ChatSearch/ChatSearch.vue";
import ChatNavbar from "@/components/ChatNavbar/ChatNavbar.vue";

export default {
  name: "ChatList",
  components: {ChatSearch, ChatListItem, ChatNavbar}
}
</script>

<style scoped>

</style>