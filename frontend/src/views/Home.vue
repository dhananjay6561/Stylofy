<template>
  <div class="home">
    <h1>Welcome to Virtual Stylist</h1>
    <p v-if="isAuthenticated">Hello, {{ user.username }}!</p>
    <p v-else>Please log in or register to get started.</p>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  setup() {
    const store = useStore()
    const isAuthenticated = computed(() => store.getters.isAuthenticated)
    const user = computed(() => store.state.user)

    return {
      isAuthenticated,
      user
    }
  }
}
</script>