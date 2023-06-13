<template>
  <div v-if="show" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="modal-title">New Group Chat</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <form>
            <div class="form-field">
              <input name="name" v-model="name" type="text" placeholder="chat name"/>
            </div>

            <div class="form-field">
              <select id="type" v-model="chatType" name="type">
                <option value="private">private</option>
                <option value="public">public</option>
              </select>
            </div>
            <button type="submit" @click="submit">Create</button>
          </form>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "NewChatModal",
  data: function () {
    return {
      show: false,
      name: '',
      chatType: 'private',
    }
  },
  methods: {
    ...mapActions(['createChat']),
    closeModal: function () {
      this.show = false;
    },
    submit: async function () {
      this.closeModal();
      if (!this.name) {
        return;
      }
      await this.createChat({
        name: this.name,
        chat_type: this.chatType
      });
    }
  }
}
</script>

<style scoped lang="less">
.modal {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  left: 10%;
  min-width: 420px;
  max-width: 480px;
  position: absolute;

  &-close {
    border-radius: 50%;
    color: #fff;
    background: #6A557B;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 7px;
    right: 7px;
    width: 30px;
    height: 30px;
    cursor: pointer;
  }

  &-title {
    color: #6A557B;
  }
}

select {
  border-style: solid;
  border-width: 0 0 1px;
  border-color: #FFFFFF;
  outline: none;
  font-size: 20px;
  background: #FFFFFF;
  font-family: 'Fahkwang', sans-serif;
  transition: all 200ms ease;
}
</style>