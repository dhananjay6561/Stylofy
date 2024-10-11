<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Register</button>
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
    const email = ref('')
    const password = ref('')

    const register = async () => {
      try {
        await store.dispatch('register', { 
          username: username.value, 
          email: email.value, 
          password: password.value 
        })
        router.push('/')
      } catch (error) {
        console.error('Registration failed', error)
        // Here you might want to show an error message to the user
      }
    }

    return {
      username,
      email,
      password,
      register
    }
  }
}
</script>