<template>
  <header>
  </header>

  <main>
    <ChatList/>
  </main>
</template>

<script>
import ChatList from "@/components/ChatList.vue";

export default {
  name: "MessengerVue",
  components: {ChatList}
}
</script>