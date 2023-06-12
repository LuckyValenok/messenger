<script setup>
import '../assets/styles/auth.less';
</script>

<template>
  <div class="form-card">
    <h1>Sign Up</h1>
    <form @submit.prevent="submit">
      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon3"/>
        <input name="name" v-model="user.name" type="text" placeholder="your name"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon1.png" alt="icon1"/>
        <input name="username" v-model="user.login" type="text" placeholder="username"/>
      </div>

      <div class="form-field">
        <img src="../assets/img/icon2.png" alt="icon2"/>
        <input name="password" v-model="user.password" type="password" minlength="6" placeholder="password"/>
      </div>

      <button type="submit">Sign Up</button>
    </form>
    <h3>Already have an account?
      <router-link :to="{ name: 'login' }">Log In.</router-link>
    </h3>
  </div>
</template>

<script>
import {defineComponent} from 'vue';
import {mapActions} from 'vuex';

export default defineComponent({
  name: 'SignUp',
  data() {
    return {
      user: {
        name: '',
        login: '',
        password: '',
      },
    };
  },
  methods: {
    ...mapActions(['signUp']),
    async submit() {
      try {
        await this.signUp(this.user);
        this.$router.push({name: 'messenger'});
      } catch (e) {
        throw 'Username already exists. Please try again.';
      }
    }
  }
});
</script>