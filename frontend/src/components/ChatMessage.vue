<template>
  <div class="message">
    <div>
      <div>
        <p style="color: #411467">Alice (@alice56)</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore </p>
        <p>12:00 PM | Aug 13</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChatMessage"
}
</script>

<style lang="less" scoped>
.message {
  background: rgba(214, 199, 225, 0.55);
  border-radius: 10px;
  padding: 10px;
  min-width: 100px;
  width: auto;
  max-width: 600px;

  margin-top: 25px;
}

p {
  color: black;
}
</style>