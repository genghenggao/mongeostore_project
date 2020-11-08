<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-03 15:11:11
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-08 22:21:39
-->
<template>
  <!-- 主界面-->
  <div class="maincontent">
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
          ><i class="el-icon-s-home"></i>首页</a
        >
        <a
          class="nav-item nav-link"
          id="nav-profile-tab"
          data-toggle="tab"
          href="#nav-profile"
          role="tab"
          aria-controls="nav-profile"
          aria-selected="false"
          ><i class="el-icon-s-data"></i>表格数据</a
        >
        <a
          class="nav-item nav-link"
          id="nav-metadata-tab"
          data-toggle="tab"
          href="#nav-metadata"
          role="tab"
          aria-controls="nav-metadata"
          aria-selected="false"
          ><i class="el-icon-s-data"></i>元数据</a
        >
        <a
          class="nav-item nav-link"
          id="nav-uploadfile-tab"
          data-toggle="tab"
          href="#nav-uploadfile"
          role="tab"
          aria-controls="nav-uploadfile"
          aria-selected="false"
          ><i class="el-icon-top"></i>上传数据</a
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
        <Home />
      </div>

      <div
        class="tab-pane fade"
        id="nav-profile"
        role="tabpanel"
        aria-labelledby="nav-profile-tab"
      >
        <Data />
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
        <UploadCSV />
        <UploadExcel />
      </div>
    </div>
  </div>
</template>

<script>
import MapView from "@/views/MapView.vue";
import Home from "@/views/Home.vue";
import UploadFile from "@/views/UploadFile.vue";
import UploadCSV from "@/views/UploadCSV.vue";
import UploadExcel from "@/views/UploadExcel.vue";
import SeiTable from "@/components/SeiTable.vue";
import Data from "@/components/Data.vue";
export default {
  name: "MainContent",
  components: {
    MapView,
    Home,
    SeiTable,
    UploadFile,
    UploadCSV,
    UploadExcel,
    Data
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

<style>
.maincontent div#nav-tab {
  height: 46px;
  /* background-color: rgba(21, 132, 197, 0.5); */
  background-color: #870000;
}
.maincontent div#nav-tab a{
  color: #b45c5c;
}
div#nav-tabContent{
  height: 775px;
}
</style>