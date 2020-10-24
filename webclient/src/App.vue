<template>
  <div id="app">
    <b-list-group v-bind = "list_group_attr" class = "app-view">
      <router-view name = "profile"></router-view>
    </b-list-group>
  </div>
</template>

<script>
import Vue from 'vue'
import LoadScript from 'vue-plugin-load-script'

Vue.use(LoadScript)
export default {
  name: 'App',
  mounted(){
    Vue.loadScript('https://extension-files.twitch.tv/helper/v1/twitch-ext.min.js')
  },
  data(){
    return {
      list_group_attr:{
        flush: false,
        tag: 'div' 
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.app-view  {
  background-color: red;
}
</style>
