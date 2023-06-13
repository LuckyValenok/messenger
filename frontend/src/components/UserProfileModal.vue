<template>
<div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="modal-title">Edit profile</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <form>
            <div class="form-field">
              <input name="name" type="text" placeholder="your name"/>
            </div>

            <div class="form-field">
            </div>
            <button type="submit" @click="closeModal">Change</button>
            <button type="submit" style="margin-bottom: 10px; background: #984343">Delete Profile</button>
          </form>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>

export default {
  name: "UserProfileModal",  data: function () {
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

button{
  margin: 5px;
}
</style>