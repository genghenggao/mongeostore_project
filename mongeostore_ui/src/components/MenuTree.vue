<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-05 11:09:49
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-16 08:56:55
-->
<template>
  <!-- <el-container style="overflow:auto"> -->
  <div class="menutree">
    <div class="sidebar_header">
      <div class="title_img">
        <a href="https://crsm.cumtb.edu.cn/" title="煤炭国家重点实验室">
          <img
            style="width: 240px; height: 42px"
            src="@/assets/logo-20191228.png"
            alt=""
          />
        </a>
      </div>
      <div class="title_search">
        <el-row class="demo-autocomplete">
          <el-col :span="15">
            <el-autocomplete
              class="inline-input"
              v-model="state"
              :fetch-suggestions="querySearch"
              placeholder="请输入搜索内容"
              :trigger-on-focus="false"
              @select="handleSelect"
            ></el-autocomplete>
          </el-col>
          <el-col :span="9"
            ><el-button
              type=""
              plain
              size="small"
              icon="el-icon-search"
              style="font-size: 15px; color: #b36262"
              >搜索</el-button
            ></el-col
          >
        </el-row>
      </div>
    </div>

    <div class="mentree_content">
      <!-- <div class="menutree infinite-list" style="overflow:auto"> -->
      <el-row class="tac">
        <el-col :span="24">
          <el-menu
            :default-active="$route.path"
            @select="handleSelect"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
          >
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>地震数据采集子系统</span>
              </template>
              <el-menu-item-group>
                <!-- <el-menu-item index="1-1">钻孔数据</el-menu-item>
              <el-menu-item index="1-2">钻孔数据</el-menu-item>
              <el-menu-item index="1-3">钻孔数据</el-menu-item> -->
                <el-submenu index="1-1">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>地质数据管理子系统</span>
                  </template>
                  <el-menu-item index="1-1-1"
                    ><i class="el-icon-document"></i>柠条塔工区</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-2">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>地震数据处理子系统</span></template
                  >
                  <el-menu-item index="1-2-1"
                    ><i class="el-icon-document"></i>哈勒噶提区域</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-3">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>钻孔数据管理子系统</span></template
                  >
                  <el-menu-item index="1-3-1"
                    ><i class="el-icon-document"></i>钻孔数据</el-menu-item
                  >
                  <el-menu-item index="1-3-2"
                    ><i class="el-icon-document"></i>DEM数据</el-menu-item
                  >
                  <el-menu-item index="1-3-3"
                    ><i class="el-icon-document"></i>地质剖面</el-menu-item
                  >
                  <el-menu-item index="1-3-4"
                    ><i class="el-icon-document"></i>空间索引</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-4">
                  <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>地震历史数据子系统</span></template
                  >
                  <el-menu-item index="1-4-1"
                    ><i class="el-icon-document"></i>选项1</el-menu-item
                  >
                </el-submenu>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>钻孔数据管理子系统</span>
              </template>
              <el-menu-item-group>
                <el-submenu index="1-1">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>柠条塔工区</span>
                  </template>
                  <el-menu-item index="1-1-1"
                    ><i class="el-icon-document"></i>定位表</el-menu-item
                  >
                  <el-menu-item index="1-1-2"
                    ><i class="el-icon-document"></i>测斜表</el-menu-item
                  >
                  <el-menu-item index="1-1-2"
                    ><i class="el-icon-document"></i>化验表</el-menu-item
                  >
                  <el-menu-item index="1-1-2"
                    ><i class="el-icon-document"></i>岩性表</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-2">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>哈勒噶提工区</span></template
                  >
                  <el-menu-item index="1-2-1"
                    ><i class="el-icon-document"></i>哈勒噶提区域</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-3">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>钻孔数据管理子系统</span></template
                  >
                  <el-menu-item index="1-3-1"
                    ><i class="el-icon-document"></i>钻孔数据</el-menu-item
                  >
                  <el-menu-item index="1-3-2"
                    ><i class="el-icon-document"></i>DEM数据</el-menu-item
                  >
                  <el-menu-item index="1-3-3"
                    ><i class="el-icon-document"></i>地质剖面</el-menu-item
                  >
                  <el-menu-item index="1-3-4"
                    ><i class="el-icon-document"></i>空间索引</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-4">
                  <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>地震历史数据子系统</span></template
                  >
                  <el-menu-item index="1-4-1"
                    ><i class="el-icon-document"></i>选项1</el-menu-item
                  >
                </el-submenu>
              </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="/maincontent">
              <i class="el-icon-menu"></i>
              <span slot="title">钻孔数据管理子系统</span>
            </el-menu-item>

            <el-menu-item index="3">
              <i class="el-icon-menu"></i>
              <span slot="title">地质数据管理子系统</span>
            </el-menu-item>
            <el-menu-item index="4">
              <i class="el-icon-menu"></i>
              <span slot="title">地震历史数据子系统</span>
            </el-menu-item>
            <el-menu-item index="5">
              <i class="el-icon-menu"></i>
              <span slot="title">地震数据成果子系统</span>
            </el-menu-item>
            <el-menu-item index="6">
              <i class="el-icon-menu"></i>
              <span slot="title">遥感数据管理子系统</span>
            </el-menu-item>
            <el-menu-item index="7">
              <i class="el-icon-menu"></i>
              <span slot="title">矿产资源管理子系统</span>
            </el-menu-item>
            <el-menu-item index="8">
              <i class="el-icon-menu"></i>
              <span slot="title">地理数据管理子系统</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuTree",
  data() {
    return {
      // 搜索框
      state: ""
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleSelect(path) {
      this.$router.push(path);
    },
    // 搜索框
    querySearch() {}
  }
};
</script>

<style lang="scss" scoped>
// 头部
header.el-header {
  height: 106px;
}
.title_img {
  height: 60px;
  background: #870000;
  color: #b45c5c;
  padding-top: 10px;
  // letter-spacing: 40px;
  // box-pack: start;
  // padding-left: 20px;
}
// 侧边搜索
.title_search {
  background-color: #870000;
  height: 46px;
  padding-top: 3px;
}
// 搜索按钮的颜色
button.el-button.el-button--small.is-plain {
  margin: 3px;
  background: #870000;
}
// 侧边主要内容
.mentree_content {
  width: 250px;
  height: 775px ;
  overflow: auto; //超出内容部分有下拉框
}
</style>