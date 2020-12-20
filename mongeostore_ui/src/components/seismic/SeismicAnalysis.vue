<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-17 22:25:22
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-20 23:04:48
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
            <el-button type="goon" size="medium" plain>上传数据</el-button
            ><el-button type="goon" size="medium" plain>云端数据</el-button>
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

      <div style="height: 600px; width: 835px">
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
          <div style="text-align: left; display: flex">
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
        </el-card>
      </div>
    </el-container>
  </el-container>
</template>

<script>
import axios from "axios";
export default {
  name: "SeismicAnalysis",
  data() {
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
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 删除文件
    handleDelete(index, rows, row) {
      // console.log(index, rows, row);
      console.log(row.filename);
      rows.splice(index, 1);
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
      let this_url = "http://127.0.0.1:8000/seismic/seismicheaderquery/";
      axios({
        method: "GET",
        url: this_url,
        params: { filename: this.seismic_message, queryparams: val },
      })
        .then((res) => {
          console.log(res);
          console.log(res.data);
          this.seismic_info = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
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

.analysis_content::-webkit-scrollbar {
  width: 6px; // 横向滚动条

  height: 6px; // 纵向滚动条 必写
}
.analysis_content::-webkit-scrollbar-thumb {
  background-color: rgba(119, 158, 194, 0.829);

  border-radius: 3px;
}
</style>