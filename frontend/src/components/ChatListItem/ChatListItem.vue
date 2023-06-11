<script setup>
import './chat-list-item.less';
</script>


<template>


  <div>
    <div >
      <ul>
        <li class="chat-item" >
          <a href="#!">
            <div class="chat-item-content">
              <div>
                <img src="../../assets/img/icon3.png" alt="avatar">
              </div>
              <div class="chat-item-content--text">
                <p style="color: #411467;">Marie Horwitz</p>
                <p>Hello, Are you there? ertyey  s tyhtsr truh ftuj f ag </p>
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

<script>
export default {
  name: "ChatListItem"
}
</script>

<style scoped>

</style>