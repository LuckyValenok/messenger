<template>
  <div>
    <input type="search" @input="event => onChange(event.target.value)" placeholder="Search" aria-label="Search">
  </div>
</template>

<script>
import {mapMutations} from "vuex";

export default {
  methods: {
    ...mapMutations(['setFilter']),
    onChange(search) {
      this.setFilter(search);
    }
  }
}
</script>

<style lang="less" scoped>
input {
  border-radius: 20px;
  padding: 10px 20px;
  top: 0;
  left: 0;
  width: 100%;
  margin-top: 30px;
}
</style>