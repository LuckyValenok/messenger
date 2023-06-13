<template>
  <div class="message">
    <div>
      <div>
        <p style="color: #411467">{{ message.user.name }} (@{{ message.user.login }})</p>
        <p>{{ message.text }}</p>
        <p>{{ convertDateTimeFull(message.created_date) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import {convertDateTimeFull} from "@/utils";

export default {
  name: "ChatMessage",
  props: ['message'],
  methods: {
    convertDateTimeFull
  }
}
</script>

<style lang="less" scoped>
.message {
  background: rgba(214, 199, 225, 0.55);
  border-radius: 10px;
  padding: 10px;
  min-width: 100px;
  width: auto;
  max-width: 600px;

  margin-top: 25px;
}

p {
  color: black;
}
</style>