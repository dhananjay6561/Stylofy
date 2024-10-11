<template>
  <div class="wardrobe-list">
    <h2>My Wardrobe</h2>
    <div class="items-container">
      <WardrobeItem v-for="item in items" :key="item.id" :item="item" />
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import WardrobeItem from './WardrobeItem.vue'

export default {
  components: {
    WardrobeItem
  },
  setup() {
    const store = useStore()
    const items = computed(() => store.state.wardrobeItems)

    return {
      items
    }
  }
}
</script>

<style scoped>
.items-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>