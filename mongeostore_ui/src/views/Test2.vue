<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-28 18:39:36
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-03 10:07:36
-->
<template>
  <div>
    <!-- header -->
    <Navbar />

    <div class="row">
      <!-- menutree -->
      <div class="col-2">
        <MenuTree />
      </div>
      <!-- 主界面-->
      <div class="col-10">
        <div><h2  class="text-monospace">地震数据管理子系统</h2></div>
        <!-- 子导航 -->
        <nav>
          <div class="nav nav-tabs" id="nav-tab" role="tablist">
            <a
              class="nav-item nav-link active"
              id="nav-home-tab"
              data-toggle="tab"
              href="#nav-home"
              role="tab"
              aria-controls="nav-home"
              aria-selected="true"
              >Home</a
            >
            <a
              class="nav-item nav-link"
              id="nav-profile-tab"
              data-toggle="tab"
              href="#nav-profile"
              role="tab"
              aria-controls="nav-profile"
              aria-selected="false"
              >Profile</a
            >
            <a
              class="nav-item nav-link"
              id="nav-metadata-tab"
              data-toggle="tab"
              href="#nav-metadata"
              role="tab"
              aria-controls="nav-metadata"
              aria-selected="false"
              >MetaData</a
            >
            <a
              class="nav-item nav-link"
              id="nav-uploadfile-tab"
              data-toggle="tab"
              href="#nav-uploadfile"
              role="tab"
              aria-controls="nav-uploadfile"
              aria-selected="false"
              >UploadFile</a
            >
          </div>
        </nav>
        <div class="tab-content" id="nav-tabContent">
          <div
            class="tab-pane fade show active"
            id="nav-home"
            role="tabpanel"
            aria-labelledby="nav-home-tab"
          >
            <MapView />
          </div>

          <div
            class="tab-pane fade"
            id="nav-profile"
            role="tabpanel"
            aria-labelledby="nav-profile-tab"
          >
            <HomePage />
          </div>
          <div
            class="tab-pane fade"
            id="nav-metadata"
            role="tabpanel"
            aria-labelledby="nav-metadata-tab"
          >
            <SeiTable />
          </div>
          <div
            class="tab-pane fade"
            id="nav-uploadfile"
            role="tabpanel"
            aria-labelledby="nav-uploadfile-tab"
          >
            <UploadFile />
          </div>
        </div>
        <!-- <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">First</th>
              <th scope="col">Last</th>
              <th scope="col">Handle</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Mark</td>
              <td>Otto</td>
              <td>@mdo</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Jacob</td>
              <td>Thornton</td>
              <td>@fat</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td colspan="2">Larry the Bird</td>
              <td>@twitter</td>
            </tr>
          </tbody>
        </table> -->
      </div>
    </div>
    <Footbar />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footbar from "@/components/Footbar.vue";
import MenuTree from "@/components/MenuTree.vue";
import Home from "@/views/Home.vue";
import MapView from "@/views/MapView.vue";
import HomePage from "@/views/HomePage.vue";
import UploadFile from "@/views/UploadFile.vue";
import SeiTable from "@/components/SeiTable.vue";
export default {
  name: "test2",
  components: {
    Navbar,
    Footbar,
    MenuTree,
    MapView,
    HomePage,
    Home,
    SeiTable,
    UploadFile
  },
  data() {
    return {
      activeIndex: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<style lang="scss" scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.menutree {
  height: 840px;
  background: #ffffff;
}
.row {
  padding: 0;
}
.col-2 {
  // 消除边距
  // padding: 0;
  // height: 100%;
  // padding-left: 0;
  // padding-right: 0;
  // padding-bottom: 50px;
  margin: 0px;
  padding: 0px;
}
.col-10 {
  // padding-left: 0;
  // padding-right: 0;
  margin: 0px;
  padding: 0px;
  // height: 100vh;
}
.row {
  margin: 0px;
  padding: 0px;
}
</style>