<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-18 15:08:08
 * @LastEditors: henggao
 * @LastEditTime: 2021-01-19 19:38:16
-->
<template>
  <!-- <el-container style="overflow:auto"> -->
  <div class="menutree" style="overflow: hidden">
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
          <!-- <el-col :span="15">
            <el-autocomplete
              class="inline-input"
              v-model="state"
              :fetch-suggestions="querySearch"
              placeholder="请输入搜索内容"
              :trigger-on-focus="false"
              @select="handleSelect"
            ></el-autocomplete>
          </el-col> -->
          <el-col :span="24">
            <!-- <el-button
              type=""
              plain
              size="small"
              icon="el-icon-search"
              style="font-size: 15px; color: #b36262"
              >搜索</el-button
            > -->
            <div
              class="grid-content"
              style="font-size: 18px; color: white; padding-top: 5px"
            >
              {{ date }}
            </div>
          </el-col>
        </el-row>
      </div>
    </div>

    <div class="mentree_content">
      <!-- <div class="menutree infinite-list" style="overflow:auto"> -->
      <el-scrollbar style="height: 100%">
        <el-row class="tac">
          <el-col :span="24">
            <el-menu
              :default-active="$route.path"
              @select="handleSelect"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              :default-openeds="openeds"
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
              <el-submenu index="2" class="elcatalog2">
                <template slot="title">
                  <i
                    class="el-icon-menu"
                    style="font-size: 17px; color: #870000"
                  ></i>
                  <span>专题数据管理系统</span>
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
                      ><i class="el-icon-document"></i
                      >哈勒噶提区域</el-menu-item
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
                      <i class="el-icon-folder-opened"></i>
                      <span>地震历史数据子系统</span></template
                    >
                    <el-menu-item index="1-4-1"
                      ><i class="el-icon-document"></i>选项1</el-menu-item
                    >
                  </el-submenu>
                </el-menu-item-group>
              </el-submenu>
              <el-submenu index="3" class="elcatalog3">
                <template slot="title">
                  <i
                    class="el-icon-phone"
                    style="font-size: 17px; color: #870000"
                  ></i>
                  <span>联系我们</span>
                </template>
                <el-menu-item-group>
                  <el-menu-item index="3-1" style="padding-left: 0px"
                    ><i
                      class="el-icon-user-solid"
                      style="font-size: 17px; color: #870000"
                    ></i
                    >关于我们</el-menu-item
                  >
                  <el-menu-item index="3-2" style="padding-left: 0px"
                    ><i
                      class="el-icon-message"
                      style="font-size: 17px; color: #870000"
                    ></i
                    >提供建议</el-menu-item
                  >
                  <el-menu-item index="3-3" style="padding-left: 0px"
                    ><i
                      class="el-icon-link"
                      style="font-size: 17px; color: #870000"
                    ></i
                    >友情链接</el-menu-item
                  >
                </el-menu-item-group>
              </el-submenu>
            </el-menu>
          </el-col>
        </el-row>
      </el-scrollbar>
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
      openeds: ["1"], //默认展开导航
      // 搜索框数据
      state: "", //存放所有数据库、集合的名称
      date: "您好，欢迎访问MeoGeoStore！", //当前时间
    };
  },
  mounted() {
    let _this = this; // 声明一个变量指向Vue实例this，保证作用域一致
    this.timer = setInterval(() => {
      // _this.date = new Date(); // 修改数据date
      _this.date = this.getTime(); // 修改数据date
    }, 1000);
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
    }
  },
  methods: {
    // 格式下时间
    padDate(value) {
      return value < 10 ? "0" + value : value;
    },
    getTime() {
      var date1 = new Date();
      var year = date1.getFullYear();
      var month = this.padDate(date1.getMonth() + 1);
      var day = this.padDate(date1.getDate());
      var hours = this.padDate(date1.getHours());
      var minutes = this.padDate(date1.getMinutes());
      // var seconds = date1.getSeconds();
      var seconds = this.padDate(date1.getSeconds());
      return (
        year +
        "年" +
        month +
        "月" +
        day +
        "日" +
        hours +
        ":" +
        minutes +
        ":" +
        seconds
      );
    },
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
// button.el-button.el-button--small.is-plain {
//   margin: 3px;
//   background: #870000;
// }
// 侧边主要内容
.mentree_content {
  width: 280px;
  // height: 775px;
  height: 810px;
  overflow: auto; //超出内容部分有下拉框
}
// 导航子目录
.elcatalog2 i {
  color: #870000;
}
.elcatalog2 .el-menu-item-group {
  padding-left: 20px;
}
.elcatalog2 .el-menu-item {
  padding-left: 20px !important;
  text-align: left;
  font-size: 14px;
  font-weight: bold;
  color: #870000;
}
.elcatalog3 .el-menu-item {
  padding-left: 20px !important;
  text-align: left;
  font-size: 14px;
  font-weight: bold;
  color: #870000;
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
.el-scrollbar__wrap {
  overflow-x: hidden; //设置滚动条隐藏
}
</style>