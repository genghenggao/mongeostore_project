<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-02 18:57:20
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-24 09:47:51
-->
<template>
  <div class="drillmetahome" style="height: 800px">
    <div>
      <h2 style="color: #810000; padding-top: 30px">钻孔柱状图信息</h2>
    </div>
  <div>
     <img src="@/assets/images/ZK1柱状图.jpg" alt="">
  </div>
  </div>
</template>

<script>
// import Home from "@/views/Home.vue";
// import Navbar from "@/components/Navbar.vue";
// import Footbar from "@/components/Footbar.vue";

export default {
  name: "HomePage",
  components: {
    // Navbar,
    // Footbar
  },
};
</script>

<style lang="scss" scoped>
.carousel {
  width: 1000px;
  //   left: 500px;
  //   top: 150px;
  //   设置轮播图剧中
  margin: auto;
  position: relative;
  top: 150px;
  left: 0;
  right: 0;
  bottom: 0;
}
.d-block {
  height: 450px;
  filter: brightness(50%); //设置图片对比度
}
// .jumbotron {
//   //   设置轮播图剧中
//   top: 550px;
// }
// 重写Footbar.vue中的位置
.footer {
  position: absolute;
}
</style>