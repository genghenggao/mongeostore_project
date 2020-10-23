<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-21 14:30:16
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-23 10:27:09
-->
<template>
  <uploader :options="options" class="uploader-example">
    <uploader-unsupport></uploader-unsupport>
    <uploader-drop>
      <p>Drop files here to upload or</p>
      <uploader-btn>select files</uploader-btn>
      <uploader-btn :attrs="attrs">select images</uploader-btn>
      <uploader-btn :directory="true">select folder</uploader-btn>
    </uploader-drop>
    <uploader-list></uploader-list>
  </uploader>
</template>

<script>
export default {
  data() {
    return {
      options: {
        // https://github.com/simple-uploader/Uploader/tree/develop/samples/Node.js
        // target: '//localhost:3000/upload',
        target: "http://127.0.0.1:8000/api/uploadinfo",
        testChunks: false,
        // headers: { "Content-Type": "application/x-www-form-urlencoded" }
      },
      attrs: {
        accept: "image/*"
      }
    };
  }
};
</script>

<style>
.uploader-example {
  width: 880px;
  padding: 15px;
  margin: 40px auto 0;
  font-size: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
}
.uploader-example .uploader-btn {
  margin-right: 4px;
}
.uploader-example .uploader-list {
  max-height: 440px;
  overflow: auto;
  overflow-x: hidden;
  overflow-y: auto;
}
</style>