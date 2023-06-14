<template>
  <div class="message" :class="{right: user.id === message.user.id}">
    <p style="color: #411467">{{ message.user.name }} (@{{ message.user.login }})</p>
    <p>{{ message.text }}</p>
    <p>{{ convertDateTimeFull(message.created_date) }}</p>
  </div>
</template>

<script>
import {convertDateTimeFull} from "@/utils";
import {mapGetters} from "vuex";

export default {
  name: "ChatMessage",
  props: ['message'],
  methods: {
    convertDateTimeFull
  },
  computed: {
    ...mapGetters({user: "user"})
  }
}
</script>

<style lang="less" scoped>
.message {
  background: #F3F3F7;
  border-radius: 10px;
  padding: 10px;
  min-width: 100px;
  width: auto;
  max-width: 600px;
  margin-top: 25px;
}

.message.right {
  margin-left: auto;
}

p {
  color: black;
}
</style>