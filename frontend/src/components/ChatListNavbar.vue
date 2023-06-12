<template>
  <div class="navbar">
    <a href="#" class="navbar-item">
      <img src="../assets/img/icon4.png" alt="profile-img" style="width: 30px; "/>
      <p v-if="user">{{ user.name }} (@{{ user.login }})</p>
    </a>
    <a href="#" class="navbar-item">
      <img src="../assets/img/logout.png" @click="logout" alt="profile-img" style="width: 25px;"/>
    </a>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: 'ChatListNabvar',
  computed: {
    ...mapGetters({user: "user"}),
  },
  methods: {
    ...mapActions(['logOut']),
    async logout() {
      await this.logOut()
      this.$router.push({name: 'login'})
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
}
</style>