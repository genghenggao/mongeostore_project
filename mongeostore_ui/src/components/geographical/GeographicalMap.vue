<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2021-01-03 22:56:56
 * @LastEditors: henggao
 * @LastEditTime: 2021-01-06 15:45:04
-->
<template>
  <div class="viewer">
    <vc-viewer>
      <vc-layer-imagery></vc-layer-imagery>
    </vc-viewer>
  </div>
</template>

<script>
import Vue from "vue";
import VueCesium from "vue-cesium";
// VueCesium 默认使用 `https://unpkg.com/cesium/Build/Cesium/Cesium.js`
Vue.use(VueCesium, {
  // cesiumPath 是指引用的Cesium.js路径，如
  // 项目本地的Cesium Build包，vue项目需要将Cesium Build包放static目录：
  // cesiumPath: /static/Cesium/Cesium.js
  // 个人在线Cesium Build包：
  // cesiumPath: 'https://zouyaoji.top/vue-cesium/statics/Cesium/Cesium.js'
  // 个人在线SuperMap Cesium Build包（在官方基础上二次开发出来的）：
  // cesiumPath: 'https://zouyaoji.top/vue-cesium/statics/SuperMapCesium/Cesium.js'
  // 官方在线Cesium Build包，有CDN加速，推荐用这个：
  cesiumPath: "https://unpkg.com/cesium/Build/Cesium/Cesium.js",
  // 指定Cesium.Ion.defaultAccessToken，使用Cesium ion的数据源需要到https://cesium.com/ion/申请一个账户，获取Access Token。不指定的话可能导致 Cesium 在线影像加载不了
  accessToken:
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxZDE0MWI4OS1jYjYxLTRmMDEtYWI5Yy1hZjBiNDAwZjc2NzEiLCJpZCI6MTgzMDEsImlhdCI6MTYwOTMyNjMxNH0.5H4EA7TyeUBhRmOI6IoRFXjyLtEJAjFZKJORBhGK2uc",
});
export default {};
</script>

<style>
.viewer {
  width: 100%;
  height: 811px;
}
</style>