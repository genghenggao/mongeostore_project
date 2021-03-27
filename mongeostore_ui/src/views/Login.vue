<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-31 15:03:39
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-27 19:15:39
-->
<template>
  <div id="poster">
    <Navbar />
    <div class="login-body">
      <h1>欢迎登录地震大数据管理系统</h1>
      <el-form
        class="login-container"
        ref="Login"
        :model="Login"
        :rules="rules"
        label-position="left"
        label-width="80px"
      >
        <h3 class="login_title">MonGeoStore</h3>
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
                <!-- <div>{{ msg }}</div> -->
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
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
import aa from "@/assets/images/aa.jpg"; //	如果使用网络图片资源就无需引入

import Navbar from "@/components/Navbar.vue";

export default {
  name: "Login",
  components: {
    Navbar
  },
  data() {
    // <!--验证账号-->
    let checkUsername = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入用户名"));
      } else {
        callback();
      }
    };
    // <!--验证密码-->
    let checkPassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      visible: false, //图片验证弹出框
      msg: "",
      // bgimgs: [aa], //	如果使用网络图片资源就用该值
      bgimgs: [], //	如果使用网络图片资源就用该值
      text: "向右滑动~",
      Login: {
        username: "",
        password: ""
      },
      rules: {
        username: [
          { required: true, message: "请输入账号", trigger: "blur" },
          {
            // pattern: /^(?!(\d+)$)[a-zA-Z\d_]{4,20}$/,
            pattern: /^[a-zA-Z0-9_-]{5,20}$/,
            message: "账号长度5-20，可包括数字字母下划线",
            trigger: "blur"
          },
          { validator: checkUsername, trigger: "blur" }
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            // pattern: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
            pattern: /^[a-zA-Z0-9_-]{6,20}$/,
            message: "密码长度为6-20位，可以为数字、字母",
            trigger: "blur"
          },
          { validator: checkPassword, trigger: "blur" }
        ]
      }
      // responseResult: []
    };
  },
  watch: {},
  methods: {
    onSuccess(Login) {
      // let username = this.Login.username;
      // let password = this.Login.password;
      let postData = qs.stringify({
        first: 1, //用于解决第一个参数为None设置的无用参数，现在我还不知道为什么，但这样可以解决，以后发现根本再来补充
        username: this.Login.username,
        // email: this.Login.email,
        password: this.Login.password,
        // password2: this.Login.password2,
        // mobile: this.Login.mobile,
        // smscode: this.Login.smscode,
        last: 1 //用于解决后端smscode参数为3019"}多了"}问题
      });
      console.log(postData);
      // console.log(postData.username);
      let url = `http://127.0.0.1:8000/api/userlogin/`;
      axios
        .post(
          url,
          {
            // params: this.userInfo, //params用于get请求
            data: postData,
            responseType: "json"
          },
          {
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
          }
        )
        .then(response => {
          console.log("优雅的分割线");
          // console.log(response.data.username);
          // console.log(response.data.password);
          console.log(response.data.status_code);
          console.log(response);
          // 登录成功，定向到首页
          if (response.data.status_code == 200) {
            // _this.$store.commit("login", _this.loginForm);
            // var path = this.$route.query.redirect;
            // var path = '/mongeostore';
            var path = '/mongeostorehome';
            console.log(path);
            this.$router.replace({
              path: path === "/" || path === undefined ? "/" : path
            });
          } else if (response.data.status_code == 502) {
            // alert("用户不存在")
            this.$message.error("用户不存在，请重新输入");
            this.visible = false;
            // this.$router.push("/");
          } else {
            // alert("密码不正确")
            this.$message.error("密码不正确，请重新输入");
            this.visible = false;
          }
          console.log("....");
        })
        .catch(error => {
          console.log("....");
        });
      // this.$router.push("/index");
      // this.msg = "登录成功~";
      // this.$message({
      //   message: "恭喜你，注册成功！",
      //   type: "success"
      // });
    },
    onFail() {
      // this.msg = "登录失败！";
      this.$message.error("验证码不正确，登录失败");
    },
    onRefresh() {
      // this.msg = "重新生成验证码";
      this.$message.error("重新生成验证码，请稍后...");
    }

    // login() {
    //   var _this = this;
    //   console.log(this.$store.state);
    //   this.$api
    //     .post("/login", {
    //       username: this.loginForm.username,
    //       password: this.loginForm.password
    //     })
    //     .then(successResponse => {
    //       if (successResponse.data.code === 200) {
    //         _this.$store.commit("login", _this.loginForm);
    //         var path = this.$route.query.redirect;
    //         this.$router.replace({
    //           path: path === "/" || path === undefined ? "/index" : path
    //         });
    //       }
    //     })
    //     // eslint-disable-next-line no-unused-vars
    //     .catch(failResponse => {});
    // }
  }
};
</script>

<style lang="scss" scoped>
// 背景
#poster {
  background: url("../assets/images/background.jpg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
// 登录内容
.login-body {
  // 登录表格的位置
  padding-left: 1000px;
  padding-top: 100px;
  height: 800px;
  position: absolute;

}
// 登录框位置
form.el-form.login-container.el-form--label-left {
  // right: 0px;
  position: absolute;
  /* width: 600px; */
  margin: 30px 30px 0px 180px;
  top: 200px;
  /* left: 30px; */
}
// 注册标题设置
.login-body h1 {
  // 欢迎字体设置
  color: rgb(228, 214, 214);
  margin: 0 30px 0 80px;
  padding: 40px 0 0 0;
  position: absolute;
  top: 60px;
  // left: 3%;
  width: 600px;
}
// 登录框
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
// 登录框标题
.login_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}
// 注册
.register {
  position: relative;
  right: 40px;
  // width: 100%;
}
// 注册位置
.register_id {
  right: -80px;
}

// 密码与注册
.el-popover {
  padding: 0px;
  // line-height: 1;
}
</style>