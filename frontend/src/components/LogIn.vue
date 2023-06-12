<script setup>
import '../assets/styles/auth.less';
</script>

<template>
  <div class="form-card">
    <h1>Log In</h1>
    <form @submit.prevent="submit">
      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon1"/>
        <input name="username" v-model="username" type="text" placeholder="username"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon2.png" alt="icon2"/>
        <input name="password" v-model="password" type="password" minlength="6" placeholder="password"/>
      </div>

      <button type="submit">Log In</button>
    </form>
    <h3>Don't have an account?
      <router-link :to="{ name: 'signup' }">Sign Up.</router-link>
    </h3>
  </div>
</template>

<script>
import {defineComponent} from 'vue';
import {mapActions} from 'vuex';

export default defineComponent({
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.username);
      User.append('password', this.password);
      await this.logIn(User);
      this.$router.push({name: 'messenger'});
    }
  }
});
</script>