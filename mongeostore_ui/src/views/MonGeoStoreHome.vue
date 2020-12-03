<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-03 16:52:28
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-03 23:06:58
-->
<template>
  <div class="mongoestore_home">
    <el-container>
      <el-header
        ><div class="header"><h1>MonGeoStore系统简介</h1></div></el-header
      >
      <el-main style="padding: 0">
        <el-container class="act_one wow fadeInUp" data-wow-duration="0.5s">
          <el-row :gutter="20">
            <el-col :span="24" :offset="10">
              <h1>MongoGeoStore系统简介</h1>
              <p>
                系统主要使用SpringBoot框架，整合MongoDB数据库。<br />
                该系统主要用于解决海量地学数据的高性能存储，为地质工作者提供更好的服务。
              </p>
              <img src="@/assets/images/yanshitu.jpg" alt="" />
            </el-col>
          </el-row>
        </el-container>
        <el-container
          class="act_two wow fadeInUp"
          data-wow-duration="1s"
          data-wow-delay="1s"
        >
          <el-row :gutter="120">
            <el-col :span="8">
              <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                <img
                  src="@/assets/images/a.jpeg"
                  class="img-responsive"
                  alt=""
                />
                <h3>数据存储</h3>
                <p>数据存储阶段，支持海量数据的水平扩展</p>
              </a>
            </el-col>
            <el-col :span="8">
              <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                <img
                  src="@/assets/images/b.jpeg"
                  class="img-responsive"
                  alt=""
                />
                <h3>数据查询</h3>
                <p>数据查询阶段，支持海量数据的快速查询</p>
              </a>
            </el-col>
            <el-col :span="8">
              <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                <img
                  src="@/assets/images/c.jpeg"
                  class="img-responsive"
                  alt=""
                />
                <h3>数据更新</h3>
                <p>数据更新阶段，支持海量数据的实时更新</p>
              </a>
            </el-col>
          </el-row>
        </el-container>
        <el-container class="act_three">
          <el-row :gutter="50">
            <el-col :span="8" class="act_three_tips wow fadeInLeft">
              <h2>地学数据的多元(源)性与异构性</h2>
              <p>
                地学数据的多元(源)异构性，一方面体现在地学数据包含的数据类型众多，
                另一方面，数据的来源众多，这主要因为地学数据的采集的仪器类型特别多，并且其采集的数据类型也是各不相同。
                <el-divider></el-divider>
              </p>
              <p>
                <i class="el-icon-caret-right"></i>
                遥感数据的数据主要有BSQ、BIP、BIL等格式。
              </p>
              <el-divider></el-divider>
              <p>
                <i class="el-icon-caret-right"></i
                >地理信息方面的数据主要有Shapefile、Coverage、EOO、TAB等格式。
              </p>
            </el-col>
            <el-col :span="12" class="act_three_img wow fadeInRight">
              <img
                src="@/assets/images/duoyanxing.png"
                class="img-responsive"
                alt=""
              />
            </el-col>
          </el-row>
        </el-container>

        <el-container class="act_four">
          <el-row :gutter="120">
            <el-col :span="12">
              <img
                src="@/assets/images/shijian.jpg"
                class="img-responsive"
                alt=""
              />
            </el-col>
            <el-col :span="12">
              <h2>地学数据的时间性与空间性</h2>
              <p>
                地学数据的时间性体现在地学数据的获取时间上。地球系统是一个动态变化的系统，但它的变化速度常常十分缓慢。
              </p>
              <p>
                <span class="glyphicon glyphicon-grain mai-icon"></span>
                地学数据时间跨度从分秒跨越至数十万年，时间序列越长
                ,数据就越有价值 。
              </p>
              <p>
                <span class="glyphicon glyphicon-grain mai-icon"></span
                >具有明确的空间坐标 (经度、纬度和海拔高度 )且有一定的空间范围。
              </p>
            </el-col>
          </el-row>
        </el-container>

        <el-container class="act_five">
          <el-row :gutter="120">
            <el-col :span="8"> </el-col>
          </el-row>
        </el-container>
        <el-container
          class="act_six wow fadeInUp"
          data-wow-duration="1s"
          data-wow-delay="1s"
        >
          <el-row :gutter="120">
            <el-col :span="8"> </el-col>
          </el-row>
        </el-container>
        <el-container
          class="act_seven wow fadeInUp"
          data-wow-duration="1s"
          data-wow-delay="1s"
        >
          <el-row :gutter="120">
            <el-col :span="8"> </el-col>
          </el-row>
        </el-container>
      </el-main>
    </el-container>
           
  </div>
</template>

<script>
import "animate.css";
import WOW from "wowjs";
export default {
  name: "MonGeoStoreHome",
  data() {
    return {};
  },
  mounted() {
    // new this.$wow.WOW().init();
    let wow = new WOW.WOW({
      boxClass: "wow",
      animateClass: "animated",
      offset: 0,
      mobile: true,
      live: true,
    });
    wow.init();
  },
};
</script>

<style lang='scss'>
.act_one {
  margin-top: 70px;
  background: url("../assets/images/home-bg.jpg");
  background-size: cover;

  width: 100%;
  padding: 0;
  color: #ffffff;
  text-align: center;
}
.act_two {
  padding: 20px 30px 50px 380px;
  color: #ffffff;
}
.act_two h3 {
  font-weight: bold;
  color: #030303;
}
.act_two p {
  color: #000000;
}
.act_three {
  // padding: 20px 30px 50px 380px;
  padding: 80px 0 0 400px;
  background: #f8f8f8;
}

.act_three_tips {
  // color: #810000;
  text-align: left;
}
.act_three_tips h2 {
  font-weight: bold;
}
</style>