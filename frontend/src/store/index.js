import { createStore } from "vuex";
import createPersistedState from "vuex-plugin-persistedstate";

import users from './modules/users';

export default createStore({
  modules: {
    users,
  },
  plugins: [createPersistedState()]
});