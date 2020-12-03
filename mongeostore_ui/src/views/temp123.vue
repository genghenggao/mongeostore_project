<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-03 20:35:16
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-03 21:09:19
-->
<template>
  <div class="mongoestore_home">
    <!-- 导航 -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <!-- 小屏幕按钮和logo -->
          <button
            class="navbar-toggle"
            data-toggle="collapse"
            data-target=".navbar-collapse"
          >
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a href="index.html" class="navbar-brand">MonGeoStore</a>
          <!-- 小屏幕按钮和logo -->
        </div>

        <!-- 导航 -->
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#home">首页</a></li>
            <li><a href="#bbs">论坛</a></li>
            <li><a href="#html5">最新成果</a></li>
            <li><a href="#course">建议反馈</a></li>
            <li><a href="#app">移动App</a></li>
            <li><a href="#contact">联系我们</a></li>
          </ul>
        </div>
        <!-- 导航 -->

        <!-- home -->
        <section id="home">
          <div class="lvjing">
            <div class="container">
              <div class="row wow fadeInUp" data-wow-duration="0.5s">
                <div class="col-md-1"></div>
                <div class="col-md-10">
                  <h1>MongoGeoStore系统简介</h1>
                  <p>
                    系统主要使用SpringBoot框架，整合MongoDB数据库。<br />
                    该系统主要用于解决海量地学数据的高性能存储，为地质工作者提供更好的服务。
                  </p>
                  <img
                    src="@/assets/images/yanshitu.jpg"
                    class="img-responsive"
                    alt="yanshitu"
                  />
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- home -->

        <!-- bbs -->
        <section id="bbs">
          <div class="container">
            <div
              class="row wow fadeInUp"
              data-wow-duration="1s"
              data-wow-delay="1s"
            >
              <div class="col-md-4">
                <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                  <img
                    src="@/assets/images/a.jpeg"
                    class="img-responsive"
                    alt=""
                  />
                  <h3>数据存储</h3>
                  <p>数据存储阶段，支持海量数据的水平扩展</p>
                </a>
              </div>
              <div class="col-md-4">
                <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                  <img
                    src="@/assets/images/b.jpeg"
                    class="img-responsive"
                    alt=""
                  />
                  <h3>数据查询</h3>
                  <p>数据查询阶段，支持海量数据的快速查询</p>
                </a>
              </div>
              <div class="col-md-4">
                <a href="https://www.cnblogs.com/genghenggao/" target="_blank">
                  <img
                    src="@/assets/images/c.jpeg"
                    class="img-responsive"
                    alt=""
                  />
                  <h3>数据更新</h3>
                  <p>数据更新阶段，支持海量数据的实时更新</p>
                </a>
              </div>
            </div>
          </div>
        </section>
        <!-- bbs -->

        <!-- html5 -->
        <section id="html5">
          <div class="container">
            <div class="col-md-6 wow fadeInLeft">
              <h2>地学数据的多元(源)性与异构性</h2>
              <p>
                地学数据的多元(源)异构性，一方面体现在地学数据包含的数据类型众多，
                另一方面，数据的来源众多，这主要因为地学数据的采集的仪器类型特别多，并且其采集的数据类型也是各不相同。
              </p>
              <p>
                <span class="glyphicon glyphicon-grain mai-icon"></span>
                遥感数据的数据主要有BSQ、BIP、BIL等格式。
              </p>
              <p>
                <span class="glyphicon glyphicon-grain mai-icon"></span
                >地理信息方面的数据主要有Shapefile、Coverage、EOO、TAB等格式。
              </p>
            </div>
            <div class="col-md-6 wow fadeInRight">
              <img
                src="@/assets/images/duoyanxing.png"
                class="img-responsive"
                alt=""
              />
            </div>
          </div>
        </section>
        <!-- html5 -->

        <!-- BootStrap -->
        <section id="bootstrap">
          <div class="container wow fadeInUp" data-wow-duration="0.5s">
            <div class="col-md-6">
              <img
                src="@/assets/images/shijian.jpg"
                class="img-responsive"
                alt=""
              />
            </div>
            <div class="col-md-6">
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
            </div>
          </div>
        </section>
        <!-- BootStrap -->

        <!-- course -->
        <section id="course">
          <div class="container">
            <div class="row wow fadeIn" data-wow-delay="0.6s">
              <div class="col-md-12">
                <h2>最新发现</h2>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
              <div class="col-md-3">
                <div class="course">
                  <img
                    src="@/assets/images/yanshi.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <a
                    href="https://www.cnblogs.com/genghenggao/"
                    class="btn btn-primary"
                    target="_blank"
                    role="button"
                  >
                    加入研究
                  </a>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- course -->
        <!-- App -->
        <section id="mongeostore_app">
          <div class="container">
            <div class="row wow fadeInUp" data-wow-duration="0.5s">
              <div class="col-md-6">
                <h2>MongoGeoStore移动App下载</h2>
                <p>
                  MongoGeoStore,一种基于MongoDB的地学数据存储管理系统，
                  使用MongoDB作为数据库，很好的用于解决地学数据的结构化、半结构化和非结构化数据存储问题。
                  该系统就有高度的安全性、可扩展性、并行性，实现数据的快速存储、查找，
                  作为一种工具为地质工作者提供很好的服务。
                </p>
                <button class="btn btn-primary">
                  <span class="glyphicon glyphicon-download-alt"></span>
                  iPhone版
                </button>
                <button class="btn btn-primary">
                  <span class="glyphicon glyphicon-download-alt"></span>
                  Android版
                </button>
              </div>
              <div class="col-md-6"></div>
              <img
                src="@/assets/images/diqiuapp.png"
                class="img-responsive"
                alt=""
              />
            </div>
          </div>
        </section>
        <!-- App -->

        <!-- contact -->
        <section id="contact">
          <div class="lvjing1">
            <div class="container">
              <div class="row">
                <div class="col-md-6 wow fadeInLeft">
                  <h2>
                    <span class="glyphicon glyphicon-send"></span>
                    &nbsp; 联系我们
                  </h2>
                  <p>MongoGeoStore,一种基于MongoDB的地学数据存储管理系统。</p>
                  <address>
                    <p>
                      <span class="glyphicon glyphicon-home"></span>
                      &nbsp;
                      地址：北京市海淀区学院路丁11号，中国矿业大学（北京）
                    </p>
                    <p>
                      <span class="glyphicon glyphicon-phone-alt"></span>
                      &nbsp; 联系电话：15518501828
                    </p>
                    <p>
                      <span class="glyphicon glyphicon-envelope"></span>
                      &nbsp; 邮箱：genghenggao@outlook.com
                    </p>
                  </address>
                </div>
                <div class="col-md-6 wow fadeInRight">
                  <form action="#" method="POST">
                    <div class="col-md-6">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="您的姓名"
                      />
                    </div>
                    <div class="col-md-6">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="您的邮箱"
                      />
                    </div>
                    <div class="col-md-12">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="标题"
                      />
                    </div>

                    <div class="col-md-12">
                      <textarea
                        class="form-control"
                        placeholder="留言内容"
                        rows="4"
                      ></textarea>
                    </div>
                    <div class="col-md-8">
                      <input type="submit" class="form-control" value="提交" />
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- contact -->

        <!-- footer -->
        <footer>
          <div class="container">
            <div class="row">
              <div class="col=-md-12">
                <p>
                  Copyright
                  &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                  京公网安备：110402430067号
                </p>
              </div>
            </div>
          </div>
        </footer>
        <!-- footer -->
      </div>
    </nav>
    <!-- 导航 -->
           
  </div>
</template>

<script>
import "animate.css";
import WOW from "wowjs";
import "@/assets/css/mongeostore_home.css";
export default {
  name: "Home",
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
</style>