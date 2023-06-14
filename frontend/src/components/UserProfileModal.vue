<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="flex-row" style="justify-content: flex-end">
        <button class="modal-close" type="submit" @click="closeModal">&#10006;</button>
      </div>
      <slot name="title">
        <h3 class="modal-title">Edit profile</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <form>
            <div class="form-field">
              <input name="name" v-model="newName" type="text" placeholder="your name"/>
            </div>
            <div class="flex-row" style="justify-content: flex-end; margin: 20px 5px 10px; ">
              <button type="submit" @click="changeNameSubmit">Change</button>
              <button class="btn-red" @click="deleteProfile">Delete Profile</button>
            </div>
          </form>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "UserProfileModal", data: function () {
    return {
      show: false,
      newName: '',
    }
  },
  computed: {
    ...mapGetters({user: "user"})
  },
  created() {
    this.newName = this.user.name;
  },
  methods: {
    ...mapActions(['changeName', 'deleteUser']),
    closeModal: function () {
      this.show = false
    },
    changeNameSubmit: async function () {
      this.closeModal();
      if (!this.newName.trim()) {
        return;
      }
      await this.changeName(this.newName);
      this.newName = this.user.name;
    },
    deleteProfile: async function () {
      await this.deleteUser();
      this.$router.push({name: 'login'})
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

.btn-red {
  background: #984343
}

.btn-red:hover {
  background: #a76262;
}

.btn-red:active {
  background: #ae3333;
}

button:hover {
  background: #aa94b7;
}

button:active {
  background: #6A557B;
}
</style>