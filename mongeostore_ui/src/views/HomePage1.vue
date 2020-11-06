<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-03 15:18:02
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-06 20:09:26
-->
<template>
  <div>
    <Navbar />
    <el-container>
      <el-aside width="250px"><MenuTree /></el-aside>
      <el-container>
        <el-header>
          <div class="head title">
            地震数据管理系统
          </div>
          <div id="head1" class="logo f1">
            <a
              href="https://www.cumtb.edu.cn/index.htm"
              title="煤炭国家重点实验室"
            >
              <img src="@/assets/重点实验室logo-removebg.png" alt=""
            /></a>
          </div>
        </el-header>
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
  /* background-color: #106ba3; */
  font-size: 40px;
  height: 20px;
  font-family: serif;
  color: rgb(134, 163, 207);
  display: flex;
  justify-content: space-between;
  padding: 0; /* 消除子div边距*/
}
.head.title {
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
/* .head.title::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: -1;
  background: rgb(91, 137, 223);
  transform: perspective(0.5em) rotateX(deg);
  transform-origin: bottom left;
} */
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