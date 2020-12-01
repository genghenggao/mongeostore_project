<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-01 10:40:49
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-01 14:09:26
-->
<template>
  <el-row :gutter="20">
    <el-col :span="10" :offset="6">
      <el-container style="min-width: 600px; overflow: hidden">
        <el-header><h2>单位信息上传</h2></el-header>
        <el-main>
          <el-form ref="form" :model="form" label-width="100px">
            <el-scrollbar style="height: 650px">
              <el-form-item label="钻孔编号">
                <el-input v-model="form.zk_num" placeholder="ZK1"></el-input>
              </el-form-item>
              <el-form-item label="上传人员">
                <el-input
                  v-model="form.uploader"
                  placeholder="采集员"
                ></el-input>
              </el-form-item>

              <el-form-item label="上传日期">
                <el-date-picker
                  type="date"
                  placeholder="选择日期"
                  v-model="form.upload_date"
                  style="width: 100%"
                ></el-date-picker
              ></el-form-item>

              <el-form-item label="单位名称">
                <el-input
                  v-model="form.company_name"
                  placeholder="中国矿业大学（北京）煤炭资源与安全开采国家重点实验室"
                ></el-input>
              </el-form-item>
              <el-form-item label="通讯地址">
                <el-input
                  v-model="form.address"
                  placeholder="北京市海淀区学院路丁11号"
                ></el-input>
              </el-form-item>

              <el-form-item>
                <el-button
                  ref="VideoChose"
                  type="primary"
                  size="medium  "
                  @click="onSubmit"
                  >提交</el-button
                >
                <el-button>取消</el-button>
              </el-form-item>
            </el-scrollbar>
          </el-form>
        </el-main>
      </el-container>
    </el-col>
  </el-row>
</template>

<script>
import plupload from "plupload";
import axios from "axios";
import { stringify } from "qs";
export default {
  name: "CompanyInfoUpload",
  data() {
    return {
      form: {
        zk_num: "",
        project_name: "",
        profile_name: "",
        finish_date: "",
        achievement_num: "",
      },
    };
  },

  mounted() {},
  computed: {},
  methods: {
    //开始上传
    // FileUplodeOn() {
    //   this.uploader.start();
    // },
    onSubmit() {
      this.uploader.start();
    },
  },
};
</script>

<style lang="scss">
.el-form-item {
//   width: 560px; //这里设置为了和右边滚动条有一定的距离
}
.el-scrollbar__wrap {
  overflow-x: hidden; //设置滚动条隐藏
}
</style>