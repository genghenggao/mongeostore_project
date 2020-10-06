<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-25 17:06:12
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-06 20:53:09
-->
<template>
  <div>
    <Navbar />

    <div>
      <div
        id="carouselExampleIndicators"
        class="carousel slide"
        data-ride="carousel"
      >
        <ol class="carousel-indicators">
          <li
            data-target="#carouselExampleIndicators"
            data-slide-to="0"
            class="active"
          ></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              src="../assets/images/中秋.jpg"
              class="d-block w-100"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img
              src="../assets/images/教师节.png"
              class="d-block w-100"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img
              src="../assets/images/新同学.png"
              class="d-block w-100"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img
              src="../assets/images/抗击疫情.jpg"
              class="d-block w-100"
              alt="..."
            />
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="carousel-control-next"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    <div class="jumbotron">
      <h1 class="display-4">Hello, world!</h1>
      <p class="lead">
        This is a simple hero unit, a simple jumbotron-style component for
        calling extra attention to featured content or information.
      </p>
      <hr class="my-4" />
      <p>
        It uses utility classes for typography and spacing to space content out
        within the larger container.
      </p>
      <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
    </div>
    <Footbar />
  </div>
</template>

<script>
import aa from "@/assets/images/aa.jpg"; //	如果使用网络图片资源就无需引入
// import bb from "@/assets/images/bb.jpg"	//	如果使用网络图片资源就无需引入
// import cc from "@/assets/images/cc.jpg"	//	如果使用网络图片资源就无需引入
// import dd from "@/assets/images/dd.jpg"	//	如果使用网络图片资源就无需引入
// import ee from "@/assets/images/ee.jpg"	//	如果使用网络图片资源就无需引入
// import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from "@/components/Navbar.vue";
import Footbar from "@/components/Footbar.vue";
export default {
  name: "test",
  components: {
    Navbar,
    Footbar
  },
  data() {
    return {
      msg: "",
      bgimgs: [aa],
      //   bgimgs:[ aa, bb, cc, dd, ee, ],
      //   bgimgs:[],	//	如果使用网络图片资源就用该值
      text: "向右滑动~"
    };
  },
  methods: {
    onSuccess() {
      this.msg = "登录成功~";
    },
    onFail() {
      this.msg = "登录失败！";
    },
    onRefresh() {
      this.msg = "重新生成验证码";
    }
  }
};
</script>
<style lang="scss">


</style>
