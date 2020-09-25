<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-25 17:06:12
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-25 17:29:16
-->
<template>
  <el-card>
    <div class="page-slidecode">
      <slide-verify
          :l="42"
          :r="10"
          :w="310"
          :h="155"
          :imgs="bgimgs"
          @success="onSuccess"
          @fail="onFail"
          @refresh="onRefresh"
          :slider-text="text"
        ></slide-verify>
        <div>{{msg}}</div>
    </div>
  </el-card>
</template>

<script>
import aa from "@/assets/images/aa.jpg"	//	如果使用网络图片资源就无需引入
// import bb from "@/assets/images/bb.jpg"	//	如果使用网络图片资源就无需引入
// import cc from "@/assets/images/cc.jpg"	//	如果使用网络图片资源就无需引入
// import dd from "@/assets/images/dd.jpg"	//	如果使用网络图片资源就无需引入
// import ee from "@/assets/images/ee.jpg"	//	如果使用网络图片资源就无需引入
export default {
  data() {
    return {
      msg: "",
      bgimgs:[ aa,],
    //   bgimgs:[ aa, bb, cc, dd, ee, ],
    //   bgimgs:[],	//	如果使用网络图片资源就用该值
      text: "向右滑动~"
    };
  },
  methods: {
    onSuccess() {
      this.msg = "登录成功~";
    },
    onFail() {
      this.msg = "登录失败！";
    },
    onRefresh() {
      this.msg = "重新生成验证码";
    }
  }
};
</script>
