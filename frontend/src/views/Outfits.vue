<template>
  <div class="outfits">
    <h1>Outfit Recommendations</h1>
    <button @click="getRecommendation">Get New Recommendation</button>
    <div v-if="recommendedOutfit" class="outfit">
      <h2>Recommended Outfit</h2>
      <div v-for="(item, category) in recommendedOutfit" :key="category">
        <h3>{{ category }}</h3>
        <WardrobeItem :item="item" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import WardrobeItem from '../components/Wardrobe/WardrobeItem.vue'
import axios from 'axios'

export default {
  components: {
    WardrobeItem
  },
  setup() {
    const store = useStore()
    const recommendedOutfit = ref(null)

    const getRecommendation = async () => {
      try {
        const response = await axios.post('http://localhost:8001/recommend', store.state.wardrobeItems, {
          headers: { Authorization: `Bearer ${store.state.token}` }
        })
        recommendedOutfit.value = response.data.recommended_outfit
      } catch (error) {
        console.error('Failed to get recommendation', error)
      }
    }

    return {
      recommendedOutfit,
      getRecommendation
    }
  }
}
</script>