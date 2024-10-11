<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const store = useStore()
    const router = useRouter()
    const username = ref('')
    const password = ref('')

    const login = async () => {
      try {
        await store.dispatch('login', { username: username.value, password: password.value })
        router.push('/')
      } catch (error) {
        console.error('Login failed', error)
        // Here you might want to show an error message to the user
      }
    }

    return {
      username,
      password,
      login
    }
  }
}
</script>