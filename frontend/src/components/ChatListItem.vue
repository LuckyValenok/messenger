<template>
  <div class="chat-item" :class="{active: chat.id === selectChatId}">
    <a @click="select">
      <div class="chat-item-content">
        <div>
          <img :src="getImgUrl(chat.type)" alt="avatar">
        </div>
        <div class="chat-item-content--text">
          <p style="color: #411467;">{{ chat.name }}</p>
          <p v-if="chat.message">{{ chat.message.text }}</p>
        </div>
        <div v-if="chat.message">
          <p style="width: 70px;">{{ time }}</p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import {convertDateTime} from "@/utils";

export default {
  props: ['chat'],
  data() {
    return {
      time: '',
    }
  },
  computed: {
    ...mapGetters({selectChatId: "selectChatId"}),
  },
  created() {
    this.getDate();
    setInterval(() => {
      this.getDate();
    }, 1000)
  },
  methods: {
    ...mapActions(['selectChat']),
    select() {
      this.selectChat(this.chat.id);
    },
    getImgUrl(pic) {
      return require('../assets/img/' + pic + '_chat_icon.png')
    },
    getDate() {
      if (this.chat.message) {
        this.time = convertDateTime(this.chat.message.created_date)
      }
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