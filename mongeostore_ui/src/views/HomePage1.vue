<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-03 15:18:02
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-09 09:26:41
-->
<template>
  <div>
    <Navbar />
    <el-container>
      <el-aside width="250px"><MenuTree /></el-aside>
      <el-main class="far_main_content">
        <el-header class="hompage_head">
          <div class="head_title">
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
        <el-main class="sub_main_content"><router-view></router-view></el-main>
      </el-main>
    </el-container>
    <!-- <el-footer> <Footbar /></el-footer> -->
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

<style >
/* 头部 */
.hompage_head {
  /* background-color: #106ba3; */
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

/* 侧边栏 */
.menutree {
  height: 881px;
  background: #ffffff;
  overflow: auto;
}
/* 主要内容 */
.el-main {
  padding: 0px;
}
/* .far_main_content {
  padding: 0px;
} */

/* 尾部 */
.el-footer {
  background-color: #a79f9f;
  color: rgb(134, 125, 125);
  text-align: center;
  line-height: 40px;
}
</style>