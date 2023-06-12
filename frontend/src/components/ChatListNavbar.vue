<template>
  <div class="navbar">
    <a href="#" class="navbar-item">
      <img src="../assets/img/icon4.png" alt="profile-img" style="width: 30px; "/>
      <p>username</p>
    </a>
    <a href="#" class="navbar-item">
      <img src="../assets/img/logout.png" alt="profile-img" style="width: 25px;"/>
    </a>
  </div>
</template>

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

a{
  text-decoration: none;
}
</style>