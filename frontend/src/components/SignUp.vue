<script setup>
import '../assets/styles/auth.less';
</script>

<template>
  <div class="form-card">
    <h1>Sign Up</h1>
    <form method="post">
      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon3"/>
        <input name="name" type="text" placeholder="your name"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon1"/>
        <input name="username" type="text" placeholder="username"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon2.png" alt="icon2"/>
        <input name="password" type="password" minlength="6" placeholder="password"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon2.png" alt="icon2"/>
        <input name="password2" type="password" minlength="6" placeholder="password (again)"/>
      </div>

      <button type="submit">Sign Up</button>
    </form>
    <h3>Already have an account?
      <router-link :to="{ name: 'login' }">Log In.</router-link>
    </h3>
  </div>
</template>