<template>
  <div class="page">
    <div class="login-box">
      <p data-v-032893be class="title">欢迎登录</p>
      <el-tabs v-model="activeName">
        <el-tab-pane label="密码登录" name="first">
          <el-form
            :model="ruleForm"
            status-icon
            :rules="rules"
            ref="ruleForm"
            label-width="0"
            class="demo-ruleForm"
          >
            <el-form-item prop="account">
              <el-input
                type="text"
                prefix-icon="el-icon-user-solid"
                v-model="ruleForm.account"
                auto-complete="off"
                placeholder="请输入账号"
              ></el-input>
            </el-form-item>
            <el-form-item prop="pass" v-if="visible">
              <el-input
                type="password"
                prefix-icon="el-icon-lock"
                v-model="ruleForm.pass"
                auto-complete="off"
                placeholder="请输入密码"
              >
                <i
                  slot="suffix"
                  title="显示密码"
                  @click="changePass('show')"
                  style="cursor:pointer;"
                  class="iconfont iconyanjing_kai"
                ></i>
              </el-input>
            </el-form-item>
            <el-form-item prop="pass" v-else>
              <el-input type="text" v-model="ruleForm.pass" auto-complete="off" placeholder="请输入密码">
                <i
                  slot="suffix"
                  title="隐藏密码"
                  @click="changePass('hide')"
                  style="cursor:pointer;"
                  class="iconfont iconyanjing_bi"
                ></i>
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                :loading="logining"
                :disabled="true"
                v-if="!isLog"
                @click="submitForm('ruleForm')"
                style="width:100%;"
              >登录</el-button>
              <el-button
                type="primary"
                :loading="logining"
                v-else-if="isLog"
                @click="submitForm('ruleForm')"
                style="width:100%;"
              >登录</el-button>
              <!-- <p class="login" @click="gotoLogin">已有账号？立即登录</p> -->
            </el-form-item>
            <el-form-item class="login">
              <label id="showPasswordToggle">
                <el-checkbox v-model="checked" id="showPasswordCheck">已阅读并同意《服务协议》</el-checkbox>
              </label>
              <div class="gotoRight">
                <span @click="gotoLoginForget">忘记密码</span>
                <el-divider direction="vertical"></el-divider>
                <span @click="gotoLoginReg">免费注册</span>
              </div>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="验证码登录" name="second">
          <el-form
            :model="ruleForm2"
            status-icon
            :rules="rules"
            ref="ruleForm2"
            label-width="0"
            class="demo-ruleForm"
          >
            <el-form-item prop="tel">
              <el-input v-model="ruleForm2.tel" auto-complete="off" placeholder="请输入手机号"></el-input>
            </el-form-item>
            <el-form-item prop="smscode" class="code">
              <el-input v-model="ruleForm2.smscode" placeholder="短信验证码"></el-input>
              <el-button :disabled="true" @click="sendCode" v-if="disabled== 0">{{buttonText}}</el-button>
              <el-button
                type="primary"
                :disabled="isDisabled"
                class="btn-color"
                @click="sendCode"
                v-else-if="disabled== 1"
              >{{buttonText}}</el-button>
            </el-form-item>
            <el-form-item>
              <el-button
                :loading="logining"
                :disabled="true"
                v-if="!isLogin"
                @click="submitForm('ruleForm2')"
                style="width:100%;"
              >登录</el-button>
              <el-button
                type="primary"
                :loading="logining"
                v-else-if="isLogin"
                @click="submitForm('ruleForm2')"
                style="width:100%;"
              >登录</el-button>
            </el-form-item>
            <el-form-item class="login">
              <label id="showPasswordToggle">
                <el-checkbox v-model="checked" id="showPasswordCheck">已阅读并同意《服务协议》</el-checkbox>
              </label>
              <div class="gotoRight">
                <span @click="gotoLoginForget">忘记密码</span>
                <el-divider direction="vertical"></el-divider>
                <span @click="gotoLoginReg">免费注册</span>
              </div>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    // <!--验证账号-->
    let account = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        callback();
      }
    };
    // <!--验证密码-->
    let validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    // <!--验证手机号是否合法-->
    let checkTel = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机号码"));
      } else if (!this.checkMobile(value)) {
        callback(new Error("请输入正确的11位手机号码"));
      } else {
        callback();
      }
    };
    //  <!--验证码是否为空-->
    let checkSmscode = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入手机验证码"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        account: "",
        pass: ""
      },
      ruleForm2: {
        tel: "",
        smscode: ""
      },
      rules: {
        account: [
          { required: true, message: "请输入账号", trigger: "blur" },
          {
            pattern: /^(?!(\d+)$)[a-zA-Z\d_]{4,20}$/,
            message: "账号长度4-20，可包括数字、字母、下划线",
            trigger: "blur"
          },
          { validator: account, trigger: "blur" }
        ],
        pass: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            pattern: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$/,
            message: "密码长度为6-20位，可以为数字、字母",
            trigger: "blur"
          },
          { validator: validatePass, trigger: "blur" }
        ],
        tel: [
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
            pattern: /^[0-9]{6}$/,
            message: "请输入正确的六位数字验证码",
            trigger: "blur"
          },
          { validator: checkSmscode, trigger: "blur" }
        ]
      },
      activeName: "first",
      buttonText: "获取短信验证码",
      isDisabled: false, // 是否禁止点击发送验证码按钮
      flag: true,
      visible: true,
      checked: true,
      disabled: 0,
      isLog: false,
      isLogin: false,
      logining: false
    };
  },
  watch: {
    //账号验证btn按钮显示高亮
    ruleForm: {
      handler: function() {
        if (this.ruleForm.account != "" && this.ruleForm.pass != "") {
          this.isLog = true;
        } else {
          this.isLog = false;
        }
      },
      deep: true
    },
    //账手机验证btn按钮显示高亮
    "ruleForm2.tel"() {
      if (this.ruleForm2.tel != "") {
        this.disabled = 1;
      } else {
        this.disabled = 0;
      }
    },
    ruleForm2: {
      handler: function(val, oldval) {
        if (val.tel != "" && val.smscode != "") {
          this.isLogin = true;
        } else {
          this.isLogin = false;
        }
      },
      deep: true //对象内部的属性监听，也叫深度监听
    }
  },
  methods: {
    //密码判断渲染，true:暗文显示，false:明文显示
    changePass(value) {
      this.visible = !(value === "show");
    },
    // <!--发送验证码-->
    sendCode() {
      let tel = this.ruleForm2.tel;
      if (this.checkMobile(tel)) {
        console.log(tel);
        let time = 60;
        this.buttonText = "已发送";
        this.isDisabled = true;
        if (this.flag) {
          this.flag = false;
          let timer = setInterval(() => {
            time--;
            this.buttonText = time + " s";
            if (time === 0) {
              clearInterval(timer);
              this.buttonText = "重新获取";
              this.isDisabled = false;
              this.flag = true;
            }
          }, 1000);
        }
      }
    },
    // <!--提交登录-->
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.logining = true;
          setTimeout(() => {
            this.$message({
              message: "登录成功！",
              type: "success"
            });
          }, 400);
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    // <!--免费注册页-->
    gotoLoginReg() {
      this.$router.push({
        path: "/"
      });
    },
    // <!--忘记密码页-->
    gotoLoginForget() {
      this.$router.push({
        path: "/LoginForget"
      });
    },
    // 验证手机号
    checkMobile(str) {
      let reg = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
      if (reg.test(str)) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>
 
<style lang="scss" scoped>
$white-bg-color: #ffffff;
$bg-color: #f7f7f7;
$btn-color: #409eff;
.page {
  background-color: $bg-color;
  position: absolute;
  width: 100%;
  height: 100%;
  font-size: 16px;
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  .login-box {
    position: absolute;
    top: 45%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    display: block;
    width: 100%;
    max-width: 400px;
    background-color: $white-bg-color;
    margin: 0;
    padding: 15px 35px;
    box-sizing: border-box;
    // border: solid 1px #ddd;
    border-radius: 0.5em;
    font-family: "Source Sans Pro", sans-serif;
    .title {
      font-size: 20px;
      line-height: 50px;
      font-weight: bold;
      margin: 10px;
      text-align: center;
    }
  .el-tabs__header {
      margin: 0 0 30px 0;
    }
    // /deep/ .el-tabs__item {
    //   font-size: 20px;
    //   text-align: center;
    // }
.el-tabs__nav-wrap::after {
      height: 0;
    }
#tab-first::after {
      content: "";
      position: absolute;
      right: 0;
      bottom: 0;
      width: 1px;
      height: 20px;
      background-color: #dcdfe6;
      margin: 8px 0;
      vertical-align: middle;
    }
    .code .el-form-item__content {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .code button {
      margin-left: 20px;
      width: 140px;
      text-align: center;
    }
    .el-form-item:last-child {
      margin-bottom: 6px;
    }
    .el-button--primary:focus {
      background: $btn-color;
      border-color: $btn-color;
      color: $white-bg-color;
    }
 .el-input__suffix-inner {
      margin-right: 6px;
    }
  }
  .login {
    margin-top: -15px;
    font-size: 12px;
    cursor: pointer;
    text-align: left;
    .gotoRight {
      float: right;
      color: #999999;
      &:hover {
        color: $btn-color;
      }
    }
  }
}
</style>