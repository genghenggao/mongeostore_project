<template>
  <div id="poster">
    <el-form
      class="login-container"
      label-position="left"
      ref="loginForm"
      :model="user"
      label-width="80px"
    >
      <h3 class="login_title">注册</h3>
      <el-form-item prop="username" label="用户名:">
        <el-input v-model="user.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item prop="mobile" label="手机号:">
        <el-input v-model="user.mobile" placeholder="请输入手机号"></el-input>
      </el-form-item>
      <el-form-item prop="email" label="邮箱:">
        <el-input v-model="user.email" placeholder="请输入邮箱"></el-input>
      </el-form-item>
      <el-form-item prop="password" label="设置密码:">
        <el-input v-model="user.password" show-password placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item prop="password2" label="确认密码:">
        <el-input v-model="user.password2" show-password placeholder="请再次输入密码"></el-input>
      </el-form-item>
      <el-checkbox class="checkbox" v-model="checked">同意”用户使用协议“</el-checkbox>
      <el-link class="login" :underline="false" type="primary" href="/login">登录</el-link>
      <el-form-item>
        <el-button
          type="primary"
          style="width: 100%;background: #505458;border: none"
          icon
          @click="doRegister()"
        >注册账号</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "register",
  data() {
    return {
      // 同意用户使用协议
      checked: true,
      user: {
        username: "",
        mobile:"",
        email: "",
        password: ""
      }
    };
  },
  created() {
    // console.log($);
    // console.log("1111");
  },
  methods: {
    doRegister() {
      var res_name = /^[a-zA-Z0-9_-]{5,20}$/;
      if (!res_name.test(this.user.username)) {
        this.$message.error("请输入5-20个字符的用户名！");
        return;
      } else if (!this.user.mobile) {
        this.$message.error("请输入手机号！");
        return;
      } else if (!this.user.email) {
        this.$message.error("请输入邮箱！");
        return;
      } else if (this.user.email != null && this.user.mobile != null) {
        var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        var res2 = /^1[3456789]\d{9}$/;
        if (!res2.test(this.user.mobile)) {
          this.$message.error("请输入有效手机号！");
        } else if (!reg.test(this.user.email)) {
          this.$message.error("请输入有效的邮箱！");
        } else if (!this.user.password) {
          this.$message.error("请输入密码！");
          return;
        } else if (!this.user.password2  && password != password2) {
          this.$message.error("两次密码不一致，请确认输入密码！");
          return;
        } else {
          // this.$router.push({ path: "/" }); //无需向后台提交数据，方便前台调试
          this.$http
            .post("/register/", {
              name: this.user.username,
              mobile: this.user.mobile,
              email: this.user.email,
              password: this.user.password,
            })
            .then(res => {
              // console.log("输出response.data", res.data);
              // console.log("输出response.data.status", res.data.status);
              if (res.data.status === 200) {
                this.$router.push({
                  path: "/"
                });
              } else {
                alert("您输入的用户名已存在！");
              }
            });
        }
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
#poster {
  background: url("../assets/images/background.jpg") no-repeat;
  background-position: center;
  width: 100%;
  height: 100%;
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
  margin: 0px auto 20px auto;
  text-align: center;
  color: #505458;
}

.checkbox {
  padding-left: 60px;
}

.login {
  // margin-left: -50px;
  padding-left: 60px;
}
</style>
