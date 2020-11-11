<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-06 15:35:53
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-11 10:06:20
-->
<template>
  <el-table :data="tableData" @cell-dblclick="handle" style="width: 100%">
    <el-table-column prop="date" label="日期" width="180">
      <template slot-scope="scope">
        <div v-if="!scope.row.isEdit">{{ scope.row.date }}</div>
        <div v-else>
          <el-input v-model="scope.row.date"></el-input>
        </div>
      </template>
    </el-table-column>
    <el-table-column prop="name" label="姓名" width="180">
      <template slot-scope="scope">
        <div v-if="!scope.row.isEdit">{{ scope.row.name }}</div>
        <div v-else>
          <el-input v-model="scope.row.name"></el-input>
        </div>
      </template>
    </el-table-column>
    <el-table-column prop="address" label="地址"> </el-table-column>
    <el-table-column label="按钮">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)">{{
          scope.row.isEdit ? "完成" : "编辑"
        }}</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          date: "2016-05-02",
          name: "王小虎1",
          address: "上海市普陀区金沙江路 1518 弄"
        },
        {
          date: "2016-05-04",
          name: "王小虎2",
          address: "上海市普陀区金沙江路 1517 弄"
        },
        {
          date: "2016-05-01",
          name: "王小虎3",
          address: "上海市普陀区金沙江路 1519 弄"
        },
        {
          date: "2016-05-03",
          name: "王小虎4",
          address: "上海市普陀区金沙江路 1516 弄"
        }
      ]
    };
  },
  methods: {
    handleClick(row) {
      // 动态设置数据并通过这个数据判断显示方式
      if (row.isEdit) {
        this.$delete(row, "isEdit");
      } else {
        this.$set(row, "isEdit", true);
      }
      console.log(this.tableData);
    },
    handle(row, column, cell, event) {}
  }
};
</script>

<style scoped>
.el-input {
  width: 100%;
}
</style>