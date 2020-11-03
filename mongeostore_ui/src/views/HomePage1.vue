<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-03 15:18:02
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-03 16:43:38
-->
<template>
  <div>
    <Navbar />
    <el-container>
      <el-aside width="200px"><MenuTree /></el-aside>
      <el-container>
        <el-header>地震数据管理系统</el-header>
        <el-main><router-view></router-view></el-main>
      </el-container>
    </el-container>
    <Footbar />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import MenuTree from "@/components/MenuTree.vue";
import Footbar from "@/components/Footbar.vue";
export default {
  name: "HomePage1",
  components: { Navbar, MenuTree, Footbar },
  methods: {}
};
</script>

<style>
.el-header {
  background-color: rgb(255, 255, 255);
  font-size: 30px;
  height: 20px;
  color: rgb(134, 163, 207);
}
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
/* .el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
} */
/* .el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
} */
/* body > .el-container {
  margin-bottom: 40px;
} */
/* .el-container:nth-child(5) .el-aside, */
/* .el-container:nth-child(6) .el-aside {
  line-height: 260px;
} */
/* .el-container:nth-child(7) .el-aside {
  line-height: 320px;
} */

.menutree {
  height: 840px;
  background: #ffffff;
}
.el-main {
  padding: 0px;
}
element.style {
  height: 40px;
}
</style>