<template>
  <div class="chat-item" :class="{active: chat.id === selectChatId}">
    <a @click="select">
      <div class="chat-item-content">
        <div class="flex-row">
          <div>
            <img :src="getImgUrl(chat.type)" alt="avatar">
          </div>
          <div class="chat-item-content--text">
            <p style="color: #411467;">{{ chat.name }}</p>
            <p v-if="chat.message">{{ chat.message.text }}</p>
          </div>
        </div>
        <div v-if="chat.message">
          <p style="width: 120px;">{{ convertDateTime(chat.message.created_date) }}</p>
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
    },
    getImgUrl(pic) {
      return require('../assets/img/' + pic + '_chat_icon.png')
    }
  }
}
</script>

<style lang="less" scoped>
.chat-item {
  margin-top: 10px;
  list-style-type: none;
  padding: 10px
}

.chat-item:hover {
  background-color: #FFFFFF;
  border-radius: 10px;
}

.chat-item.active {
  background-color: #ffffff;
  border-radius: 10px;
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
  margin-right: 10px;
  justify-content: space-between;
}

.chat-item-content--text {
  margin: 0 20px 0 15px;
}

img {
  margin-right: 30px;
}

ul {
  padding: 0;
}
</style>