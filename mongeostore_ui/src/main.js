/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-21 14:57:37
 */
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from "element-ui";
import VueResource from 'vue-resource';
import "element-ui/lib/theme-chalk/index.css";
import api from './http'
import global from '@/utils/global'
import 'font-awesome/css/font-awesome.min.css'
import i18n from './i18n'

// BootStrap
import "jquery";
// import $ from 'jquery';
// import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap/dist/js/bootstrap.min.js";

// BootStrap—Vue
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import SlideVerify from 'vue-monoplasty-slide-verify';
// Baidui API
import BaiduMap from 'vue-baidu-map';
import uploader from 'vue-simple-uploader';

// 滑动验证码
Vue.use(SlideVerify)

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(BaiduMap, {
  /* Visit http://lbsyun.baidu.com/apiconsole/key for details about app key. */
  ak: '23jFoXtASNYo6tR1hrrjuVWwM97FGKpH'
})
Vue.use(uploader)

// // 设置反向代理，前端请求默认发送到 http://localhost:8080/api
// var axios = require("axios");
// axios.defaults.baseURL = "http://localhost:8080/api";
// // 全局注册，之后可在其他组件中通过 this.$axios 发送数据
// Vue.prototype.$axios = axios;

Vue.config.productionTip = false;

Vue.use(ElementUI);
Vue.use(VueResource);
Vue.use(api)  // 引入API模块

Vue.prototype.global = global // 挂载全局配置模块

new Vue({
  i18n,
  router,
  store,
  // $,
  render: h => h(App)
}).$mount("#app");
