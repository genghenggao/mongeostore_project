<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-05 11:09:49
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-07 18:54:51
-->
<template>
  <!-- <el-container style="overflow:auto"> -->
  <div class="menutree">
    <!-- <div class="title"><h2>目录</h2></div> -->
    <div class="title">
      <a href="https://crsm.cumtb.edu.cn/" title="煤炭国家重点实验室">
        <img
          style="width: 240px; height: 42px"
          src="@/assets/logo-20191228.png"
          alt=""
        />
      </a>
    </div>
    <div class="title-search">
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
    <div class="mentree-content">
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
                    <span>地质数据采集子系统</span>
                  </template>
                  <el-menu-item index="1-1-1"
                    ><i class="el-icon-document"></i>选项1</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-2">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>地震数据处理子系统</span></template
                  >
                  <el-menu-item index="1-2-1"
                    ><i class="el-icon-document"></i>选项1</el-menu-item
                  >
                </el-submenu>
                <el-submenu index="1-3">
                  <template slot="title">
                    <i class="el-icon-folder-opened"></i>
                    <span>地质数据管理子系统</span></template
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
              <span slot="title">地震数据处理子系统</span>
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
              <span slot="title">地震数据成果子系统</span>
            </el-menu-item>
            <el-menu-item index="7">
              <i class="el-icon-menu"></i>
              <span slot="title">地震数据成果子系统</span>
            </el-menu-item>
            <el-menu-item index="8">
              <i class="el-icon-menu"></i>
              <span slot="title">地震数据成果子系统</span>
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
.title {
  height: 60px;
  background: #870000;
  color: #b45c5c;
  padding-top: 10px;
  // letter-spacing: 40px;
  // box-pack: start;
  // padding-left: 20px;
}
.title a {
  color: rgb(40, 185, 142);
}
.title-search {
  background-color: #870000;
  height: 46px;
  padding-top: 3px;
}

.demo-autocomplete h5 {
  padding-top: 6px;
  color: #b36262;
  font-size: 20px;
}
// 搜索按钮的颜色
button.el-button.el-button--small.is-plain {
  margin: 3px;
  background: #870000;
}
</style>