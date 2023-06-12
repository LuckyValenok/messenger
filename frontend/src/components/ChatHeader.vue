<template>
  <div class="navbar">
    <p class="navbar-title">{{ chat.name }}</p>
    <hr>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ChatHeader",
  computed: {
    ...mapGetters({chat: "selectChat"}),
  }
}
</script>

<style lang="less" scoped>
.navbar {
  background: #ffffff;
}

.navbar-title {
  font-size: 20px;
}

p {
  color: black;
}
</style>