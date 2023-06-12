<template>
  <div class="chat-item">
    <a @click="select">
      <div class="chat-item-content">
        <div>
          <img src="../assets/img/icon3.png" alt="avatar">
        </div>
        <div class="chat-item-content--text">
          <p style="color: #411467;">{{ name }}</p>
          <p v-if="last_message">{{ last_message }}</p>
        </div>
        <div v-if="time_last_message">
          <p style="width: 70px;">{{ time_last_message }}</p>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
import axios from "axios";
import {mapActions} from "vuex";

export default {
  props: ['id', 'name'],
  data() {
    return {
      last_message: '',
      time_last_message: ''
    };
  },
  created: async function () {
    await axios.get('/message/last/' + this.id)
        .then(value => {
          let data = value.data;
          if (data) {
            this.last_message = data.text
            this.time_last_message = new Date(Date.parse(data.created_date)).toLocaleString()
          }
        });
  },
  methods: {
    ...mapActions(['selectChat']),
    async select() {
      await this.selectChat(this.id);
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
  background-color: #F3F3F7;
}

.chat-item:active {
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