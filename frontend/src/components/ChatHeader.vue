<template>
  <div class="navbar">
    <p class="navbar-title">{{ capitalize(chat.type) }} chat «{{ chat.name }}»</p>
    <div class="page">
      <button type="submit" @click="showModal">Add members</button>
      <NewMembersModal ref="modal"></NewMembersModal>
    </div>
  </div>
  <hr>


</template>

<script>
import {mapGetters} from "vuex";
import {capitalize} from "@/utils";
import NewMembersModal from "@/components/NewMembersModal.vue";

export default {
  name: "ChatHeader",
  components: {NewMembersModal},
  computed: {
    ...mapGetters({chat: "selectChat"}),
  },
  methods: {
    capitalize,
    showModal: function () {
      this.$refs.modal.show = true
    },
  }
}
</script>

<style lang="less" scoped>
.navbar{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.navbar-title {
  font-size: 20px;
}

p {
  color: black;
}

button{
  margin: 0;
  padding: 0;
  min-width: 150px;
  width: 150px;
  height: 40px;
  font-size: 15px;
  background: transparent;
  color: black;
}
</style>