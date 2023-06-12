<template>
  <form class="input-form">
    <input type="text" placeholder="Write a message..." class="input-write"/>
    <button type="submit">
      <span>Send</span>
      <img src="../assets/img/arrow.png" alt="Image">
    </button>
  </form>
</template>

<style lang="less" scoped>
.flex-row {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.input-form {
  .flex-row();
  gap: 10px;
}

input {
  background-color: #F3F3F7;
  height: 45px;
  padding-left: 20px;
  color: #B8B8C6;
  border-radius: 50px;
  border: none;
  font-size: larger;
  width: 70%;
}


button {
  .flex-row();
  min-width: 130px;
  height: 45px;
  background-color: #D6C7E1;
  border-radius: 50px;
  font-size: larger;
  margin: 0;
  padding: 0;
}

button:hover {
  background-color: #C0B2CB;
}

button:active {
  background-color: #6A557B;
}

a {
  color: #ffffff;
}
</style>
  