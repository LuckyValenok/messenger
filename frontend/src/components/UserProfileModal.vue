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
.modal-shadow {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 999999;
}

.modal {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  left: 10%;
  min-width: 420px;
  max-width: 480px;
  position: absolute;

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