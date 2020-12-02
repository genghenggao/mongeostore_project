<template>
  <div class="drillmetahome" style="height: 800px">
    <div>
      <h2 style="color: #810000; padding-top: 30px">钻孔元数据信息</h2>
    </div>
    <div
      id="carouselExampleCaptions"
      class="carousel slide"
      data-ride="carousel"
    >
      <ol class="carousel-indicators">
        <li
          data-target="#carouselExampleCaptions"
          data-slide-to="0"
          class="active"
        ></li>
        <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
        <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="@/assets/images/bg_semsic.jpg"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>First slide label</h5>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/images/bg_semsic2.png"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>Second slide label</h5>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/images/bg_semsic3.png"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>Third slide label</h5>
            <p>
              Praesent commodo cursus magna, vel scelerisque nisl consectetur.
            </p>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselExampleCaptions"
        role="button"
        data-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselExampleCaptions"
        role="button"
        data-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
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