<template>
  <div class="custom-tree-container">
    <div class="block">
      <p>使用 render-content</p>
      <el-tree
        :data="data"
        show-checkbox
        node-key="id"
        default-expand-all
        :expand-on-click-node="false"
        :render-content="renderContent"
      >
      </el-tree>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
let id = 1000;

export default {
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
      // data: JSON.parse(JSON.stringify(data)),
    };
  },
  created() {
    this.showDataBase();
  },

  methods: {
    // 读取数据库信息，返回前端页面展示
    showDataBase() {
      let url = "http://127.0.0.1:8000/load/showdatabase/";
      var temp_list = [];
      axios
        .get(url, {})
        .then((res) => {
          console.log(res.data); //打印后端传过来的数据,string
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
      const newChild = { id: id++, label: "NewDataBase", children: [] };
      if (!data.children) {
        this.$set(data, "children", []);
      }
      data.children.push(newChild);
    },

    rename(node, data) {
      // const parent = node.parent;
      // const children = parent.data.children || parent.data;
      // const index = children.findIndex((d) => d.id === data.id);
      // children.splice(index, 1);
      console.log(data.isEdit);
      // console.log(data.id <= 2);
      // data.label = "xiaocui";
      let url = "http://127.0.0.1:8000/load/editdatabasename/";
      this.$prompt("请输入新的名称", "重命名", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /^[\u4e00-\u9fa5]{1,}$/, //匹配全中文
        inputErrorMessage: "请输入中文", //不符合正则匹配的提示语句
      })
        .then(({ value }) => {
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
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消修改",
          });
        });
    },

    remove(node, data) {
      const parent = node.parent;
      const children = parent.data.children || parent.data;
      const index = children.findIndex((d) => d.id === data.id);
      children.splice(index, 1);
    },

    renderContent(h, { node, data, store }) {
      // console.log(data.isEdit);
      if (!data.isEdit) {
        return (
          <span class="custom-tree-node">
            <span>{node.label}</span>
            <span>
              <el-button
                size="mini"
                type="text"
                on-click={() => this.rename(node, data)}
              >
                <i class="el-icon-edit-outline"></i>
              </el-button>
              <el-button
                size="mini"
                type="text"
                // v-show="node.isEdit"
                on-click={() => this.remove(node, data)}
              >
                <i class="el-icon-delete"></i>
              </el-button>
            </span>
          </span>
        );
      } else {
        return (
          <span class="custom-tree-node">
            <span>{node.label}</span>
            <span>
              <el-button
                size="mini"
                type="text"
                // v-show="!node.isEdit"
                on-click={() => this.append(data)}
              >
                <i class="el-icon-plus"></i>
              </el-button>
              <el-button
                size="mini"
                type="text"
                on-click={() => this.rename(node, data)}
              >
                <i class="el-icon-edit-outline"></i>
              </el-button>
            </span>
          </span>
        );
      }
    },
  },
};
</script>

<style>
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}
</style>