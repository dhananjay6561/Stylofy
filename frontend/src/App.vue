<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/wardrobe">Wardrobe</router-link> |
      <router-link to="/outfits">Outfits</router-link> |
      <template v-if="isAuthenticated">
        <a href="#" @click.prevent="logout">Logout</a>
      </template>
      <template v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link>
      </template>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const store = useStore()
    const router = useRouter()
    const isAuthenticated = computed(() => store.getters.isAuthenticated)

    const logout = () => {
      store.dispatch('logout')
      router.push('/login')
    }

    return {
      isAuthenticated,
      logout
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>