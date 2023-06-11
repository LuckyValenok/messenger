<script setup>
import './signup.less';
</script>

<template>
  <div class="form-card">
    <h1>Sign Up</h1>
    <form method="post">
      <div class="form-field">
        <img src="../../assets/img/icon1.png" alt="icon1"/>
        <input name="username" type="text" placeholder="username"/>
      </div>

      <div class="form-field">
        <img src="../../assets/img/icon2.png" alt="icon2"/>
        <input name="password" type="password" minlength="6" placeholder="password"/>
      </div>

      <div class="form-field">
        <img src="../../assets/img/icon1.png" alt="icon3"/>
        <input name="name" type="text" placeholder="your name"/>
      </div>

      <button type="submit">Sign Up</button>
    </form>
    <h3>Already have an account? <a href="#">Log In.</a></h3>
  </div>
</template>

<script>
export default {
  name: "SignUp"
}
</script>

<style>

</style>