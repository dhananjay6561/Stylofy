import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Wardrobe from '../views/Wardrobe.vue'
import Outfits from '../views/Outfits.vue'
import Login from '../components/Auth/Login.vue'
import Register from '../components/Auth/Register.vue'

const routes = [
  {
    path: '/',
    name: '