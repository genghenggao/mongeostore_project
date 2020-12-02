<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-27 16:37:40
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-02 18:45:49
-->
<template>
  <el-container style="min-width: 1100px; overflow: hidden">
    <el-header>
      <h2
        style="
          font-size: 30px;
          padding-top: 10px;
          color: #870000;
          min-width: 1100px;
          overflow: hidden;
          text-align: left;
        "
      >
        <i class="el-icon-caret-right" /> 钻孔编号：{{ ZK_num }}
      </h2>
    </el-header>
    <el-main style="padding-top: 10px; min-width: 1100px; overflow-y: hidden">
      <!-- <div style="">
        <h3>钻孔编号：{{ ZK_num }}</h3>
      </div> -->
      <el-row :gutter="20" style="margin: 0">
        <el-col :span="16" :offset="4">
          <el-tabs :tab-position="tabPosition">
            <el-tab-pane label="钻孔信息">
              <div class="drillinfo" style="min-width: 900px">
                <table style="width: 100%" class="myTable">
                  <el-scrollbar style="height: 700px">
                    <!-- 滚动条 -->
                    <tr v-for="(value, keyword) in tableData" :key="keyword">
                      <div v-if="keyword == '钻孔柱状图'">
                        <td class="column" style="">钻孔柱状图</td>
                        <td class="column">
                          <!-- <el-image
                            style="width: 60px; height: 60px"
                            :src="url"
                            :preview-src-list="srcList"
                          >
                          </el-image> -->
                          <img
                            :src="'data:image/png;base64,' + ico"
                            class="avatar"
                            height="60"
                            alt="图片名"
                            v-viewer
                          />
                        </td>
                      </div>
                      <div v-else>
                        <td class="column">{{ keyword }}</td>
                        <td class="column">{{ value }}</td>
                      </div>
                    </tr>
                  </el-scrollbar>
                </table>
              </div>
            </el-tab-pane>
            <el-tab-pane label="项目信息"
              ><div>
                <table style="width: 100%" class="myTable">
                  <el-scrollbar style="height: 700px">
                    <tr
                      v-for="(value, keyword) in ProjectInformation"
                      :key="keyword"
                    >
                      <td class="column">{{ keyword }}</td>
                      <td class="column">{{ value }}</td>
                    </tr>
                  </el-scrollbar>
                </table>
              </div></el-tab-pane
            >
            <el-tab-pane label="单位信息"
              ><div>
                <table style="width: 100%" class="myTable">
                  <el-scrollbar style="height: 700px">
                    <tr
                      v-for="(value, keyword) in FileInformation"
                      :key="keyword"
                    >
                      <td class="column">{{ keyword }}</td>
                      <td class="column">{{ value }}</td>
                    </tr>
                  </el-scrollbar>
                </table>
              </div></el-tab-pane
            >
            <el-tab-pane label="其他信息">其他信息</el-tab-pane>
          </el-tabs>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from "axios";
export default {
  name: "DrillDetails",
  data() {
    return {
      ico: "",
      _id: "o_1eoekb1rb5191s631sp871115ccd",
      ZK_num: "ZK1", //小标题
      tabPosition: "right", //标签页位置设置
      tableData: {
        钻孔编号: "	ZK1",
        // 钻孔柱状图: "浏览",
        钻孔柱状图: "浏览",
        原始资料档号: "2010091",
        勘探线号: "1-1",
        钻孔名称: "ZK2",
        钻孔类型: "灾害地质勘查钻孔",
        钻孔位置: "广元市剑阁县上寺乡",
        孔口高程H: "608.6",
        终孔深度Z: "	16.94",
        终孔日期: "2010/4/2",
        施工单位: "重庆长江工程勘察设计研究院",
        测井报告: "无",
        原始地质记录表: "有",
        钻孔岩心: "无",
      },
      ProjectInformation: {
        钻孔编号: "	ZK2",
        项目名称: "广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查",
        资料名称: "广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查报告",
        成果资料档号: "	aa548",
        项目结束时间: "	2010/4/25",
      },
      FileInformation: {
        钻孔编号: "	ZK2",
        上传人员: "ghg",
        上传日期: "2020/11/11",
        单位名称: "中国矿业大学（北京）",
        通讯地址: "北京市海淀区学院路丁11号",
      },

      search: "", //搜索框
      // 分页数据，默认第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 100,
      // 个数选择器（可修改）
      pageSizes: [10, 20, 50, 100],
      // 默认每页显示的条数（可修改)
      PageSize: 10,
      //   图片
      imgurl:
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      srcList: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
        "https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg",
      ],
    };
  },
  created() {
    this.showMetaData();
    // this.ZK_num = this.$route.params._id;
    // this.tableData = JSON.parse(JSON.stringify(this.tableData));
  },
  methods: {
    showMetaData() {
      console.log(this.$route.params._id); //查看DrillMetaData.vue路由传过来的参数
      // console.log(typeof this.tableData);
      // console.log(this.tableData);
      let url = "http://127.0.0.1:8000/load/drillhistogram/";
      axios
        .get(url, {
          // responseType: "arraybuffer",
          params: {
            // 每页显示的条数
            // PageSize: n1,
            // 显示第几页
            // currentPage: n2,
            _id: this.$route.params._id,
          },
        })
        .then((res) => {
          // console.log(res.data);
          let end_data = res.data[0];
          // console.log(end_data["pic_data"]);
          let pic_data = end_data["pic_data"];
          // console.log(pic_data["$binary"]);
          // // end_data.splice(0,1)
          delete end_data["pic_data"]; //删除pic_data这一项,使用splice\shift方法不行
          this.tableData = end_data;
          console.log(end_data);
          this.ico = pic_data["$binary"];
          this.ZK_num = end_data["钻孔编号"];
          // let imgUrl =
          //   "data:image/png;base64," +
          //   btoa(
          //     new Uint8Array(res.data.data).reduce(
          //       (data, byte) => data + String.fromCharCode(byte),
          //       ""
          //     )
          //   );
          // this.imgUrl = imgUrl;
        })
        .catch((err) => {
          console.log("err");
        });
    },
  },
};
</script>

<style  lang='scss'>
.myTable {
  border-collapse: collapse;
  margin: 0 auto;
  text-align: center;
}

.myTable td,
.myTable th {
  border: 1px solid #cad9ea;
  color: #666;
  height: 60px;
  width: 450px;
  padding-top: 20px; //设置文字居中
  padding-bottom: 20px;
}
.el-scrollbar__wrap {
  overflow-x: hidden; //设置滚动条隐藏
}
</style>