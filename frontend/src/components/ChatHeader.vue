<template>
  <div class="navbar">
    <p class="navbar-title">{{ capitalize(chat.type) }} chat «{{ chat.name }}»</p>
    <hr>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import {capitalize} from "@/utils";

export default {
  name: "ChatHeader",
  computed: {
    ...mapGetters({chat: "selectChat"}),
  },
  methods: {
    capitalize
  }
}
</script>

<style lang="less" scoped>

.navbar-title {
  font-size: 20px;
}

p {
  color: black;
}
</style>