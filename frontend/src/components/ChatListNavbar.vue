<template>
  <div class="navbar">
    <a href="#" class="navbar-item" @click="showModal">
      <img src="../assets/img/profile.png" alt="profile-img" style="width: 30px; "/>
      <p v-if="user">{{ user.name }} (@{{ user.login }})</p>
    </a>
    <a href="#" class="navbar-item">
      <img src="../assets/img/logout.png" @click="logout" alt="profile-img" style="width: 25px;"/>
    </a>
    <UserProfileModal ref="modal"></UserProfileModal>

  </div>
</template>

<script>
import UserProfileModal from "@/components/UserProfileModal.vue";
import {mapActions, mapGetters} from "vuex";

export default {
  name: 'ChatListNavbar',
  components: {UserProfileModal},
  computed: {
    ...mapGetters({user: "user"}),
  },
  methods: {
    ...mapActions(['logOut', 'clearMessages', 'clearAccessToken']),
    logout() {
      this.logOut();
      this.clearMessages();
      this.clearAccessToken();
      this.$router.push({name: 'login'});
    },
    showModal: function () {
      this.$refs.modal.show = true
    }

  }
}
</script>

<style lang="less" scoped>
.flex-row {
  display: flex;
  flex-direction: row;
}

.navbar {
  .flex-row();
  justify-content: space-between;
  margin: 0 5px;
}

.navbar-item {
  .flex-row();
  align-items: center;
}

img {
  margin-right: 10px
}

p {
  color: #33363F
}

a {
  text-decoration: none;
  cursor: pointer;
}


</style>