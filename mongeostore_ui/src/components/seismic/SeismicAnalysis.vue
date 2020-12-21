<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-17 22:25:22
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-21 17:36:10
-->
<template>
  <el-container>
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
        <i class="el-icon-caret-right" /> 地震数据解析
      </h2></el-header
    >
    <el-container>
      <div class="left_aside" style="width: 500px; height: 750px">
        <el-card shadow="hover" style="">
          <div class="mian_file_title" style="text-align: left; height: 50px">
            <h5 style="color: #810000">
              <i class="el-icon-document-checked"></i> 当前可以解析的数据如下：
            </h5>
          </div>
          <div class="main_file_button" style="text-align: left; display: flex">
            <h5 style="padding-top: 6px; color: #810000">选择：</h5>
            <el-button
              type="goon"
              size="medium"
              plain
              @click="centerDialogVisible = true"
              >上传数据</el-button
            ><el-button
              type="goon"
              size="medium"
              plain
              @click="cloudDialogVisible = true"
              >云端数据</el-button
            >
            <el-button type="goon" size="medium" plain @click="refreshtable"
              >刷新表格</el-button
            >
          </div>
          <div>
            <el-table
              :data="
                tableData.filter(
                  (data) =>
                    !search ||
                    data.filename.toLowerCase().includes(search.toLowerCase())
                )
              "
              height="620"
              style="width: 100%"
            >
              <el-table-column type="expand">
                <template slot-scope="props">
                  <el-form
                    label-position="left"
                    inline
                    class="demo-table-expand"
                  >
                    <el-form-item label="文件名称">
                      <span>{{ props.row.filename }}</span>
                    </el-form-item>
                    <el-form-item label="文件大小">
                      <span>{{ props.row.filesize }}</span>
                    </el-form-item>
                    <el-form-item label="修改时间">
                      <span>{{ props.row.upload_time }}</span>
                    </el-form-item>
                  </el-form>
                </template>
              </el-table-column>
              <el-table-column type="index" width="45"> </el-table-column>
              <el-table-column label="文件名" prop="filename">
              </el-table-column>

              <el-table-column align="right">
                <template slot="header" slot-scope="{}">
                  <el-input
                    v-model="search"
                    size="small"
                    placeholder="输入关键字搜索"
                  />
                </template>
                <template slot-scope="scope">
                  <el-button
                    size="mini"
                    type="danger"
                    plain
                    @click="handleDelete(scope.$index, tableData, scope.row)"
                    >删除</el-button
                  >
                  <el-button
                    size="mini"
                    type="primary"
                    plain
                    @click="seismicanalysic(scope.$index, tableData, scope.row)"
                    >解析</el-button
                  >
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-card>
      </div>

      <div style="height: 600px; width: 835px; min-width: 820px">
        <el-card shadow="hover" style="height: 750px">
          <div>
            <h5 style="color: #810000; text-align: left">
              <i class="el-icon-video-play"></i> 正在解析数据：{{
                seismic_message
              }}
            </h5>
          </div>
          <div class="analysis_content" style="height: 700px; overflow: auto">
            <pre>{{ seismic_info }}</pre>
          </div>
        </el-card>
      </div>
      <div style="height: 600px; width: 300px">
        <el-card shadow="hover" style="height: 750px">
          <div>
            <h5 style="color: #810000; text-align: left">
              <i class="el-icon-setting"></i> 解析数据工具：
            </h5>
          </div>
          <div style="text-align: left; display: flex">
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'header'))"
              >卷头</el-button
            >
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'track'))"
              >道头</el-button
            >
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'traces'))"
              >Traces</el-button
            >
          </div>
          <div style="text-align: left; display: flex; padding-top: 5px">
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'Bin'))"
              >Bin</el-button
            >
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'trace1'))"
              >第一道</el-button
            >
            <el-button
              type="goon"
              size="medium"
              plain
              @click="queryHeader((val = 'trace_1'))"
              >最后一道</el-button
            >
          </div>
          <div style="padding-top: 5px">
            <el-form
              ref="seismicform"
              :model="seismicform"
              :rules="seismicformrules"
              style="
                display: flex;
                height: 40px;
                width: 240px;
                background: #51abce;
                border-radius: 5px;
              "
            >
              <el-form-item
                label-width="70px"
                label="第N道"
                style="
                  width: 165px;
                  background: #51abce;
                  height: 40px;
                  border-radius: 5px;
                "
              >
                <el-input
                  v-model="seismicform.trace"
                  placeholder="0-n"
                  @keyup.enter.native="queryHeader((val = seismicform.trace))"
                ></el-input>
              </el-form-item>
              <el-form-item style="width: 50px">
                <el-button
                  type="goon"
                  @click="queryHeader((val = seismicform.trace))"
                  >查询</el-button
                >
              </el-form-item>
            </el-form>
          </div>
        </el-card>
      </div>
      <el-dialog
        title="请上传需要解析的文件"
        :visible.sync="centerDialogVisible"
        width="30%"
        center
      >
        <AnalysisUploadFile />

        <span slot="footer" class="dialog-footer">
          <el-button @click="centerDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="makesuretable">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="请上传需要解析的文件"
        :visible.sync="cloudDialogVisible"
        width="30%"
        center
      >
        <AnalysisCloudData />

        <span slot="footer" class="dialog-footer">
          <el-button @click="cloudDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="makesuretable">确 定</el-button>
        </span>
      </el-dialog>
    </el-container>
  </el-container>
</template>

<script>
import axios from "axios";
import qs from "qs";
import plupload from "plupload";
import { stringify } from "qs";
import AnalysisUploadFile from "@/components/seismic/AnalysisUploadFile.vue";
import AnalysisCloudData from "@/components/seismic/AnalysisCloudData.vue";
export default {
  name: "SeismicAnalysis",
  components: {
    AnalysisUploadFile,
    AnalysisCloudData,
  },
  data() {
    // 校验表单trace
    var checkTrace = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("Trace不能为空"));
      }
      setTimeout(() => {
        var re = /^[0-9]*/; //判断字符串是否为数字
        if (!re.test(value)) {
          callback(new Error("请输入数字值"));
        } else {
          callback();
        }
      }, 500);
    };
    return {
      tableData: [
        {
          filename: "LX_SEGY001",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY002",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY003",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY004",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY005",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY006",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY007",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY008",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY009",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY010",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
        {
          filename: "LX_SEGY011",
          filesize: "1.24G",
          upload_time: "2018-12-1",
        },
      ],
      search: "", //搜索框
      seismic_message: "LX_SEGY001", //文件名称
      seismic_info: "", //地震解析数据
      // 表单数据
      seismicform: {
        trace: "",
      },
      // 校验表单数据
      seismicformrules: {
        trace: [{ validator: checkTrace, trigger: "blur" }],
      },
      // 上传弹出框
      centerDialogVisible: false,
      cloudDialogVisible: false,
    };
  },
  created() {
    this.showSeismicFile();
  },

  methods: {
    // 展示文件夹数据
    showSeismicFile() {
      let this_url = "http://127.0.0.1:8000/seismic/seismicfileread/";
      axios({ method: "GET", url: this_url, params: {} })
        .then((res) => {
          console.log(res);
          console.log(res.data);
          this.tableData = res.data;
          // 设置默认解析文件，这里社第一个文件
          let temp_data = res.data[0];
          this.seismic_message = temp_data["filename"];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 删除文件
    handleDelete(index, rows, row) {
      // console.log(index, rows, row);
      console.log(row.filename);

      // let json_data = JSON.stringify(row);
      let data = { filename: row.filename };
      rows.splice(index, 1);
      let this_url = "http://127.0.0.1:8000/seismic/Seismicanalysisdelete/";
      axios({
        method: "POST",
        url: this_url,
        data: qs.stringify(data),
        // data: {json_data} ,
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        // headers: { "Content-Type": "application/json" },
      })
        .then((res) => {
          console.log("success");
        })
        .catch((err) => {
          console.log("err");
        });
    },
    // 解析文件
    seismicanalysic(index, rows, row) {
      console.log(index, row);
      console.log(row.filename);
      this.seismic_message = row.filename;
    },
    // 查询卷头信息
    queryHeader(val) {
      console.log(this.seismic_message);
      console.log(val);
      let this_url = "http://127.0.0.1:8000/seismic/seismicheaderquery/";
      axios({
        method: "GET",
        url: this_url,
        params: { filename: this.seismic_message, queryparams: val },
      })
        .then((res) => {
          // console.log(res);
          // console.log(res.data);
          // console.log(this.val);
          if (this.val == "header" || this.val == "Bin") {
            // console.log("yes");
            let jsondata = eval("(" + res.data + ")");
            // console.log(jsondata);
            // this.seismic_info = res.data;
            this.seismic_info = jsondata;
          } else {
            // console.log("no");
            this.seismic_info = res.data;
          }
        })
        .catch((err) => {
          // console.log(err);
          this.$message.error("Sorry，文件无法解析，请检查文件正确性！");
        });
    },
    // 上传服务器文件
    // 确定按钮
    makesuretable() {
      this.centerDialogVisible = false;
      this.cloudDialogVisible = false;

      this.showSeismicFile();
    },
    // 刷新表格
    refreshtable() {
      this.showSeismicFile();
    },
  },
};
</script>

<style lang='scss' scoped>
// 按钮样式
.el-button--goon.is-active,
.el-button--goon:active {
  background: #51abce;
  border-color: #20b2aa;
  color: #fff;
}

.el-button--goon:focus,
.el-button--goon:hover {
  background: #48d1cc;
  border-color: #48d1cc;
  color: #fff;
}

.el-button--goon {
  color: #fff;
  background-color: #51abce;
  border-color: #20b2aa;
}

//表格滚动条的宽度
::v-deep .el-table__body-wrapper::-webkit-scrollbar {
  width: 6px; // 横向滚动条

  height: 6px; // 纵向滚动条 必写
}

// 表格滚动条的滑块
::v-deep .el-table__body-wrapper::-webkit-scrollbar-thumb {
  background-color: rgba(119, 158, 194, 0.829);

  border-radius: 3px;
}
// 表格样式
::v-deep .demo-table-expand {
  font-size: 0;
}
::v-deep .demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
::v-deep .demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 80%;
}
// 主要内容滚动条
.analysis_content::-webkit-scrollbar {
  width: 6px; // 横向滚动条

  height: 6px; // 纵向滚动条 必写
}
.analysis_content::-webkit-scrollbar-thumb {
  background-color: rgba(119, 158, 194, 0.829);

  border-radius: 3px;
}

// 解析工具表单
// 表单label
::v-deep .el-form-item__label {
  color: #ffffff;
  // padding: 0;
}
// 按钮位置
// ::v-deep .el-form-item__content {
//   margin-left: 10px;
// }
::v-deep .el-form-item__content {
  margin-left: 5px;
}
</style>