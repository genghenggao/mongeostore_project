<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-04 17:05:21
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-10 23:10:00
-->
<template>
  <div class="DataShow">
    <el-container>
      <el-header class="data_search">
        <!-- 搜索和添加功能 -->
        <!-- <h5>1：5万</h5> -->
        <!--搜索头 开始-->
        <el-form :inline="true" :model="tableData" class="demo-form-inline">
          <el-form-item class="header_key_world" label="关键字:">
            <el-input
              v-model="tableData.ZK_num"
              suffix-icon="el-icon-date"
              placeholder="请输入关键字"
            ></el-input>
          </el-form-item>
          <el-form-item id="submit-item">
            <el-button
              type="info"
              plain
              icon="el-icon-search"
              @click="onSearchSubmit"
              >查询</el-button
            >
          </el-form-item>
          <el-form-item id="addNew-item">
            <el-button
              type="info"
              plain
              icon="el-icon-edit"
              @click="addNewHandler"
              >新增</el-button
            >
          </el-form-item>
        </el-form>
        <!--搜索头 结束-->
        <!-- <SearchData /> -->
      </el-header>
      <el-main class="data_content">
        <div class="data_table">
          <!-- 注意里面max-height字段设置高度 -->
          <el-table
            class="tb-edit"
            highlight-current-row
            :data="
              tableData.slice(
                (currentPage - 1) * PageSize,
                currentPage * PageSize
              )
            "
            style="width: 100%"
            max-height="690px"
            :default-sort="{ prop: 'Depth', order: 'Depth' }"
            @selection-change="handleSelectionChange"
          >
            <!-- 选择框设置 -->
            <el-table-column type="selection" width="55"> </el-table-column>
            <!-- 添加_id字段 -->
            <el-table-column label="_id" prop="_id.$oid"> </el-table-column>
            <!-- 筛选字段 filters,这只是筛选当页的-->
            <el-table-column
              fixed="left"
              label="ZK_num"
              prop="ZK_num"
              width="100"
              :filters="filter_data"
              :filter-method="filterHandler"
            ></el-table-column>
            <!-- 生成关键词 -->
            <!-- <template v-for="(col, index) in cols"> -->
            <template v-for="col in cols">
              <!-- 设置排序字段 -->
              <el-table-column
                v-if="col.Depth === 'normal'"
                :key="col._id"
                :prop="col.prop"
                :label="col.label"
                align="center"
              >
                <!-- 每一行数据 -->
                <template slot-scope="scope">
                  <div v-if="!scope.row.isEdit">{{ scope.row[col.prop] }}</div>
                  <div v-else>
                    <el-input v-model="scope.row[col.prop]"></el-input>
                  </div>
                </template>
              </el-table-column>
              <el-table-column
                v-if="col.Depth === 'sort'"
                :key="col._id"
                :prop="col.prop"
                sortable
                :label="col.label"
              >
                <template slot-scope="scope">
                  <!-- 生成标签 -->
                  <el-tag type="primary">{{ scope.row.Depth }}</el-tag>
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
                  >{{ scope.row.isEdit ? "保存" : "编辑" }}</el-button
                >
                <el-button
                  @click.native.prevent="
                    deleteRow(scope.$index, tableData, scope.row)
                  "
                  type="danger"
                  plain
                  size="mini"
                >
                  删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <!-- 分页 -->
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
        <!-- 下面这个用来设置点击添加按钮的弹出框，里面可以进行嵌套表格来展示弹出的表格信息,使用下面的:visible.sync来控制显示与否。里面绑定的是我们新设置的值，填写完成后，将我们这个新值塞到页面中所有的数据当中去  -->
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
// import SearchData from "@/components/SearchData.vue";
export default {
  name: "Data",
  components: {
    // SearchData
  },
  data() {
    return {
      // cols prop属性值都是作为 tableData的属性
      cols: [
        { label: "节点编号_id", prop: "_id.$oid", nickname: "normal" },
        { label: "名称nickname", prop: "nickname", nickname: "sort" },
        { label: "类型combat", prop: "combat", nickname: "normal" },
        { label: "状态level", prop: "level", nickname: "normal" },
        { label: "坐标rid", prop: "rid", nickname: "normal" }
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
      // 筛选字段
      filter_data: [
        { text: "ZK1", value: "ZK1" },
        { text: "ZK2", value: "ZK2" },
        { text: "ZK3", value: "ZK3" },
        { text: "ZK4", value: "ZK4" }
      ],
      // 分页数据，默认第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 400,
      // 个数选择器（可修改）
      pageSizes: [10, 20, 30, 40],
      // 默认每页显示的条数（可修改)
      PageSize: 10,
      // 搜索
      input_data: "",
      select: ""
      // 搜索条件
      // searchCondition: {
      //   nickname: "",
      //   vip: "",
      //   dateVal: ""
      // }
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
    // 开始搜索
    onSearchSubmit() {
      // this.initAdminList(1);
      console.log(this.tableData.ZK_num);
    },
    // 添加数据
    addNewHandler() {
      this.addNew.visible = true;
    },
    // 编辑（修改）按钮
    handleEdit(index, row) {
      // console.log(index, row);
      // 动态设置数据并通过这个数据判断显示方式
      if (row.isEdit) {
        // 点击保存的
        this.$delete(row, "isEdit");
        // console.log("开始delete");
        // console.log(index, row); //把row发送给后端
        // console.log(row["_id"]["$oid"]); //把row发送给后端
        // row["id"] = row["_id"]["$oid"];
        // row["help_param"] = "help_param"; //用于解决后端smscode参数为3019"}多了"}问题
        // let postData = qs.stringify(row); // w为了解决后端拿不到数据问题
        // postData["_id"] = row["_id"]["$oid"];
        // console.log(typeof postData);
        // console.log(row["id"]);
        let json_data = JSON.stringify(row);

        const url = "http://127.0.0.1:8000/load/editdata/";
        axios
          .post(
            url,
            {
              // data: JSON.stringify(row) //data用于post请求
              json_data
            },
            {
              headers: { "Content-Type": "application/x-www-form-urlencoded" }
            }
            // console.log(postData)
          )
          .then(res => {
            console.log("编辑成功");
          });
      } else {
        // 点击编辑
        this.$set(row, "isEdit", true);
        // console.log("开始set");
        // console.log(index, row);
      }
      // console.log(this.tableData);s
    },
    // 删除按钮
    deleteRow(index, rows, row) {
      rows.splice(index, 1);
      let json_data = JSON.stringify(row);
      console.log(json_data);
      const url = "http://127.0.0.1:8000/load/deletedata/";
      axios
        .post(
          url,
          { json_data },
          {
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
          }
        )
        .then(res => {
          console.log("删除成功");
        });
    },
    handleCurrentChange(row, event, column) {
      console.log(row, event, column, event.currentTarget);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    // 展示数据
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
          // this.searchCondition = response.data;
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
              Depth: "normal"
            });
          }
          // console.log(listcol);
          // listcol[0].prop = "_id.$oid"; //_id是一个对象，取值
          listcol[0].prop = "_id"; //_id是一个对象，取值，使用这个为了取值
          listcol.splice(0, 2); //去掉_id、ZK_num字段,自己在页面添加，为了更好的遍历
          // listcol[6].nickname = "sort"; //按字段设置排序
          console.log(listcol);
          listcol[0].Depth = "sort"; //按字段设置排序
          this.cols = listcol;

          // 生成一个筛选字段ZKX，赋值给filter_data
          let tem_list = [];
          for (let i = 0; i < 55; i++) {
            // const element = array[i];
            let ZK = "ZK";
            let ZKX = ZK + i;
            // {text:"ZKX",value;"ZKX"}
            let json_data = { text: ZKX, value: ZKX };
            tem_list.push(json_data);
          }
          console.log(tem_list);
          this.filter_data = tem_list;
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


<style lang="scss">
// 设置真个数据内容的大小
.DataShow {
  height: 775px;
}
// 设置搜索框的大小
.data_search {
  height: 45px !important;
}
// 设置表格数据大小，表格+分页
.data_content {
  height: 730px !important;
  overflow: auto;
}
// 设置表格数据大小
.data_table {
  height: 690px !important;
  overflow: auto;
}
label.el-form-item__label {
  font-size: 18px;
  font-family: "Arial Narrow";
  // font-weight: bold;
  // font-family: Arial;
}
</style>