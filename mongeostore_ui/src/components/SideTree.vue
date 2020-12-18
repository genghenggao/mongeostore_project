<template>
  <div class="custom-tree-container">
    <div class="block">
      <el-input
        style="width: 96%"
        placeholder="输入关键字进行搜索"
        v-model="filterText"
      >
      </el-input>
      <el-tree
        class="filter-tree"
        :data="data"
        node-key="id"
        :props="defaultProps"
        default-expand-all
        :filter-node-method="filterNode"
        :expand-on-click-node="false"
        @node-click="handleNodeClick"
        ref="tree"
      >
        <span
          class="custom-tree-node"
          slot-scope="{ node, data }"
          @mouseenter="mouseenter(data)"
          @mouseleave="mouseleave(data)"
        >
          <span v-if="data.isEdit" style="font-weight: bold"
            ><i class="el-icon-folder"></i>{{ node.label }}</span
          >
          <span v-else-if="!data.isEdit"
            ><i class="el-icon-folder-opened"></i>{{ node.label }}</span
          >
          <span>
            <el-button
              type="text"
              size="mini"
              v-show="data.del"
              v-if="data.isEdit"
              @click="() => append(data)"
            >
              <i class="el-icon-plus"></i>
            </el-button>
            <el-button
              type="text"
              size="mini"
              v-show="data.del"
              v-else-if="!data.isEdit"
              @click="() => remove(node, data)"
            >
              <i class="el-icon-delete"></i>
            </el-button>
            <el-button
              size="mini"
              type="text"
              v-show="data.del"
              @click="() => rename(node, data)"
            >
              <i class="el-icon-edit-outline"></i>
            </el-button>
          </span>
        </span>
      </el-tree>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
let id = 1000;

export default {
  name: "SideTree",
  inject: ["reload"], //刷新页面
  data() {
    const data = [
      {
        id: 1,
        label: "一级 1",
        children: [
          {
            id: 4,
            label: "二级 1-1",
            children: [
              {
                id: 9,
                label: "三级 1-1-1",
              },
              {
                id: 10,
                label: "三级 1-1-2",
              },
            ],
          },
        ],
      },
      {
        id: 2,
        label: "一级 2",
        children: [
          {
            id: 5,
            label: "二级 2-1",
          },
          {
            id: 6,
            label: "二级 2-2",
          },
        ],
      },
      {
        id: 3,
        label: "一级 3",
        children: [
          {
            id: 7,
            label: "二级 3-1",
          },
          {
            id: 8,
            label: "二级 3-2",
          },
        ],
      },
    ];
    return {
      data: JSON.parse(JSON.stringify(data)),
      sub_message: "", //用于父标题名称
      filterText: "",
      defaultProps: {
        children: "children",
        label: "label",
      },
    };
  },
  components: {
    // CommonData: () => import("./CommonData.vue"), //子组件
  },
  created() {
    this.showDataBase();
  },
  watch: {
    // 树形目录过滤
    filterText(val) {
      this.$refs.tree.filter(val);
    },
  },

  methods: {
    // 过滤目录
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    // 读取数据库信息，返回前端页面展示
    showDataBase() {
      let url = "http://127.0.0.1:8000/load/showdatabase/";
      var temp_list = [];
      axios
        .get(url, {})
        .then((res) => {
          // console.log(res.data); //打印后端传过来的数据,string
          // console.log(res.data.length); //打印后端d对象个数
          // console.log(typeof res.data); //打印后端传过来的数据类型
          this.data = res.data;
          // var data_json = res.data.parseJSON();
          // var data_json = JSON.parse(JSON.stringify(res.data));
          // console.log(data_json);
          // console.log(typeof data_json);
          // temp_list.push(res.data);
          // var arr = eval(temp_list);
          // var temp_list = eval("(" + res.data + ")");
          // console.log(arr);
          // console.log(typeof arr);
          // var arrParse = JSON.parse(arr)
          // console.log(typeof arrParse);
          // console.log(arrParse);
          // this.data = temp_list //将数据赋值给data
          // console.log(this.data);
          // console.log(typeof this.data);
        })
        .catch();
    },

    append(data) {
      // 前端添加集合
      // const newChild = { id: id++, label: "NewDataBase", children: [] };
      // if (!data.children) {
      //   this.$set(data, "children", []);
      // }
      // data.children.push(newChild)
      // console.log(data.children);
      let collections = [];
      for (let i = 0; i < data.children.length; i++) {
        const col_data = data.children[i];
        const collection = col_data["label"];
        // console.log(collection);
        collections.push(collection);
      }
      // console.log(collections);
      // 用es6的new Set来生成一个Set数据结构的数据，从而调用has方法来判断，有则返回true，没有则false
      let temp = new Set(collections);
      this.$prompt("请输入名称", "添加数据（请勿重名）", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /^[A-Za-z0-9\u4e00-\u9fa5]{3,}$/, //匹配全中文
        inputErrorMessage: "请输入不少于3个字符", //不符合正则匹配的提示语句
        // inputPattern: /^[\u4e00-\u9fa5]{1,}$/, //匹配全中文
        // inputErrorMessage: "请输入中文", //不符合正则匹配的提示语句
      })
        .then(({ value }) => {
          //判断集合是否存在
          if (!temp.has(value)) {
            // 后端数据添加
            const newChild = {
              id: id++,
              label: value,
              isEdit: false,
              _database: data.label,
            };
            data.children.push(newChild);
            console.log(data);
            let url = "http://127.0.0.1:8000/load/addcollection/";
            axios
              .post(url, { newChild })
              .then((res) => {
                this.$message({
                  type: "success",
                  message: "添加成功",
                });
              })
              .catch(() => {
                this.$message({
                  type: "info",
                  message: "添加失败",
                });
              });
          } else {
            this.$message({
              type: "info",
              message: "已存在，请重新输入！",
            });
          }
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消添加",
          });
        });
    },

    rename(node, data) {
      // const parent = node.parent;
      // const children = parent.data.children || parent.data;
      // const index = children.findIndex((d) => d.id === data.id);
      // children.splice(index, 1);
      // console.log(data.isEdit);
      // console.log(data.id <= 2);
      // data.label = "xiaocui";
      // console.log(node);
      // console.log(data); //当前的data
      // console.log(data["label"]); //当前数据名称
      // console.log(this.data); //数据中的data
      // console.log(this.data.length); //数据中的data
      let db_cols = [];
      if (data["isEdit"]) {
        console.log("数据库");
        // let db_cols = [];
        for (let i = 0; i < this.data.length; i++) {
          const db_data = this.data[i];
          const dbcol = db_data["label"];
          db_cols.push(dbcol);
        }
        // console.log(db_cols);
        // let db_temp = new Set(db_cols);
      } else {
        // console.log("集合");
        // console.log(data["_database"]);
        // 通过this.data拿到集合数据
        // let db_cols = [];
        let databasename = data["_database"];
        for (let i = 0; i < this.data.length; i++) {
          const db_data = this.data[i];
          const dbcol = db_data["label"];
          if (databasename == dbcol) {
            // console.log("存在" + databasename);
            // console.log(db_data);
            // console.log(db_data["children"]);
            let children_col = db_data["children"];
            for (let i = 0; i < children_col.length; i++) {
              const db_data = children_col[i];
              const collection = db_data["label"];
              db_cols.push(collection);
            }
          }
        }
        // console.log(db_cols);
        // let db_temp = new Set(db_cols);
      }
      // console.log(db_cols);
      let db_temp = new Set(db_cols);

      let url = "http://127.0.0.1:8000/load/editdatabasename/";
      this.$prompt("请输入新的名称", "重命名", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        // inputPattern: /^[\u4e00-\u9fa5]{1,}$/, //匹配全中文
        // inputErrorMessage: "请输入中文", //不符合正则匹配的提示语句
        inputPattern: /^[A-Za-z0-9\u4e00-\u9fa5]{3,}$/, //匹配全中文
        inputErrorMessage: "请输入不少于3个字符", //不符合正则匹配的提示语句
      })
        .then(({ value }) => {
          // 判断重命名的数据库和集合是否已经存在
          if (!db_temp.has(value)) {
            //可以在这里发请求，http是我模拟的一个虚假的封装好的axios请求,()可写请求参数
            axios
              .post(url, { value, data })
              .then((data) => {
                this.$message({
                  type: "success",
                  message: "修改成功",
                });
                //请求成功需局部刷新该节点，调用方法,把节点信息node传入
                this.showDataBase();
              })
              //请求失败
              .catch(() => {
                this.$message({
                  type: "info",
                  message: "修改失败",
                });
              });
          } else {
            this.$message({
              type: "info",
              message: "已存在，请重新输入！",
            });
          }
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消修改",
          });
        });
    },

    remove(node, data) {
      this.$confirm("永久删除，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 前端页面删除
          const parent = node.parent;
          const children = parent.data.children || parent.data;
          const index = children.findIndex((d) => d.id === data.id);
          children.splice(index, 1);
          // 后端数据删除
          let url = "http://127.0.0.1:8000/load/deletecollection/";
          axios
            .post(url, { data })
            .then((res) => {
              this.$message({
                type: "success",
                message: "删除成功",
              });
            })
            .catch(() => {
              //请求失败
              this.$message({
                type: "info",
                message: "删除失败",
              });
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消删除",
          });
        });
    },
    mouseenter(data) {
      this.$set(data, "del", true);
    },
    mouseleave(data) {
      this.$set(data, "del", false);
    },
    handleNodeClick(obj, node, data) {
      // console.log(data);
      // console.log(node);
      // console.log(obj);
      // console.log(obj["label"]);
      // console.log(obj["isEdit"]);
      // this.sub_message = obj["label"];
      this.$store.state.title_message = obj["label"]; //给标题动态赋值
      this.$store.state.DBorCol = obj["isEdit"]; //设置参数，判断数据库还是集合
      this.$store.state.temp_database = obj["_database"]; //判断集合属于哪个数据库

      if (this.$store.state.title_message == "钻孔信息") {
        this.$router.push({ path: "/mongeostore/drillmetahome" });
      }
      if (this.$store.state.title_message == "定位表") {
        this.$router.push({ path: "/mongeostore/drilllocationhome" });
      }
      // 点击不同集合，数据动态展示数据
      this.reload(); //重载页面
      if (!obj["isEdit"]) {
        // this.$router.push({ path: obj["label"] });
        // this.reload(); //重载页面
        // this.$refs.CommonData.showData();
        // const url = "http://127.0.0.1:8000/load/showcommondata/";
        // axios
        //   .get(url, {
        //     params: {
        //       // 设置上传到后端的数据库和集合名称
        //       colname: this.$store.state.title_message,
        //       dbname: this.$store.state.temp_database,
        //     },
        //   })
        //   .then((res) => {
        //     // console.log("success");
        //     console.log(res.data);
        //     // this.tableData = res.data;
        //     this.$store.state.colData = res.data; //将集合数据写入store，组件使用自取
        //   })
        //   .catch(() => {
        //     console.log("error");
        //   });
      } else {
        // this.$router.push({ path: obj["label"] });
      }
    },
  },
};
</script>

<style lang='scss' scoped>
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
</style>