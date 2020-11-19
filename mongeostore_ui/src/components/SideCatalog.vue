<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-18 15:08:08
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-19 19:18:54
-->
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-05 11:09:49
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-18 11:00:06
-->
<template>
  <!-- <el-container style="overflow:auto"> -->
  <div class="menutree">
    <div class="sidebar_header">
      <div class="title_img">
        <a
          href="https://www.cumtb.edu.cn/index.htm"
          title="中国矿业大学（北京）"
        >
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
                <i
                  class="el-icon-menu"
                  style="font-size: 17px; color: #870000"
                ></i>
                <span>地震大数据采集系统</span>
              </template>
              <el-menu-item-group>
                <SideTree />
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title">
                <i
                  class="el-icon-menu"
                  style="font-size: 17px; color: #870000"
                ></i>
                <span>钻孔数据管理子系统</span>
              </template>
              <el-menu-item-group>
                <el-submenu index="2-1">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>柠条塔工区</span>
                  </template>
                  <el-menu-item index="2-1-1"
                    ><i class="el-icon-document"></i>定位表</el-menu-item
                  >
                  <el-menu-item index="2-1-2"
                    ><i class="el-icon-document"></i>测斜表</el-menu-item
                  >
                  <el-menu-item index="2-1-3"
                    ><i class="el-icon-document"></i>化验表</el-menu-item
                  >
                  <el-menu-item index="2-1-4"
                    ><i class="el-icon-document"></i>岩性表</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="2-2">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>哈勒噶提工区</span></template
                  >
                  <el-menu-item index="2-2-1"
                    ><i class="el-icon-document"></i>哈勒噶提区域</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="2-3">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>钻孔数据管理子系统</span></template
                  >
                  <el-menu-item index="2-3-1"
                    ><i class="el-icon-document"></i>钻孔数据</el-menu-item
                  >
                  <el-menu-item index="2-3-2"
                    ><i class="el-icon-document"></i>DEM数据</el-menu-item
                  >
                  <el-menu-item index="2-3-3"
                    ><i class="el-icon-document"></i>地质剖面</el-menu-item
                  >
                  <el-menu-item index="2-3-4"
                    ><i class="el-icon-document"></i>空间索引</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="2-4">
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
            <el-submenu index="3">
              <template slot="title">
                <i
                  class="el-icon-menu"
                  style="font-size: 17px; color: #870000"
                ></i>
                <span>地质数据管理子系统</span>
              </template>
            </el-submenu>
          </el-menu>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import SideTree from "@/components/SideTree.vue";
export default {
  name: "SideCatalog",
  components: { SideTree },
  data() {
    return {
      // 搜索框
      state: "",
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      // console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      // console.log(key, keyPath);
    },
    handleSelect(path) {
      this.$router.push(path);
    },
    // 搜索框
    querySearch() {},
  },
};
</script>

<style lang="scss" >
// 头部
header.el-header {
  height: 106px;
}
.title_img {
  height: 55px;
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
  width: 280px;
  height: 775px;
  overflow: auto; //超出内容部分有下拉框
}

// 调整目录
.el-submenu__title {
  //   background-color: rgb(91, 160, 224);
  //   width: 200px;
  letter-spacing: 1px;
  position: left;
  //  设置内容靠左
  padding-left: 0px !important;

  text-align: left;
}
.el-submenu__title span {
  color: #870000;
  font-size: 15px;
  font-weight: bold;
}
// // 设置树形结构字体颜色
// .custom-tree-container .el-tree {
//   color: #870000;
// //   background-color: #b45c5c;
// }
// 设置树形结构字体大小
.custom-tree-node span {
  font-family: sans-serif;
  font-size: 14px;
  color: #870000; //这个地方设置，添加、删除图标也会变
}
// 图标位置大小设置
.el-menu .el-submenu [class^="el-icon-"] {
  vertical-align: middle;
  margin-right: 3px;
  margin-bottom: 5px;
}
</style>