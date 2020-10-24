import Vue from 'vue'
import Router from 'vue-router'
import profile from '../components/Profile.vue'


const routes = [
  {
    path: '/view', 
    components: 
    { 
      profile: profile
    }
  }
]

//For every router option import router component file and return router option array
// const routes = routerOptions.map(route => {
//   return {
//     ...route,
//     component: () => import(`@/components/${route.component}.vue`)
//   }
// })

Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})