<script setup>
import '../assets/styles/auth.less';
</script>

<template>
  <div class="form-card">
    <h1>Log In</h1>
    <form method="post">
      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon1"/>
        <input name="username" type="text" placeholder="username"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon2.png" alt="icon2"/>
        <input name="password" type="password" minlength="6" placeholder="password"/>
      </div>

      <button type="submit">Log In</button>
    </form>
    <h3>Don't have an account?
      <router-link :to="{ name: 'signup' }">Sign Up.</router-link>
    </h3>
  </div>
</template>