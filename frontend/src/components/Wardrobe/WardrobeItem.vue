<template>
  <div class="wardrobe-item">
    <img :src="item.image_url" :alt="item.category">
    <p>{{ item.category }}</p>
  </div>
</template>

<script>
export default {
  props: ['item']
}
</script>

<style scoped>
.wardrobe-item {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.wardrobe-item img {
  max-width: 100%;
  height: auto;
}
</style>