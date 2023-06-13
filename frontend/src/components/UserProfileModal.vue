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
              <input name="name" type="text" placeholder="your name"/>
            </div>
            <div class="flex-row" style="justify-content: flex-end; margin: 20px 5px 10px; ">
              <button type="submit" @click="closeModal">Change</button>
              <button type="submit" style="background: #984343">Delete Profile</button>
            </div>

          </form>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>

export default {
  name: "UserProfileModal", data: function () {
    return {
      show: false,
    }
  },
  methods: {
    closeModal: function () {
      this.show = false
    }
  }
}
</script>

<style scoped lang="less">
input{
  background: #e2d8e5;
  border-color: #9f9f9f;
}

input::placeholder, h3 {
  color: #9f9f9f;
}

.modal {
  background: #e2d8e5;
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
</style>