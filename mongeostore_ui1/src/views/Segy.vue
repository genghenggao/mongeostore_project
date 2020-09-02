<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-28 08:36:26
 * @LastEditors: henggao
 * @LastEditTime: 2020-08-28 17:19:32
-->
<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input
        v-model="input"
        placeholder="请输入测线号"
        style="display:inline-table; width: 30%; float:left"
      ></el-input>
      <el-button type="primary" @click="addSegy()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="segyList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template slot-scope="scope">{{ scope.row.pk }}</template>
        </el-table-column>
        <el-table-column prop="num_id" label="测线号" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.num_id }}</template>
        </el-table-column>
        <el-table-column prop="x_line" label="x_line" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.x_line }}</template>
        </el-table-column>
        <el-table-column prop="y_line" label="y_line" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.y_line }}</template>
        </el-table-column>
        <el-table-column prop="value" label="value" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.value }}</template>
        </el-table-column>
        <el-table-column prop="author" label="采集人员" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.author }}</template>
        </el-table-column>
        <el-table-column prop="creat_time" label="添加时间" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.create_time }}</template>
        </el-table-column>
        <el-table-column prop="update_time" label="更新时间" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.update_time }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "segy",
  data() {
    return {
      input: "",
      segyList: []
    };
  },
  mounted: function() {
    this.showSegys();
  },
  methods: {
    addSegy() {
      this.$http
        .get("http://127.0.0.1:8000/api/add_segy?num_id=" + this.input)
        .then(response => {
          var res = JSON.parse(response.bodyText);
          if (res.error_num === 0) {
            this.showSegys();
          } else {
            this.$message.error("新增数据失败，请重试");
            console.log(res["msg"]);
          }
        });
    },
    showSegys() {
      this.$http.get("http://127.0.0.1:8000/api/show_segys").then(response => {
        var res = JSON.parse(response.bodyText);
        console.log(res);
        if (res.error_num === 0) {
          this.segyList = res["list"];
        } else {
          this.$message.error("查询数据失败");
          console.log(res["msg"]);
        }
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>


