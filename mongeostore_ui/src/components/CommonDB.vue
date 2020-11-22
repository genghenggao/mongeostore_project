<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-19 15:15:31
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-22 22:34:23
-->

<template>
  <!-- 主界面-->
  <div class="maincontent">
    <!-- 子导航 -->
    <el-container>
      <el-header class="maincontent_header">
        <nav>
          <div
            class="nav nav-tabs"
            id="nav-tab"
            role="tablist"
            style="min-width: 1100px"
          >
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
              ><i class="el-icon-document"></i>元数据</a
            >
            <a
              class="nav-item nav-link"
              id="nav-metadata-tab"
              data-toggle="tab"
              href="#nav-metadata"
              role="tab"
              aria-controls="nav-metadata"
              aria-selected="false"
              ><i class="el-icon-s-data">统计信息</i></a
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
      </el-header>
      <el-main>
        <div class="tab-content" id="nav-tabContent">
          <div
            class="tab-pane fade show active"
            id="nav-home"
            role="tabpanel"
            aria-labelledby="nav-home-tab"
          >
            <HomePage />
          </div>

          <div
            class="tab-pane fade"
            id="nav-profile"
            role="tabpanel"
            aria-labelledby="nav-profile-tab"
          >
            <SeiTable />
          </div>
          <div
            class="tab-pane fade"
            id="nav-metadata"
            role="tabpanel"
            aria-labelledby="nav-metadata-tab"
          >
            <!-- <CommonData /> -->
          </div>
          <div
            class="tab-pane fade"
            id="nav-uploadfile"
            role="tabpanel"
            aria-labelledby="nav-uploadfile-tab"
          >
            <CommonUploadMeta />
            <!-- <UploadCSV /> -->
            <!-- <UploadExcel /> -->
            <!-- <CommonUploadExcel /> -->
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import MapView from "@/views/MapView.vue";
import Home from "@/views/Home.vue";
import HomePage from "@/views/HomePage.vue";
import UploadFile from "@/views/UploadFile.vue";
import UploadCSV from "@/views/UploadCSV.vue";
import UploadExcel from "@/views/UploadExcel.vue";
import SeiTable from "@/components/SeiTable.vue";
import CommonUploadExcel from "@/components/CommonUploadExcel.vue";
import CommonData from "@/components/CommonData.vue";
import CommonUploadMeta from "@/components/CommonUploadMeta.vue";
export default {
  name: "CommonDB",
  components: {
    MapView,
    Home,
    HomePage,
    SeiTable,
    UploadFile,
    UploadCSV,
    // UploadExcel,
    CommonData,
    CommonUploadExcel,
    CommonUploadMeta,
  },
  data() {
    return {
      activeIndex: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>

<style lang="scss" scoped>
.maincontent {
  height: 821px;
}
/* 导航子标题 */
.maincontent_header {
  /* 固定高度 */
  height: 46px !important;
  /* 消除边距 */
  padding: 0;
  // 固定内容
}
/* maincontent子导航 */
.maincontent div#nav-tab {
  height: 46px;
  /* width: 100%; */
  /* background-color: rgba(21, 132, 197, 0.5); */
  background-color: #870000;
  /* position: static; */
}
/* maincontent子导航 字体 */
.maincontent div#nav-tab a {
  color: #b45c5c;
}
div#nav-tabContent {
  height: 775px;
}
</style>