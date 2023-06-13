<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="modal-title">New Group Chat</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <form>
            <div class="form-field">
              <input name="name" type="text" placeholder="chat name"/>
            </div>

            <div class="form-field">
              <select id="type" name="type">
                <option value="private">private</option>
                <option value="public">public</option>
              </select>
            </div>
            <button type="submit" @click="closeModal">Create</button>
          </form>
        </div>
      </slot>
    </div>
  </div>

</template>

<script>
export default {
  name: "NewChatModal",
  data: function () {
    return {
      show: false
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
  min-height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.9);
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

select{
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