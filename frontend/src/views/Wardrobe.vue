<template>
  <div class="wardrobe">
    <h1>My Wardrobe</h1>
    <WardrobeList />
    <button @click="showUploadForm = true">Add New Item</button>
    <div v-if="showUploadForm" class="upload-form">
      <h3>Upload New Item</h3>
      <form @submit.prevent="uploadItem">
        <input type="file" @change="onFileSelected" accept="image/*" required>
        <input v-model="category" placeholder="Category" required>
        <button type="submit">Upload</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import WardrobeList from '../components/Wardrobe/WardrobeList.vue'
import axios from 'axios'

export default {
  components: {
    WardrobeList
  },
  setup() {
    const store = useStore()
    const showUploadForm = ref(false)
    const selectedFile = ref(null)
    const category = ref('')

    const onFileSelected = (event) => {
      selectedFile.value = event.target.files[0]
    }

    const uploadItem = async () => {
      const formData = new FormData()
      formData.append('file', selectedFile.value)
      
      try {
        const response = await axios.post('http://localhost:8000/wardrobe/upload', formData, {
          headers: { 
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${store.state.token}`
          }
        })
        
        await store.dispatch('fetchWardrobeItems')
        showUploadForm.value = false
        category.value = ''
        selectedFile.value = null
      } catch (error) {
        console.error('Upload failed', error)
      }
    }

    return {
      showUploadForm,
      category,
      onFileSelected,
      uploadItem
    }
  }
}
</script>