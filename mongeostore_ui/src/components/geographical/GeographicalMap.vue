<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2021-01-03 22:56:56
 * @LastEditors: henggao
 * @LastEditTime: 2021-01-05 22:41:21
-->
<template>
  <div class="viewer">
    <vc-viewer @ready="ready">
      <vc-layer-imagery
        ref="layerText"
        :alpha="alpha"
        :brightness="brightness"
        :contrast="contrast"
        :sortOrder="20"
      >
        <vc-provider-imagery-tianditu
          mapStyle="cva_c"
          token="436ce7e50d27eede2f2929307e6b33c0"
        ></vc-provider-imagery-tianditu>
      </vc-layer-imagery>
      <vc-layer-imagery
        :alpha="alpha"
        :brightness="brightness"
        :contrast="contrast"
        :sortOrder="10"
      >
        <vc-provider-imagery-tianditu
          :mapStyle="mapStyle"
          token="436ce7e50d27eede2f2929307e6b33c0"
        ></vc-provider-imagery-tianditu>
      </vc-layer-imagery>
    </vc-viewer>
    <div class="demo-tool">
      <span>透明度</span>
      <vue-slider
        v-model="alpha"
        :min="0"
        :max="1"
        :interval="0.01"
      ></vue-slider>
      <span>亮度</span>
      <vue-slider
        v-model="brightness"
        :min="0"
        :max="3"
        :interval="0.01"
      ></vue-slider>
      <span>对比度</span>
      <vue-slider
        v-model="contrast"
        :min="0"
        :max="3"
        :interval="0.01"
      ></vue-slider>
      <span>切换服务</span>
      <md-select v-model="mapStyle" placeholder="请选择地图服务类型">
        <md-option
          v-for="item in options"
          :key="item.value"
          :value="item.value"
        >
          {{ item.label }}
        </md-option>
      </md-select>
    </div>
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
export default {
  data() {
    return {
      protocol: "http",
      options: [
        {
          value: "img_c",
          label: "全球影像地图服务(经纬度)",
        },
        {
          value: "img_w",
          label: "全球影像地图服务(墨卡托)",
        },
        {
          value: "vec_c",
          label: "全球矢量地图服务(经纬度)",
        },
        {
          value: "vec_w",
          label: "全球矢量地图服务(墨卡托)",
        },
        {
          value: "ter_c",
          label: "全球地形晕渲服务(经纬度)",
        },
        {
          value: "ter_w",
          label: "全球地形晕渲服务(墨卡托)",
        },
      ],
      mapStyle: "img_c",
      alpha: 1,
      brightness: 1,
      contrast: 1,
    };
  },
  methods: {
    ready({ Cesium, viewer }) {
      this.Cesium = Cesium;
      this.viewer = viewer;
    },
  },
};
</script>

<style>
.viewer {
  width: 100%;
  height: 811px;
}
</style>