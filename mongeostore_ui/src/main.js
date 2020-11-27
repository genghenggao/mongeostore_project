/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-27 10:11:03
 */
import Vue from "vue";
import Vuex from 'vuex'  // 引入 vuex
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
// v-viewer 图片插件
import 'viewerjs/dist/viewer.css'
import Viewer from 'v-viewer'


Vue.use(Vuex) // 引入
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

Vue.use(Viewer)
Viewer.setDefaults({
  Options: { // Options必须，否则会出现默认打开等等不可预知的错误
    'inline': true,
    'button': true, // 显示右上角关闭按钮
    'navbar': true, // 缩略图导航
    'title': true, // 是否显示当前图片的标题
    'toolbar': true, // 显示工具栏
    'tooltip': true, // 显示缩放百分比
    'movable': true, // 图片是否可移动
    'zoomable': true, // 是否可缩放
    'rotatable': true, // 是否可旋转
    'scalable': true, // 是否可翻转
    'transition': true, // 是否使用 CSS3 过度
    'fullscreen': true, // 播放时是否全屏
    'keyboard': true, // 是否支持键盘
    'url': 'data-source' // 设置大图片的 url
  }
})

Vue.prototype.global = global // 挂载全局配置模块

new Vue({
  i18n,
  router,
  store,
  // $,
  render: h => h(App)
}).$mount("#app");
