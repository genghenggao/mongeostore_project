<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-18 14:59:33
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-24 16:14:33
-->
<template>
  <el-container>
    <el-header><Navbar /></el-header>
    <el-container>
      <el-aside><SideCatalog /></el-aside>
      <el-main
        ><el-container>
          <el-header class="main_head" style="min-width: 1100px"
            ><div class="head_title">
              {{ title_message }}
            </div>
            <div id="head1" class="logo f1">
              <a href="https://crsm.cumtb.edu.cn/" title="煤炭国家重点实验室">
                <img src="@/assets/重点实验室logo-removebg.png" alt=""
              /></a></div
          ></el-header>
          <el-main
            class="sub_main_content"
            style="min-width: 1100px"
            v-if="isRouterAlive"
            ><div v-if="!this.$store.state.DBorCol">
              <div
                v-if="
                  this.$store.state.temp_database == '钻孔数据管理子系统' &&
                  this.$store.state.title_message == '钻孔信息'
                "
              >
                <DrillMetaInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '钻孔数据管理子系统' &&
                  this.$store.state.title_message == '定位表'
                "
              >
                <DrillLocationInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '地震数据管理子系统' &&
                  this.$store.state.title_message == '地震数据'
                "
              >
                <SeismicInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '遥感数据管理子系统' &&
                  this.$store.state.title_message == '遥感影像'
                "
              >
                <RemoteInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '测井数据管理子系统' &&
                  this.$store.state.title_message == '测井数据'
                "
              >
                <LoggingInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '地质数据管理子系统' &&
                  this.$store.state.title_message == '地质数据'
                "
              >
                <GeologicalInfo />
              </div>
              <div
                v-else-if="
                  this.$store.state.temp_database == '地理数据管理子系统' &&
                  this.$store.state.title_message == '地理数据'
                "
              >
                <GeographicalInfo />
              </div>
              <div v-else>
                <CommonCol />
              </div>
            </div>
            <div v-else-if="this.$store.state.DBorCol">
              <!-- <router-link to="/about">about</router-link> <router-view /> -->

              <div
                v-if="this.$store.state.title_message == '钻孔数据管理子系统'"
              >
                <!-- {{ title_message }} -->
                <!-- <InclinationMeta /> -->
                <Inclination />
              </div>
              <div v-else>
                <CommonDB />
              </div>
            </div>
          </el-main> </el-container
      ></el-main>
    </el-container>
  </el-container>
</template>

<script>
import { mapState } from "vuex";
import Navbar from "@/components/Navbar.vue";
import SideCatalog from "@/components/SideCatalog.vue";
import SideTree from "@/components/SideTree.vue";
import CommonCol from "@/components/CommonCol.vue";
import CommonDB from "@/components/CommonDB.vue";
import InclinationData from "@/components/drill/InclinationData.vue";
import Inclination from "@/components/drill/Inclination.vue";
import DrillMetaInfo from "@/components/drill/DrillMetaInfo.vue";
import DrillLocationInfo from "@/components/drill/DrillLocationInfo.vue";
import SeismicInfo from "@/components/seismic/SeismicInfo.vue";
import RemoteInfo from "@/components/remote_sensing/RemoteInfo.vue";
import LoggingInfo from "@/components/logging/LoggingInfo.vue";
import GeologicalInfo from "@/components/geological/GeologicalInfo.vue";
import GeographicalInfo from "@/components/geographical/GeographicalInfo.vue";
// import Navbar from '../components/Navbar.vue';
export default {
  name: "MonGeoStore",
  provide() {
    return {
      reload: this.reload,
    };
  },
  components: {
    Navbar,
    SideCatalog,
    CommonCol,
    SideTree,
    CommonDB,
    InclinationData,
    Inclination,
    DrillMetaInfo,
    DrillLocationInfo,
    SeismicInfo,
    GeographicalInfo,
    RemoteInfo,
    LoggingInfo,
    GeologicalInfo,
  },
  data() {
    return {
      //   parent_message: "地震大数据管理系统",
      //   parent_message: this.$store.state.title_message,
      isRouterAlive: true,
    };
  },
  created() {},
  computed: {
    ...mapState(["title_message", "DBorCol", "temp_database"]), //title_message设置动态标题；DBorCol判断是数据库，还是集合；
  },
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(function () {
        this.isRouterAlive = true;
      });
    },
  },
};
</script>

<style lang="scss">
// 头部设置header
header.el-header {
  padding: 0; /* 消除子div边距*/
  height: 56px !important; //高度设置
}
// 侧边aside
aside.el-aside {
  width: 280px !important;
  // height: 881px;
  overflow: hidden;
  height: 100%;
}
.el-menu-item-group__title {
  padding: 0px 0 0px 0px;
}
// 主要内容main
main.el-main {
  padding: 0;
}
// 主要内容头部
.main_head {
  //   background-color: #106ba3;
  font-size: 40px;
  height: 20px;
  font-family: serif;
  color: rgb(42, 8, 194);
  display: flex;
  justify-content: space-between;
  padding: 0; /* 消除子div边距*/
}
/* 标题头部 */
.head_title {
  width: 1350px;
  height: 0px;
  color: #ffffff;
  text-align: left;
  letter-spacing: 10px;
  padding-left: 30px;
  /* text-align: 10px; */
  /* border-bottom: 60px solid rgb(90, 180, 216); */
  border-bottom: 60px solid #870000;
  /* 不是 border-right: 100px solid pink;  这样的话元素会没有高度 */
  border-right: 100px solid transparent;
}
</style>