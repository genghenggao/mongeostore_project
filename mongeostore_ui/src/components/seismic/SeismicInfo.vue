<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 14:34:23
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-17 22:24:36
-->
<template>
  <!-- 主界面-->
  <div class="maincontent" style="overflow: hidden">
    <!-- 子导航 -->
    <el-container>
      <el-header class="maincontent_header">
        <el-menu
          router
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <el-menu-item index="/mongeostore/seismichome"
            ><i class="el-icon-s-home"></i>
            首页
          </el-menu-item>
          <el-menu-item index="/mongeostore/seismicmetadata"
            ><i class="el-icon-s-data"></i>元数据
          </el-menu-item>
          <el-menu-item index="/mongeostore/seismicprofile"
            ><i class="el-icon-document"></i>地震剖面</el-menu-item
          >
          <el-menu-item index="/mongeostore/seismicanalysis"
            ><i class="el-icon-document"></i>解析数据</el-menu-item
          >
          <el-menu-item index="/mongeostore/seismicupload"
            ><i class="el-icon-upload"></i>上传数据</el-menu-item
          >
        </el-menu>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import SeismicHome from "@/components/seismic/SeismicHome.vue";
export default {
  name: "SeismicInfo",
  components: {
    SeismicHome,
  },
  data() {
    return {
      activeIndex: "",
    };
  },
  mounted() {
    //  _this.activeIndex=window.location.href.split('/')[4];
    //  console.log(window.location.href.split('/'));
    this.activeIndex = "/mongeostore/seismichome";
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
  color: #ac8585;
}
.maincontent .el-menu-item i {
  color: #ac8585;
  font-size: 25px;
  padding-bottom: 6px;
}
// div#nav-tabContent {
//   // height: 775px;
//   // height: 780px;
// }
.el-menu-demo {
  height: 46px;
  background-color: #870000;
}
.el-menu-demo .el-menu-item {
  font-size: 20px;
  color: #b47777;
}
.el-menu--horizontal > .el-menu-item {
  float: left;
  height: 46px;
  line-height: 46px;
  margin: 0;
}
</style>