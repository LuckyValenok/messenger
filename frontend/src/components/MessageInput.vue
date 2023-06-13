<template>
  <form @submit.prevent="submit" class="input-form">
    <input type="text" v-model="text" placeholder="Write a message..." class="input-write"/>
    <button type="submit">
      <span>Send</span>
      <img src="../assets/img/arrow.png" alt="Image">
    </button>
  </form>
</template>

<script>
import {mapActions} from "vuex";

export default {
  data() {
    return {
      text: '',
    };
  },
  methods: {
    ...mapActions(['sendMessage']),
    async submit() {
      this.text = this.text.trim();
      if (this.text) {
        await this.sendMessage(this.text);
        this.text = '';
      }
    }
  }
};
</script>

<style lang="less" scoped>
.flex-row {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.input-form {
  .flex-row();
  gap: 10px;
}

input {
  background-color: #F3F3F7;
  height: 45px;
  padding-left: 20px;
  color: #B8B8C6;
  border-radius: 50px;
  border: none;
  font-size: larger;
  width: 90%;
}


button {
  .flex-row();
  min-width: 130px;
  height: 45px;
  background-color: #c8b8cd;
  border-radius: 50px;
  font-size: larger;
  margin: 0;
  padding: 0;
}

button:hover {
  background-color: #aa94b7;
}

button:active {
  background-color: #6A557B;
}

a {
  color: #ffffff;
}
</style>
  