<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-01 08:57:34
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-24 09:44:06
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
              ><i class="el-icon-s-data"></i>钻孔数据</a
            >
            <a
              class="nav-item nav-link"
              id="nav-metadata-tab"
              data-toggle="tab"
              href="#nav-metadata"
              role="tab"
              aria-controls="nav-metadata"
              aria-selected="false"
              ><i class="el-icon-document"></i>钻孔信息</a
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
            <!-- <Home /> -->
            <DrillMetaHome />
          </div>

          <div
            class="tab-pane fade"
            id="nav-profile"
            role="tabpanel"
            aria-labelledby="nav-profile-tab"
          >
            <!-- <CommonData /> -->
            <DrillMetaData />
            <!-- 钻孔的数据列表 -->
            <!-- <InclinationData /> -->
          </div>
          <div
            class="tab-pane fade"
            id="nav-metadata"
            role="tabpanel"
            aria-labelledby="nav-metadata-tab"
          >
            <!-- <SeiTable /> -->
            <!-- <router-view></router-view> -->
            <DrillDetails />
          </div>
          <div
            class="tab-pane fade"
            id="nav-uploadfile"
            role="tabpanel"
            aria-labelledby="nav-uploadfile-tab"
          >
            <!-- <UploadFile /> -->
            <!-- <UploadCSV /> -->
            <!-- <UploadExcel /> -->
            <!-- <CommonUploadExcel /> -->
            <!-- <CommonUploadCSV /> -->
            <DrillUpload />
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import MapView from "@/views/MapView.vue";
import Home from "@/views/Home.vue";
import UploadFile from "@/views/UploadFile.vue";
import UploadCSV from "@/views/UploadCSV.vue";
import UploadExcel from "@/views/UploadExcel.vue";
import SeiTable from "@/components/SeiTable.vue";
import CommonData from "@/components/CommonData.vue";
import CommonUploadExcel from "@/components/CommonUploadExcel.vue";
import CommonUploadCSV from "@/components/CommonUploadCSV.vue";
import InclinationData from "@/components/drill/InclinationData.vue";
import DrillDetails from "@/components/drill/DrillDetails.vue";
import DrillMetaData from "@/components/drill/DrillMetaData.vue";
import DrillUpload from "@/components/drill/DrillUpload.vue";
import DrillMetaHome from "@/components/drill/DrillMetaHome.vue";
export default {
  name: "DrillMetaInfo",
  components: {
    MapView,
    Home,
    SeiTable,
    UploadFile,
    UploadCSV,
    UploadExcel,
    CommonData,
    CommonUploadExcel,
    CommonUploadCSV,
    InclinationData,
    DrillDetails,
    DrillMetaData,
    DrillUpload,
    DrillMetaHome,
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
// .maincontent {
//   // height: 821px;
//   // height: 850px;
// }
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
// div#nav-tabContent {
//   // height: 775px;
//   // height: 780px;
// }
</style>