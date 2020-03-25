import Vue from 'vue'
import App from './App.vue'
import JQuery from 'jquery'
import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'
import './assets/css/app.css'

Vue.config.productionTip = false
window.JQuery = JQuery

  new Vue({
    render: function(createElement){
      return createElement(App);
    }
  }).$mount('#app')
