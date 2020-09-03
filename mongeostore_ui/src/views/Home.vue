<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-03 08:13:50
-->
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <li class="fa fa-home fa-lg"></li>
    <el-button type="primary" @click="testAxios()">测试Axios调用</el-button>
    <h3>{{$t('common.doc')}}</h3>
    <el-button type="success" @click="changeLanguage('zh_cn')">简体中文</el-button>
    <el-button type="success" @click="changeLanguage('en_us')">English</el-button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  methods: {
    // 语言切换
    changeLanguage(lang) {
      lang === "" ? "zh_cn" : lang;
      this.$i18n.locale = lang;
      this.langVisible = false;
    },
    testAxios() {
      axios.get("http://localhost:8080").then(res => {
        alert(res.data);
      });
      axios.get("http://localhost:8080/user").then(res => {
        alert(res.data);
      });
    }
  }
};
</script>
