<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-04 17:05:21
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-08 22:25:56
-->
<template>
  <div class="DataShow">
    <SearchData />
    <el-table
      class="tb-edit"
      highlight-current-row
      :data="
        tableData.slice((currentPage - 1) * PageSize, currentPage * PageSize)
      "
      style="width: 100%"
      max-height="740"
      :default-sort="{ prop: 'ZK_num', order: 'ZK_num' }"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column
        fixed="left"
        label="ZK_num"
        prop="ZK_num"
        width="80"
        :filters="[
          { text: 'ZK1', value: 'ZK1' },
          { text: 'ZK2', value: 'ZK2' },
          { text: 'ZK3', value: 'ZK3' },
          { text: 'ZK4', value: 'ZK4' }
        ]"
        :filter-method="filterHandler"
      ></el-table-column>
      <template v-for="(col, index) in cols">
        <el-table-column
          v-if="col.ZK_num === 'normal'"
          :key="index"
          :prop="col.prop"
          :label="col.label"
        ></el-table-column>
        <el-table-column
          v-if="col.ZK_num === 'sort'"
          :key="col.ZK_num"
          :prop="col.prop"
          sortable
          :label="col.label"
        >
          <template slot-scope="scope">
            <el-tag type="primary">{{ scope.row.ZK_num }}</el-tag>
          </template>
        </el-table-column>
      </template>
      <el-table-column fixed="right" label="操作" width="160">
        <template slot-scope="scope">
          <el-button
            type="primary"
            plain
            size="mini"
            @click="handleEdit(scope.$index, scope.row)"
            >编辑</el-button
          >
          <el-button
            @click.native.prevent="deleteRow(scope.$index, tableData)"
            type="danger"
            plain
            size="mini"
          >
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="pageSizes"
        :page-size="PageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="totalCount"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SearchData from "@/components/SearchData.vue";
export default {
  name: "Data",
  components: { SearchData },
  data() {
    return {
      // cols prop属性值都是作为 tableData的属性
      cols: [
        { label: "节点编号_id", prop: "_id.$oid", nickname: "normal" },
        { label: "名称nickname", prop: "nickname", nickname: "sort" },
        { label: "类型combat", prop: "combat", nickname: "normal" },
        { label: "状态level", prop: "level", nickname: "normal" },
        { label: "坐标rid", prop: "rid", nickname: "normal" },
        // { label: "rid", prop: "_id.$oid", ZK_num: "normal" },
        // { label: "ZK_num", prop: "ZK_num", ZK_num: "normal" },
        // { label: "Depth", prop: "Depth", ZK_num: "sort" },
        // { label: "Azimuth", prop: "Azimuth", ZK_num: "normal" },
        // { label: "Inclination", prop: "Inclination", ZK_num: "normal" }
      ],
      //   表格数据
      tableData: [
        {
          node: "0051",
          name: " 机库顶",
          type: "UWB",
          status: "正常",
          coordinate: "12.21,34.45,34.6"
        },
        {
          node: "0061",
          name: "机库门",
          type: "GPS",
          status: "低电",
          coordinate: "45.41,67.45,78.6"
        },
        {
          node: "0061",
          name: "机库门",
          type: "GPS",
          status: "低电",
          coordinate: "45.41,67.45,78.6"
        }
      ],
      // 分页数据，默认第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 400,
      // 个数选择器（可修改）
      pageSizes: [10, 20, 30, 40],
      // 默认每页显示的条数（可修改)
      PageSize: 9,
      // 搜索
      search: ""
    };
  },
  created() {
    this.showData();
  },
  methods: {
    // 选择框
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    // 排序
    filterHandler(value, row, column) {
      const property = column["property"];
      return row[property] === value;
    },
    // 编辑按钮
    handleEdit(index, row) {
      console.log(index, row);
    },
    // 删除按钮
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    handleCurrentChange(row, event, column) {
      console.log(row, event, column, event.currentTarget);
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    showData(n1, n2) {
      const url = "http://127.0.0.1:8000/load/showdata/";
      axios
        .get(url, {
          orgCode: 1,
          // 每页显示的条数
          PageSize: n1,
          // 显示第几页
          currentPage: n2
        })
        .then(response => {
          // var res = JSON.parse(response.bodyText);
          console.log(response);
          console.log(response.data);
          console.log("取到单个数据");
          console.log(typeof response.data);
          // let detailsnew = JSON.parse(JSON.stringify(this.detailslist));
          // var datatset = [];
          // datatset.push(response.data);
          // console.log(typeof datatset);
          // console.log(datatset);
          // datatset = response.data
          // console.log(datatset)
          // console.log(this.tableData)
          // console.log(typeof this.tableData)
          // this.tableData = datatset;
          // 将数据赋值给tableData
          this.tableData = response.data;
          this.searchCondition = response.data;
          // 分页所需信息
          // 将数据的长度赋值给totalCount
          this.totalCount = response.data.length;

          console.log(this.tableData);
          console.log(typeof this.tableData);
          // 获取字段信息
          // this.cols = ""
          let tmp = response.data[0];
          console.log(tmp);
          var listcol = [];
          for (var key in tmp) {
            //  { label: "节点编号_id", prop: "_id.$oid", nickname: "normal" },
            //   console.log(key);
            //   console.log(typeof key);
            // console.log(key[1])
            listcol.push({
              label: key,
              prop: key,
              ZK_num: "normal"
            });
          }
          // console.log(listcol);
          listcol[0].prop = "_id.$oid"; //_id是一个对象，取值
          // listcol[6].nickname = "sort"; //按字段设置排序
          console.log(listcol)
          listcol[1].ZK_num = "sort"; //按字段设置排序
          this.cols = listcol;
        });
    },
    // 分页
    // 每页显示的条数
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      // 改变每页显示的条数
      this.PageSize = val;
      // 点击每页显示的条数时，显示第一页
      this.showData(val, 1);
      // 注意：在改变每页显示的条数时，要将页码显示到第一页
      this.currentPage = 1;
    },
    // 显示第几页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      // 改变默认的页数
      this.currentPage = val;
      // 切换页码时，要获取每页显示的条数
      this.showData(this.PageSize, val * this.pageSize);
    }
  }
};
</script>


<style lang="less" scoped>
.DataShow {
  height: 720px;
  // height: 70px;
}
</style>