<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-31 15:03:39
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-25 22:29:16
-->
<template>
  <div id="poster">
    <el-form
      class="login-container"
      ref="Login"
      :model="Login"
      label-position="left"
      label-width="80px"
    >
      <h3 class="login_title">MongeoStore</h3>
      <el-form-item prop="username" label="用户名:">
        <el-input
          type="text"
          v-model="Login.username"
          auto-complete="off"
          placeholder="请输入账号"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password" label="密码:">
        <el-input
          type="password"
          v-model="Login.password"
          auto-complete="off"
          placeholder="请输入密码"
          show-password
        ></el-input>
      </el-form-item>

      <!-- <el-row>
        <el-col :span="18">
          <el-form-item prop="picture_code" label="验证码:">
            <el-input
              type="text"
              v-model="Login.picture_code"
              auto-complete="off"
              placeholder="请输入图片验证码"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple-light"></div>
        </el-col>
      </el-row> -->

      <el-form-item style="width: 100%">
        <el-popover
          placement="top"
          width="320"
          height="230"
          trigger="manual"
          v-model="visible"
        >
          <el-card v-model="visible">
            <div class="page-slidecode">
              <slide-verify
                :l="32"
                :r="10"
                :w="260"
                :h="155"
                :imgs="bgimgs"
                @success="onSuccess"
                @fail="onFail"
                @refresh="onRefresh"
                :slider-text="text"
              ></slide-verify>
              <div>{{ msg }}</div>
              <!--这个没完成设置文字居中-->
            </div>
          </el-card>
          <el-button
            type="primary"
            style="width: 100%;background: #505458;border: none"
            slot="reference"
            v-on:click="visible = !visible"
            >登录</el-button
          >
        </el-popover>
        <div class="register">
          <el-link :underline="false" type="primary">忘记密码？</el-link>
          <el-link
            class="register_id"
            :underline="false"
            type="primary"
            href="/register"
            >注册</el-link
          >
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      visible: false, //图片验证弹出框
      msg: "",
      bgimgs: [], //	如果使用网络图片资源就用该值
      text: "向右滑动~",
      Login: {
        username: "",
        password: ""
      },
      responseResult: []
    };
  },
  methods: {
    onSuccess() {
      let username = this.Login.username;
      let password = this.Login.password;
      console.log(username);
      console.log(password);
      let url = `http://127.0.0.1:8000/api/login/`;
      axios
        .post(
          url,
          {
            // params: this.userInfo, //params用于get请求
            responseType: "json"
          },
          {
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
          }
        )
        .then(res => {
          console.log(res.data.username);
          console.log(res.data.password);
          console.log(res);
          console.log(data);
        })
        .catch(error => {
          console.log("....");
        });
      // this.$router.push("/index");
      this.msg = "登录成功~";
    },
    onFail() {
      this.msg = "登录失败！";
    },
    onRefresh() {
      this.msg = "重新生成验证码";
    },
    login() {
      var _this = this;
      console.log(this.$store.state);
      this.$api
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
  background: url("../assets/images/background.jpg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}

.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 400px;
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
.register {
  position: relative;
  right: 40px;
  // width: 100%;
}
.register_id {
  right: -80px;
}

.el-popover {
  padding: 0px;
  // line-height: 1;
}
</style>