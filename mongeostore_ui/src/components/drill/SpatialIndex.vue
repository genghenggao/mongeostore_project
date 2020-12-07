<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-06 09:36:35
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-07 17:50:45
-->
<template>
  <div>
    <!-- 使用组件 -->
    <TdtMap />
    <!-- <div id="mapDiv"></div> -->
  </div>
</template>



<script>
/* 导入组件 */
import TdtMap from "@/components/TdtMap";
import axios from "axios";

export default {
  name: "SpatialIndex",
  components: {
    /* 注册组件 */
    TdtMap,
  },
  data() {
    return {
      // data: testdata,
    };
  },
  created() {},
  mounted() {
    this.onLoad();
  },
  watch: {},
  methods: {
    onLoad() {
      var map;
      var zoom = 4;
      var lnglats;
      var _CloudCollection;
      // map = new T.Map("mapDiv");
      // map.centerAndZoom(new T.LngLat(108.95, 34.27), zoom);
      // lnglats = [];
      lnglats = [
        [74.438, 39.006, 1],
        [74.932, 38.382, 1],
        [75.402, 37.879, 1],
        [75.24, 38.777, 1],
        [75.264, 39.656, 1],
        [75.547, 37.826, 1],
        [75.769, 39.345, 1],
        [76.073, 38.162, 1],
        [76.154, 39.673, 1],
        [77.139, 37.549, 1],
        [76.821, 39.37, 1],
        [77.094, 40.11, 1],
        [77.363, 38.011, 1],
        [77.201, 39.44, 1],
        [77.921, 37.257, 1],
        [77.75, 37.929, 1],
        [77.835, 39.3, 1],
        [77.718, 39.828, 1],
        [77.975, 40.858, 1],
        [78.085, 36.315, 1],
        [78.266, 37.584, 1],
        [78.558, 37.505, 1],
        [78.449, 40.946, 1],
        [79.191, 32.206, 1],
        [78.918, 37.314, 1],
        [79.066, 39.855, 1],
        [79.057, 40.704, 1],
      ];
      // for (var i = 0; i < data.data.length; i++) {
      //   var ll = new T.LngLat(data.data[i][0], data.data[i][1]);
      //   lnglats.push(ll);
      // }
      if (document.createElement("canvas").getContext) {
        // 判断当前浏览器是否支持绘制海量点
        _CloudCollection = new T.CloudMarkerCollection(lnglats, {
          color: "blue",
          SizeType: TDT_POINT_SIZE_SMALL,
        });
        map.addOverLay(_CloudCollection);
      } else {
        alert("此示例目前只有在IE9及以上浏览器打开");
      }
      // let url =
      //   "http://lbs.tianditu.gov.cn/api/js4.0/opensource/data/points-sample-data.js";
      // axios
      //   .get(url, {})
      //   .then((res) => {
      //     console.log(res);
      //     console.log(res.data);
      //     console.log(typeof res.data);
      //     console.log(res.data.split("="));
      //     var tempdata = res.data.split("=");
      //     var test  = tempdata[1];
      //     console.log(test);
      //     // var testdata1 = JSON.parse(test);
      //     console.log(testdata1);
      //     lnglats = [];
      //     for (var i = 0; i < data.data.length; i++) {
      //       var ll = new T.LngLat(data.data[i][0], data.data[i][1]);
      //       lnglats.push(ll);
      //     }
      //     if (document.createElement("canvas").getContext) {
      //       // 判断当前浏览器是否支持绘制海量点
      //       _CloudCollection = new T.CloudMarkerCollection(lnglats, {
      //         color: "blue",
      //         SizeType: TDT_POINT_SIZE_SMALL,
      //       });
      //       map.addOverLay(_CloudCollection);
      //     } else {
      //       alert("此示例目前只有在IE9及以上浏览器打开");
      //     }
      //   })
      //   .catch((error) => {
      //     console.log("err");
      //   });
    },
  },
};
</script>

<style scoped>
</style>
