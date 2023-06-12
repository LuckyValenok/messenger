<template>
  <div>
    <div>
      <ul>
        <li class="chat-item">
          <a href="#!">
            <div class="chat-item-content">
              <div>
                <img src="../assets/img/icon3.png" alt="avatar">
              </div>
              <div class="chat-item-content--text">
                <p style="color: #411467;">Marie Horwitz</p>
                <p>Hello, Are you there? ertyey s tyhtsr truh ftuj f ag </p>
              </div>
              <div>
                <p style="width: 70px;">Just now</p>
              </div>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style lang="less" scoped>
.chat-item {
  margin-top: 50px;
  list-style-type: none;

}

a {
  text-decoration: none;
}

.flex-row {
  display: flex;
  flex-direction: row;
}

.chat-item-content {
  .flex-row();
  margin-right: 10px
}

.chat-item-content--text {
  justify-content: space-between;
  margin: 0 20px 0 15px;
}

img {
  margin-right: 30px;
}

ul {
  padding: 0;
}
</style>