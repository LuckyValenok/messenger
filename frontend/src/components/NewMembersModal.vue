<template>
  <div v-if="show" @click.self="closeModal">
    <div class="modal">
      <div class="flex-row" style="justify-content: flex-end">
        <button class="modal-close" type="submit" @click="closeModal">&#10006;</button>
      </div>
      <slot name="title">
        <h3 class="modal-title">Add new member</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <form>
            <div class="form-field">
              <input name="name" v-model="name" type="text" placeholder="username"/>
            </div>
            <button type="submit" @click="submit" style="margin: 20px 5px 10px;">Add</button>
          </form>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "NewMembersModal", data: function () {
    return {
      show: false,
      name: '',
    }
  },
  methods: {
    ...mapActions(["addMember"]),
    closeModal: function () {
      this.show = false
    },
    submit: async function () {
      this.closeModal();
      if (!this.name.trim()) {
        return;
      }
      this.addMember(this.name);
      this.name = '';
    }
  }
}
</script>

<style scoped lang="less">
input {
  background: #e7dfe9;
  border-color: #9f9f9f;
}

input::placeholder, h3 {
  color: #9f9f9f;
}

.modal {
  background: #e7dfe9;
  border-radius: 8px;
  padding: 15px;
  position: fixed;
  bottom: 50%;
  left: 50%;
  margin: 30px;
  min-width: 420px;
  max-width: 480px;
  z-index: 999999;

  &-close {
    width: 30px;
    height: 30px;
    min-width: 30px;
  }

  &-title {
    color: #6A557B;
  }
}

button {
  margin: 5px;
}

button:hover {
  background: #aa94b7;
}

button:active {
  background: #6A557B;
}
</style>