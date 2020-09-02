<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-31 15:03:39
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-01 21:59:37
-->
<template>
<body id="poster">
  <el-form class="login-container" label-position="left" label-width="0px">
    <h3 class="login_title">MongeoStore</h3>
    <el-form-item>
      <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="请输入账号"></el-input>
    </el-form-item>
    <el-form-item>
      <el-input
        type="password"
        v-model="loginForm.password"
        auto-complete="off"
        placeholder="请输入密码"
        show-password
      ></el-input>
    </el-form-item>
    <el-form-item style="width: 100%">
      <el-button
        type="primary"
        style="width: 100%;background: #505458;border: none"
        v-on:click="login"
      >登录</el-button>
      <el-link :underline="false" type="primary" class="fpassword">忘记密码？</el-link>
      <el-link :underline="false" type="primary" class="register">注册</el-link>
    </el-form-item>
  </el-form>
</body>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      responseResult: []
    };
  },
  methods: {
    login() {
      var _this = this;
      console.log(this.$store.state);
      this.$axios
        .post("/login", {
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        .then(successResponse => {
          if (successResponse.data.code === 200) {
            _this.$store.commit("login", _this.loginForm);
            var path = this.$route.query.redirect;
            this.$router.replace({
              path: path === "/" || path === undefined ? "/index" : path
            });
          }
        })
        // eslint-disable-next-line no-unused-vars
        .catch(failResponse => {});
    }
  }
};
</script>

<style lang="scss" scoped>
#poster {
  background: url("../assets/background.jpg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
body {
  margin: 0px;
}
.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}

.login_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}
.register{
  position: relative;
  right:  -160px;
  // width: 100%;

}
</style>