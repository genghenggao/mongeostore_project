<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-06 17:05:32
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-06 21:55:31
-->
<template>
  <div>
    <!-- <el-card class="card-back-color card1"> -->
    <!-- <div class="baidu-title">
        <h4>百度地图API</h4>
      </div> -->
    <baidu-map :center="center" :zoom="zoom" @ready="handler" class="map">
      <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
      <bm-map-type
        :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']"
        anchor="BMAP_ANCHOR_TOP_LEFT"
      ></bm-map-type>
      <bm-geolocation
        anchor="BMAP_ANCHOR_BOTTOM_RIGHT"
        :showAddressBar="true"
        :autoLocation="true"
      ></bm-geolocation>
    </baidu-map>
    <!-- </el-card> -->
  </div>
</template>

<script>
export default {
  name: "MapView",
  data() {
    return {
      center: { lng: 0, lat: 0 },
      zoom: 3
    };
  },

  mounted() {
    // this.addPoints();
  },
  methods: {
    handler({ BMap, map }) {
      map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
      console.log(BMap, map);
      this.center.lng = 121.62;
      this.center.lat = 38.92;
      this.zoom = 11.5;
    }
  }
};
</script>

<style>
/* The container of BaiduMap must be set width & height. */
.map {
  width: 100%;
  height: 750px;
}
</style>
