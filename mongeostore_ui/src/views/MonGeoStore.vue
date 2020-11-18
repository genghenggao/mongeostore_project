<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-18 14:59:33
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-18 21:32:55
-->
<template>
  <el-container>
    <el-header><Navbar /></el-header>
    <el-container>
      <el-aside><SideCatalog /></el-aside>
      <el-main
        ><el-container>
          <el-header class="main_head" style="min-width: 1100px"
            ><div class="head_title">钻孔数据管理子系统</div>
            <div id="head1" class="logo f1">
              <a
                href="https://www.cumtb.edu.cn/index.htm"
                title="煤炭国家重点实验室"
              >
                <img src="@/assets/重点实验室logo-removebg.png" alt=""
              /></a></div
          ></el-header>
          <el-main class="sub_main_content"
            ><CommonModule
          /></el-main> </el-container
      ></el-main>
    </el-container>
  </el-container>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import SideCatalog from "@/components/SideCatalog.vue";
import CommonModule from "@/components/CommonModule.vue";
// import Navbar from '../components/Navbar.vue';
export default {
  name: "MonGeoStore",
  components: { Navbar, SideCatalog, CommonModule },
  data() {
    return {};
  },
  created() {},
  methods: {},
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
  height: 881px;
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