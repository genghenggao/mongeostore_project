<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-27 16:37:40
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-27 20:34:42
-->
<template>
  <el-container>
    <el-header><h2>钻孔元数据</h2></el-header>
    <el-main>
      <div>
        <el-table
          :data="
            tableData.filter(
              (data) =>
                !search ||
                data.filename.toLowerCase().includes(search.toLowerCase())
            )
          "
          style="width: 100%"
        >
          <el-table-column label="文件ID" prop="_id"> </el-table-column>
          <el-table-column label="文件名" prop="filename"> </el-table-column>
          <el-table-column label="文件大小" prop="length"> </el-table-column>
          <el-table-column label="文件类型" prop="contentType">
          </el-table-column>
          <el-table-column label="上传人员" prop="publisher"> </el-table-column>
          <el-table-column label="上传时间" prop="uploadDate">
          </el-table-column>
          <el-table-column label="备注" prop="aliases"> </el-table-column>
          <el-table-column label="展示" prop=""
            ><el-image
              style="width: 100px; height: 100px"
              :src="imgurl"
              :preview-src-list="srcList"
            >
            </el-image>
          </el-table-column>
          <el-table-column align="right">
            <!-- <template slot="header" slot-scope="scope"> -->
            <template slot="header" slot-scope="{}">
              <el-input
                v-model="search"
                size="mini"
                placeholder="输入文件名搜索"
              />
            </template>
            <template slot-scope="scope">
              <el-button
                size="mini"
                type="primary"
                plain
                @click="handleDown(scope.$index, scope.row)"
                >Down</el-button
              >
              <el-button
                size="mini"
                type="danger"
                plain
                @click="handleDelete(scope.$index, scope.row)"
                >Delete</el-button
              >
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!-- 分页 -->
      <div class="block" style="overflow: hidden">
        <el-pagination
          small
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page.sync="currentPage"
          :page-sizes="pageSizes"
          :page-size="PageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="totalCount"
        >
        </el-pagination>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import axios from "axios";
export default {
  name: "InclinationMeta",
  data() {
    return {
      tableData: [
        {
          _id: "xxxxxxxxxxx.xxxxx",
          filename: "钻孔1",
          length: "5MB",
          contentType: "jpg",
          publisher: "publisher",
          uploadDate: "2016-05-02",
          aliases: "xx工区",
        },
        {
          _id: "xxxxxxxxxxx.xxxxx",
          filename: "钻孔1",
          length: "5MB",
          contentType: "jpg",
          publisher: "publisher",
          uploadDate: "2016-05-02",
          aliases: "xx工区",
        },
        {
          _id: "xxxxxxxxxxx.xxxxx",
          filename: "钻孔1",
          length: "5MB",
          contentType: "jpg",
          publisher: "publisher",
          uploadDate: "2016-05-02",
          aliases: "xx工区",
        },
      ],
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
    this.showMetaData(this.PageSize, this.currentPage);
  },
  methods: {
    showMetaData(n1, n2) {
      let url = "http://127.0.0.1:8000/load/commonmetashow/";
      axios
        .get(url, {
          params: {
            // 每页显示的条数
            PageSize: n1,
            // 显示第几页
            currentPage: n2,
          },
        })
        .then((res) => {
          console.log("success");
          console.log(res.data);
        })
        .catch((err) => {
          console.log("err");
        });
    },
    handleDown(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
      // 添加确认删除框
      this.$confirm("永久删除，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 删除操作
          rows.splice(index, 1);
          let json_data = JSON.stringify(row);
          console.log(json_data);
          const url = "http://127.0.0.1:8000/load/deleteinclination/";
          axios
            .post(
              url,
              {
                json_data,
                // 设置上传到后端的数据库和集合名称
                colname: this.$store.state.title_message,
                dbname: this.$store.state.temp_database,
              },
              {
                headers: {
                  "Content-Type": "application/x-www-form-urlencoded",
                },
              }
            )
            .then((res) => {
              console.log("删除成功");
              // 重新获取用户列表数据
              // this.showData();
              //通过flag判断,刷新数据
              if (!this.flag) {
                this.showData(this.PageSize, this.currentPage);
              } else {
                this.onSearchSubmit(this.PageSize, this.currentPage);
              }
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消删除",
          });
        });
    },
    //   分页
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      // 改变每页显示的条数
      this.PageSize = val;
      this.showData(val, 1); // this.pageSize是undefined，使用选定的或默认值
      // 注意：在改变每页显示的条数时，要将页码显示到第一页
      this.currentPage = 1;
    },
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      this.showMetaData(this.PageSize, val);
    },
  },
};
</script>