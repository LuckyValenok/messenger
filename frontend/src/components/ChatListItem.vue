<template>
  <div class="chat-item" :class="{active: chat.id === selectChatId}">
    <a @click="select">
      <div class="chat-item-content">
        <div>
          <img src="../assets/img/icon3.png" alt="avatar">
        </div>
        <div class="chat-item-content--text">
          <p style="color: #411467;">{{ chat.name }}</p>
          <p v-if="chat.message">{{ chat.message.text }}</p>
        </div>
        <div v-if="chat.message">
          <p style="width: 70px;">{{ convertDateTime(chat.message.created_date) }}</p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  props: ['chat'],
  computed: {
    ...mapGetters({selectChatId: "selectChatId"}),
  },
  methods: {
    ...mapActions(['selectChat']),
    select() {
      this.selectChat(this.chat.id);
    }
  }
}
</script>

<style lang="less" scoped>
.chat-item {
  margin-top: 50px;
  list-style-type: none;
}

.chat-item:hover {
  background-color: #FFFFFF;
}

.chat-item.active {
  background-color: #ffffff;
}

a {
  text-decoration: none;
}

.flex-row {
  display: flex;
  flex-direction: row;
}

.chat-item-content {
  .flex-row();
  margin-right: 10px
}

.chat-item-content--text {
  justify-content: space-between;
  margin: 0 20px 0 15px;
}

img {
  margin-right: 30px;
}

ul {
  padding: 0;
}
</style>