import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/movieView.vue'
import MovieDetail from '../views/movieDetail.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Community from '@/views/Community'
import myPage from '@/views/accounts/myPage'
import communitydetail from '@/views/communityDetail.vue'
import myMvti from '@/views/myMvti'
import searchPage from '@/views/searchPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/movies/:id',
    name: 'detail',
    component: MovieDetail
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community',
    name: 'community',
    component: Community,
  },
  {
    path: '/accounts/mypage',
    name: 'mypage',
    component: myPage,
  },
  {
    path: '/communitydetail',
    name: 'communitydDetail',
    component: communitydetail,
  },
  {
    path: '/mymvti',
    name: 'myMvti',
    component: myMvti,
  },
  {
    path: '/search/:searchtext',
    name: 'searchPage',
    component: searchPage,
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
