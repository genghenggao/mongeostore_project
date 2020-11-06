<template>
  <div id="poster">
    <Navbar />
    <div class="login-body">
      <h1>欢迎注册地震大数据管理系统</h1>
      <el-form
        class="login-container"
        label-position="left"
        ref="Register"
        :model="Register"
        :rules="rules"
        label-width="100px"
      >
        <h3 class="login_title">注册</h3>
        <el-form-item prop="username" label="用户名:">
          <el-input
            v-model="Register.username"
            placeholder="请输入用户名"
          ></el-input>
        </el-form-item>

        <el-form-item prop="email" label="邮  箱:">
          <el-input
            v-model="Register.email"
            placeholder="请输入邮箱"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password" label="设置密码:">
          <el-input
            v-model="Register.password"
            show-password
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password2" label="确认密码:">
          <el-input
            v-model="Register.password2"
            show-password
            placeholder="请再次输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item prop="mobile" label="手机号:">
          <el-input
            v-model="Register.mobile"
            placeholder="请输入手机号"
          ></el-input>
        </el-form-item>

        <el-row>
          <el-col :span="16">
            <el-form-item prop="smscode" label="验证码:">
              <el-input
                v-model="Register.smscode"
                placeholder="短信验证码"
              ></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-button
              plain
              @click="sendCode"
              :disabled="true"
              v-if="disabled == 0"
              >{{ buttonText }}</el-button
            >
            <el-button
              type="primary"
              :disabled="isDisabled"
              @click="sendCode"
              v-else-if="disabled == 1"
              >{{ buttonText }}</el-button
            >
          </el-col>
        </el-row>

        <el-checkbox class="checkbox" name="allow" id="allow" v-model="allow"
          >同意”用户使用协议“</el-checkbox
        >
        <el-link class="login" :underline="false" type="primary" href="/login"
          >登录</el-link
        >
        <el-form-item>
          <el-button
            style="width: 100%;background: #505458;border: none"
            icon
            :loading="logining"
            :disabled="true"
            v-if="!isLogin"
            @click="submitRegister('Register')"
            >注册账号</el-button
          >
          <el-button
            type="primary"
            style="width: 100%;background: #505458;border: none"
            icon
            :loading="logining"
            v-else-if="isLogin"
            @click="submitRegister('Register')"
            >注册账号</el-button
          >
        </el-form-item>
      </el-form>
    </div>
    <!-- <el-button :plain="true" @click="open4">错误</el-button> -->
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
import Navbar from "@/components/Navbar.vue";
export default {
  name: "Register",
  components: {
    Navbar
  },
  data() {
    // <!--验证账号-->
    let checkUsername = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        // callback();
        // 检查重名
        const url =
          // this.host + "/smscode/?mobile=" + this.mobile ;
          "http://127.0.0.1:8000/api/username/?username=" +
          this.Register.username;
        axios
          .get(url, {
            responseType: "json"
          })
          .then(response => {
            // 表示后端发送短信成功
            if (response.data.count > 0) {
              console.log("用户名已存在");
              // alert("用户名已存在了啊");
              callback(new Error("用户名已存在，请重新输入"));
            } else {
              // element ui 表单验证 this.$refs[formName].validate()里面的内容死活不执行
              callback();
            }
          })
          .catch(error => {
            console.log(error.response);
          });
      }
    };
    // <!--验证邮箱-->
    let checkEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入邮箱"));
      } else {
        // callback();
        // 检查重名
        const url =
          // this.host + "/smscode/?mobile=" + this.mobile ;
          "http://127.0.0.1:8000/api/email/?email=" + this.Register.email;
        axios
          .get(url, {
            responseType: "json"
          })
          .then(response => {
            // 表示后端发送短信成功
            if (response.data.count > 0) {
              console.log("邮箱已存在");
              // alert("邮箱已存在");
              callback(new Error("邮箱已存在，请重新输入"));
            } else {
              // element ui 表单验证 this.$refs[formName].validate()里面的内容死活不执行
              callback();
            }
          })
          .catch(error => {
            console.log(error.response);
          });
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
    // <!--确定密码-->
    let checkPassword2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value != this.Register.password) {
        callback(new Error("两次密码不一致，请确认输入密码！"));
      } else {
        callback();
      }
    };
    // <!--验证手机号是否合法-->
    let checkTel = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机号码"));
      }
      // else if (!this.checkMobile(value)) {
      //   callback(new Error("请输入正确的11位手机号码！！！！"));
      //   // callback(new Error("手机号已存在"));
      // }
      else {
        // callback();
        // 检查重名
        const url =
          // this.host + "/smscode/?mobile=" + this.mobile ;
          "http://127.0.0.1:8000/api/mobile/?mobile=" + this.Register.mobile;
        axios
          .get(url, {
            responseType: "json"
          })
          .then(response => {
            // 表示后端发送短信成功
            if (response.data.count > 0) {
              console.log("手机号已存在");
              // alert("手机号已存在");
              callback(new Error("手机号已存在，请重新输入"));
            } else {
              // let time = 60;
              // this.buttonText = "已发送";
              // this.isDisabled = true;
              // element ui 表单验证 this.$refs[formName].validate()里面的内容死活不执行
              callback();
            }
          })
          .catch(error => {
            console.log(error.response);
          });
      }
    };
    //  <!--验证码是否为空-->
    let checkSmscode = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机验证码"));
      } else {
        callback();
        // 检查重名
        // const url =
        //   // this.host + "/smscode/?mobile=" + this.mobile ;
        //   "http://127.0.0.1:8000/api/smscode/?smcode=" + this.Register.smscode;
        // axios
        //   .get(url, {
        //     responseType: "json"
        //   })
        //   .then(response => {
        //     // 表示后端发送短信成功
        //     if (response.data.status_code != 200) {
        //       console.log("手机验证码错误");
        //       console.log(response.data.status_code);
        //       // alert("手机号已存在");
        //       callback(new Error("手机验证码错误，请重新输入"));
        //     } else {
        //       // let time = 60;
        //       // this.buttonText = "已发送";
        //       // this.isDisabled = true;
        //       // element ui 表单验证 this.$refs[formName].validate()里面的内容死活不执行
        //       callback();
        //     }
        //   })
        //   .catch(error => {
        //     console.log(error.response);
        //   });
      }
    };
    return {
      Register: {
        username: "",
        email: "",
        mobile: "",
        password: "",
        password2: "",
        smscode: ""
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
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            pattern: /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/,
            message: "请输入有效邮箱",
            trigger: "blur"
          },
          { validator: checkEmail, trigger: "blur" }
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
        ],
        password2: [
          { required: true, message: "请确认输入密码", trigger: "blur" },
          {
            // pattern: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
            pattern: /^[a-zA-Z0-9_-]{6,20}$/,
            message: "密码长度为6-20位，可以为数字、字母",
            trigger: "blur"
          },
          { validator: checkPassword2, trigger: "blur" }
        ],
        mobile: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          {
            pattern: /^[1][3,4,5,6,7,8,9][0-9]{9}$/,
            message: "请输入正确的11位手机号码",
            trigger: "blur"
          },
          { validator: checkTel, trigger: "blur" }
        ],
        smscode: [
          { required: true, message: "请输入短信验证码", trigger: "blur" },
          {
            pattern: /^[0-9]{4}$/,
            message: "输入四位数字验证码",
            trigger: "blur"
          },
          { validator: checkSmscode, trigger: "blur" }
        ]
      },
      // activeName: "first",
      buttonText: "获取验证码",
      isDisabled: false, // 是否禁止点击发送验证码按钮
      flag: true,
      visible: true,
      allow: true, // 同意用户使用协议
      disabled: 0,
      isLog: false,
      isLogin: false,
      logining: false
    };
  },
  watch: {
    //账手机验证btn按钮显示高亮
    "Register.mobile"() {
      if (this.Register.mobile != "") {
        this.disabled = 1;
      } else {
        this.disabled = 0;
      }
    },
    Register: {
      // 判断注册按钮状态
      handler: function(val, oldval) {
        if (
          val.username != "" &&
          val.email != "" &&
          val.password != "" &&
          val.password2 != "" &&
          val.mobile != "" &&
          val.smscode != ""
          //&& this.allow !=true
        ) {
          this.isLogin = true;
        } else {
          this.isLogin = false;
        }
      },
      deep: true //对象内部的属性监听，也叫深度监听
    }
  },
  created() {
    // console.log($);
    // console.log("1111");
  },
  methods: {
    //密码判断渲染，true:暗文显示，false:明文显示
    changePass(value) {
      this.visible = !(value === "show");
    },

    // <!--发送验证码-->
    sendCode() {
      // let tel = this.Register.mobile;
      // if (this.checkMobile(tel)) {
      //   console.log(tel);
      let time = 60;
      // this.buttonText = "已发送";
      // this.isDisabled = true;

      // 向后端接口发送请求，让后端发送短信验证码
      const url =
        // this.host + "/smscode/?mobile=" + this.mobile ;
        "http://127.0.0.1:8000/api/send_sms/?mobile=" + this.Register.mobile;
      axios
        .get(url, {
          params: {
            tpl: "register" //让后端判断是注册还是登录，用来获取短信验证码
          },
          responseType: "json"
        })
        .then(response => {
          // 表示后端发送短信成功
          if (this.flag) {
            // 倒计时60秒，60秒后允许用户再次点击发送短信验证码的按钮
            this.flag = false;
            // 设置一个计时器
            const timer = setInterval(() => {
              time--;
              this.buttonText = time + " s";
              if (time === 0) {
                // 如果计时器到最后, 清除计时器对象
                clearInterval(timer);
                // 将点击获取验证码的按钮展示的文本回复成原始文本
                // this.sms_code_message = "获取短信验证码";
                this.buttonText = "重新获取";
                // 将点击按钮的onclick事件函数恢复回去
                // this.sending_flag = false;
                this.isDisabled = false;
                this.flag = true;
              }
            }, 1000);
          }
        })
        .catch(error => {
          console.log(error.response);
          this.sending_flag = false;
        });
      // }
    },

    // 验证手机号,判断验证码按钮
    checkMobile(str) {
      let reg = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
      if (reg.test(str)) {
        return true;
      } else {
        return false;
      }
    },

    submitRegister(Register) {
      //点击登录 验证手机& 验证码是否符合条件
      let postData = qs.stringify({
        first: 1, //用于解决第一个参数为None设置的无用参数，现在我还不知道为什么，但这样可以解决，以后发现根本再来补充
        username: this.Register.username,
        email: this.Register.email,
        password: this.Register.password,
        password2: this.Register.password2,
        mobile: this.Register.mobile,
        smscode: this.Register.smscode,
        last: 1 //用于解决后端smscode参数为3019"}多了"}问题
      });
      console.log("postData" + postData);
      this.$refs[Register].validate(valid => {
        // 为表单绑定验证功能
        if (valid) {
          const url = `http://127.0.0.1:8000/api/register/`;
          axios
            .post(
              url,
              {
                // params: this.userInfo, //params用于get请求
                data: postData //data用于post请求
              },
              {
                headers: { "Content-Type": "application/x-www-form-urlencoded" } //用于解决axios post 产生的403错误,这个地方可以考虑一下配置settings.py,在里面配置REST_FARAMEWOTRK={#全局解析} 参考一下：https://dog.wtf/tech/drf-learning-notes-4-the-parsers-module/
              }
            )
            .then(res => {
              console.log("注册成功走这里");
              console.log(res);
              console.log(res.data);
              console.log(res.data.status_code);
              if (res.data.status_code == 500) {
                // alert("验证码失效，或未发送，请重新发送！");
                this.$message.error("验证码失效，或未发送，请重新发送！");
              } else if (res.data.status_code == 501) {
                this.$message.error("验证码错误，请重新输入");
              } else {
                this.$message({
                  message: "恭喜你，注册成功！",
                  type: "success"
                });
                this.$router.push("/login");
              }

              // if (res.data.EID == 0) {
              //   var token = res.data.Data[0].token;
              //   localStorage.setItem("token", token);
              //   this.$message({
              //     showClose: true,
              //     message: "登录成功",
              //     type: "success"
              //   });
              //   this.$router.push({ path: "/index" });
              // } else {
              //   this.$message({
              //     showClose: true,
              //     message: res.data.Err,
              //     type: "warning"
              //   });
              // }
            })
            .catch(error => {
              // console.log(error);
              console.log("走的是catch");
              console.log("....");
              // console.log(error.data.status_code);
              // if (error.data.status_code == 500) {
              //   alert("验证码失效，或未发送，请重新发送！");
              //   this.$message.error("验证码失效，或未发送，请重新发送！");
              // } else {
              //   alert("验证码错误，请重新输入");
              //   this.$message.error("验证码错误，请重新输入");
              // }
              // alert("验证码失效，或未发送，请重新发送！");
              // this.$message({
              //   message: res.message,
              //   type: "error"
              // });
            });
          console.log("无论成功与否都走一遍");
          // this.$router.push("/login");
        } else {
          this.dialogVisible = true;
          return false;
        }
      });
    }

    //   axios
    //     .get("http://127.0.0.1:8000/api/register", {
    //       name: this.Register.username,
    //       email: this.Register.email,
    //       mobile: this.Register.mobile,
    //       password: this.Register.password
    //     })
    //     .then(res => {
    //       console.log("输出response.data", res.data);
    //       // console.log("输出response.data.status", res.data.status);
    //       if (res.data.status === 200) {
    //         this.$router.push({
    //           path: "/"
    //         });
    //       } else {
    //         alert("您输入的用户名已存在！");
    //       }
    //     });
    // }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<style lang="scss" scoped>
h1 {
  // 欢迎字体设置
  color: rgb(228, 214, 214);
}
.login-body {
  // 登录表格的位置
  padding-left: 1000px;
  padding-top: 50px;
}
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
