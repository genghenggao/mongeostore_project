<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-06 15:35:53
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-27 10:13:19
-->
<template>
  <div>
    <form action="">
      商品图片：<input type="file" id="img" /><br />
      <button type="submit" @click.prevent="on_sumit">添加</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {};
  },
  methods: {
    on_sumit() {
      let form_data = new FormData(); // 需要添加其他字段时用这一步，只上传文件则不需要
      var img = document.getElementById("img").files[0];
      form_data.append("image", img, img.name); // 这里的image和后台views视图文件里获取时的名字要一样，否则获取不到,详情看下面的views 视图文件
      axios({
        url: "http://127.0.0.1:8000/api/uploadfile/",
        method: "get",
        data: form_data,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {
        console.log(res);
      });
    }
  }
};
</script>