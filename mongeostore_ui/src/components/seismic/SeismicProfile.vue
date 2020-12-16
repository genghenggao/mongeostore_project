<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 15:37:36
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-16 15:42:58
-->
<template>
  <div>
    <div id="main" ref="chart"></div>
  </div>
</template>

<script>
var echarts = require("echarts");
export default {
  name: "SeismicProfile",
  data() {
    return {
      data: "",
      a: "g",
    };
  },
  created() {},
  mounted() {
    // 基于准备好的dom，初始化echarts实例
    let mychart = echarts.init(this.$refs.chart);
    mychart.showLoading();
    setTimeout(function () {
      let self = this;
      self.data = {
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "55%",
            roseType: "angle",
            backgroundColor: "#2c343c",
            itemStyle: {
              // 阴影的大小
              shadowBlur: 200,
              // 阴影水平方向上的偏移
              shadowOffsetX: 30,
              // 阴影垂直方向上的偏移
              shadowOffsetY: 40,
              emphasis: { shadowBlur: 800 },
              // 阴影颜色
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
            textStyle: {
              color: "rgba(255, 255, 255, 0.3)",
            },
            labelLine: {
              lineStyle: {
                color: "rgba(255, 255, 255, 0.3)",
              },
            },
            // 高亮样式。
            emphasis: {
              itemStyle: {
                // 高亮时点的颜色。
                color: "blue",
              },
              label: {
                show: true,
                // 高亮时标签的文字。
                color: "black",
              },
            },
            data: [
              { value: 235, name: "视频广告" },
              { value: 274, name: "联盟广告" },
              { value: 310, name: "邮件营销" },
              { value: 335, name: "直接访问" },
              { value: 400, name: "搜索引擎" },
            ],
          },
        ],
      };
      mychart.hideLoading();
      mychart.setOption(this.data);
    }, 3000);
    console.log(this.a);
    console.log(this.data);
  },
  watch: {},
  methods: {},
};
</script>

<style lang="scss" scoped>
#main {
  width: 600px;
  height: 400px;
  /* background-color:black;  */
  margin: 0 auto;
}
</style>