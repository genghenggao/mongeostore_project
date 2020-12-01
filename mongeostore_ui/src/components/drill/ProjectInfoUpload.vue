<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-01 10:40:23
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-01 14:10:05
-->F
<template>
  <el-row :gutter="20"
    >·
    <el-col :span="10" :offset="6">
      <el-container style="min-width: 600px; overflow: hidden">
        <el-header><h2>项目信息上传</h2></el-header>

        <el-main>
          <el-form ref="form" :model="form" label-width="100px">
            <el-scrollbar style="height: 650px">
              <el-form-item label="钻孔编号">
                <el-input v-model="form.zk_num" placeholder="ZK1"></el-input>
              </el-form-item>
              <el-form-item label="项目名称">
                <el-input
                  v-model="form.project_name"
                  placeholder="广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查"
                ></el-input>
              </el-form-item>
              <el-form-item label="资料名称">
                <el-input
                  v-model="form.profile_name"
                  placeholder="广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查报告"
                ></el-input>
              </el-form-item>
              <el-form-item label="项目结束时间">
                <el-date-picker
                  type="date"
                  placeholder="选择日期"
                  v-model="form.finish_date"
                  style="width: 100%"
                ></el-date-picker
              ></el-form-item>

              <el-form-item label="成果资料档号">
                <el-input
                  v-model="form.achievement_num"
                  placeholder="aa548"
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
  name: "ProjectInfoUpload",
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