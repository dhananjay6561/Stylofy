import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
    wardrobeItems: [],
    loading: false,       // Add a loading state
    error: null           // Add an error state to handle errors
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setToken(state, token) {
      state.token = token
      localStorage.setItem('token', token)
    },
    clearUserData(state) {
      state.user = null
      state.token = null
      state.wardrobeItems = []      // Clear wardrobe items on logout
      localStorage.removeItem('token')
    },
    setWardrobeItems(state, items) {
      state.wardrobeItems = items
    },
    setLoading(state, isLoading) {
      state.loading = isLoading
    },
    setError(state, error) {
      state.error = error
    }
  },
  actions: {
    // Login action
    async login({ commit, dispatch }, credentials) {
      commit('setLoading', true)   // Start loading
      commit('setError', null)     // Clear previous errors
      try {
        const response = await axios.post('http://localhost:8000/token', credentials)
        commit('setToken', response.data.access_token)
        await dispatch('fetchUser')
      } catch (error) {
        commit('setError', 'Failed to login. Please check your credentials.')
        console.error(error)
      } finally {
        commit('setLoading', false)  // Stop loading
      }
    },
    
    // Register action
    async register({ dispatch, commit }, userData) {
      commit('setLoading', true)
      commit('setError', null)
      try {
        await axios.post('http://localhost:8000/register', userData)
        await dispatch('login', { username: userData.username, password: userData.password })
      } catch (error) {
        commit('setError', 'Registration failed. Please try again.')
        console.error(error)
      } finally {
        commit('setLoading', false)
      }
    },

    // Fetch user data
    async fetchUser({ commit, state }) {
      commit('setLoading', true)
      commit('setError', null)
      try {
        const response = await axios.get('http://localhost:8000/users/me', {
          headers: { Authorization: `Bearer ${state.token}` }
        })
        commit('setUser', response.data)
      } catch (error) {
        commit('setError', 'Failed to fetch user data.')
        console.error(error)
      } finally {
        commit('setLoading', false)
      }
    },

    // Fetch wardrobe items
    async fetchWardrobeItems({ commit, state }) {
      commit('setLoading', true)
      commit('setError', null)
      try {
        const response = await axios.get('http://localhost:8000/wardrobe/items', {
          headers: { Authorization: `Bearer ${state.token}` }
        })
        commit('setWardrobeItems', response.data)
      } catch (error) {
        commit('setError', 'Failed to fetch wardrobe items.')
        console.error(error)
      } finally {
        commit('setLoading', false)
      }
    },

    // Logout action
    logout({ commit }) {
      commit('clearUserData')
    }
  },
  getters: {
    isAuthenticated: state => !!state.token,
    getError: state => state.error,          // New getter to retrieve the error state
    isLoading: state => state.loading        // Getter for loading state
  }
})
