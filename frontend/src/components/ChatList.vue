<template>
  <header>
  </header>

  <main>
    <ChatNavbar/>
    <ChatSearch/>
    <ChatListItem/>
  </main>
</template>

<script>
import ChatListItem from "@/components/ChatListItem.vue";
import ChatSearch from "@/components/ChatSearch.vue";
import ChatNavbar from "@/components/ChatListNavbar.vue";

export default {
  name: "ChatList",
  components: {ChatSearch, ChatListItem, ChatNavbar}
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
</style>