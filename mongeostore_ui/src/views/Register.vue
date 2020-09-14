<template>
  <div id="poster">
    <el-form
      class="login-container"
      label-position="left"
      ref="loginForm"
      :model="Register"
      label-width="80px"
    >
      <h3 class="login_title">注册</h3>
      <el-form-item prop="username" label="用户名:">
        <el-input v-model="Register.username" placeholder="请输入用户名" @blur="doRegister"></el-input>
      </el-form-item>

      <el-form-item prop="email" label="邮  箱:">
        <el-input v-model="Register.email" placeholder="请输入邮箱" @blur="doRegister"></el-input>
      </el-form-item>
      <el-form-item prop="password" label="设置密码:">
        <el-input v-model="Register.password" show-password placeholder="请输入密码" @blur="doRegister"></el-input>
      </el-form-item>
      <el-form-item prop="password2" label="确认密码:">
        <el-input
          v-model="Register.password2"
          show-password
          placeholder="请再次输入密码"
          @blur="doRegister"
        ></el-input>
      </el-form-item>
      <el-form-item prop="mobile" label="手机号:">
        <el-input v-model="Register.mobile" placeholder="请输入手机号" @blur="doRegister"></el-input>
      </el-form-item>

      <el-row>
        <el-col :span="16">
          <el-form-item prop="mobile_code" label="验证码:">
            <el-input v-model="Register.sendcode" placeholder="请输入验证码"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-button
            type="primary"
            plain
            @click="doRegister"
            :disabled="disabled"
            v-if="disabled==false"
          >获取验证码</el-button>
          <el-button
            type="button"
            @click="doRegister"
            :disabled="disabled"
            v-if="disabled==true"
          >{{btntxt}}</el-button>
        </el-col>
      </el-row>

      <el-checkbox class="checkbox" v-model="checked">同意”用户使用协议“</el-checkbox>
      <el-link class="login" :underline="false" type="primary" href="/login">登录</el-link>
      <el-form-item>
        <el-button
          type="primary"
          style="width: 100%;background: #505458;border: none"
          icon
          @click="submitRegister()"
        >注册账号</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      // 同意用户使用协议
      checked: true,
      Register: {
        username: "",
        mobile: "",
        email: "",
        password: "",
        sendcode: "",
        // submitRegister: ""
      },
      disabled: false,
      time: 0,
      btntxt: "重新发送"
    };
  },
  created() {
    // console.log($);
    // console.log("1111");
  },
  methods: {
    doRegister() {
      var res_name = /^[a-zA-Z0-9_-]{5,20}$/;
      var res_password = /^[a-zA-Z0-9_-]{6,40}$/;
      var res_email = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      var res_mobile = /^1[3456789]\d{9}$/;
      if (!res_name.test(this.Register.username)) {
        this.$message.error("请输入5-20个字符的用户名！");
        return;
      } else if (!res_email.test(this.Register.email)) {
        this.$message.error("请输入有效邮箱！");
        return;
      } else if (!res_password.test(this.Register.password)) {
        this.$message.error("请输入6位及以上密码！");
        return;
      } else if (this.Register.password2 != this.Register.password) {
        this.$message.error("两次密码不一致，请确认输入密码！");
        return;
      } else if (!res_mobile.test(this.Register.mobile)) {
        this.$message.error("请输入有效手机号！");
        return;
      } else {
        // 手机验证码
        console.log(this.Register.mobile);
        this.$message({
          message: "发送成功",
          type: "success",
          center: true
        });
        this.time = 60;
        this.disabled = true;
        this.timer();
      }
    }
  },
  //60S倒计时
  timer() {
    if (this.time > 0) {
      this.time--;
      this.btntxt = this.time + "s后重新获取";
      setTimeout(this.timer, 1000);
    } else {
      this.time = 0;
      this.btntxt = "获取验证码";
      this.disabled = false;
    }
  },
  submitRegister() {
    // this.$router.push({ path: "/" }); //无需向后台提交数据，方便前台调试
    axios
      .get("http://127.0.0.1:8000/api/register", {
        name: this.Register.username,
        mobile: this.Register.mobile,
        email: this.Register.email,
        password: this.Register.password
      })
      .then(res => {
        console.log("输出response.data", res.data);
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
