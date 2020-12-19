<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-17 22:25:22
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-19 23:05:00
-->
<template>
  <el-container>
    <el-header> <h2>地震数据解析</h2></el-header>
    <el-container>
      <div
        class="left_aside"
        style="border: 2px dashed rgb(54, 92, 150); width: 300px; height: 700px"
      >
        <div>当前可以解析的数据如下：</div>
        <div></div>
        <div>
          <el-button type="primary" size="medium" plain >上传数据</el-button
          ><el-button type="primary" size="medium" plain>云端数据</el-button>
        </div>
        <div>
          <el-table
            :data="
              tableData.filter(
                (data) =>
                  !search ||
                  data.name.toLowerCase().includes(search.toLowerCase())
              )
            "
            style="width: 100%"
          >
            <el-table-column label="Name" prop="name"> </el-table-column>
            <el-table-column align="right">
              <template slot="header" slot-scope="">
                <el-input
                  v-model="search"
                  size="mini"
                  placeholder="输入关键字搜索"
                />
              </template>
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)"
                  >Delete</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>

      <div style="background: #c4d8c485; height: 700px; width: 1040px"></div>
      <div style="background: #98b9d68c; height: 700px; width: 300px"></div>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: "SeismicAnalysis",
  data() {
    return {
      tableData: [
        {
          name: "王小虎",
        },
        {
          name: "王小虎",
        },
        {
          name: "王小虎",
        },
        {
          name: "王小虎",
        },
      ],
      search: "",
    };
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
  },
};
</script>

<style lang = 'scss' scoped>
</style>