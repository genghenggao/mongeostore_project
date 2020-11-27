<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-27 09:37:21
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-27 15:50:38
-->
<template>
  <div>
    <h1>单张图片</h1>
    <br />

    <!-- <img src="data:image/jpeg;base64,{{ imagedata }}" /> -->
    <img
      src="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2605536016,3480752382&fm=11&gp=0.jpg"
      v-viewer
    />
    <br />
    <br />
    <h1>多张图片</h1>
    <br />
    <viewer :images="images">
      <!-- <img :src="image" />
       -->
      <img
        v-for="item in images"
        :src="item"
        :key="item"
        height="100"
        alt="图片"
      />
    </viewer>
    <h2>Mongodb图片</h2>
    <!-- <img src="data:image/png;base64,{{ imagedata }}" /> -->
    <img
      :src="'data:image/png;base64,' + ico"
      class="avatar"
      height="100"
      alt="图片名"
      v-viewer
    />
    <h2>Element图片展示</h2>

    <el-image
      style="width: 100px; height: 100px"
      :src="url"
      :preview-src-list="srcList"
    >
    </el-image>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Test5",
  data() {
    return {
      images: [
        "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3272199364,3404297250&fm=26&gp=0.jpg",
        "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3267295166,2381808815&fm=26&gp=0.jpg",
        "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3429654663,2972188411&fm=26&gp=0.jpg",
        "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3597323878,2962972725&fm=26&gp=0.jpg",
      ],
      ico: "",
      url:
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      srcList: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
        "https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg",
      ],
    };
  },
  created() {
    this.showimg();
  },
  methods: {
    showimg() {
      const url = "http://127.0.0.1:8000/load/listallimg/";
      axios
        .get(url)
        .then((res) => {
          // console.log(res.data);
          this.ico = res.data;
        })
        .catch((res) => {
          console.log("err");
        });
    },
  },
};
</script>

<style>
</style>