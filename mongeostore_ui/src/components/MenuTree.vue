<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-05 11:09:49
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-03 16:19:50
-->
<template>
  <div class="menutree infinite-list" style="overflow:auto">
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
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleSelect(path) {
      this.$router.push(path);
    }
  }
};
</script>

<style lang="scss" scoped>
// .el-row.tac {
//   height: 100%;
//   width: 100%;
// }
.menutree {
  margin: 0px;
  padding: 0px;
  // width: 250px;
}
// .el-menu-item-group {
//   padding-left: 0px;
// }
</style>