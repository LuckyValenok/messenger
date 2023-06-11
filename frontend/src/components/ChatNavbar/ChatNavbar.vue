<script setup>
import './chat-navbar.less';
</script>


<template>
  <div class="navbar">
    <div class="navbar-item">
      <img src="../../assets/img/icon4.png" alt="profile-img" style="width: 30px; "/>
      <p>username</p>
    </div>
    <div class="navbar-item">
      <img src="../../assets/img/logout.png" alt="profile-img" style="width: 25px;"/>
    </div>
  </div>

</template>

<script>
export default {
  name: "ChatNavbar"
}
</script>

<style scoped>

</style>