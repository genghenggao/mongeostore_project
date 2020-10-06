<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-28 20:21:57
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-06 20:52:42
-->
<template>
  <div class="fixed-bottom">
    <!-- <footer class="footer">
      友情链接：
      <a href="https://www.cumtb.edu.cn/">中国矿业大学（北京）</a>
      <span class="text-muted"> Copyright © 2020.中国矿业大学(北京)</span>
      <span class="text-muted"> 京公网安备：110402430067号</span>
      <span class="text-muted"> 学校地址：北京市海淀区学院路丁11号</span>
    </footer> -->
    <ul class="nav justify-content-center">
      <li class="nav-item">
        友情链接：
        <a href="https://www.cumtb.edu.cn/">中国矿业大学（北京）</a>
      </li>
      <li class="nav-item">
        <span class="text-muted"> Copyright © 2020.中国矿业大学(北京)</span>
      </li>
      <li class="nav-item">
        <span class="text-muted"> 京公网安备：110402430067号</span>
      </li>
      <li class="nav-item">
        <span class="text-muted"> 学校地址：北京市海淀区学院路丁11号</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Footbar",
  props: {
    msg: String
  }
};
</script>

<style>
.fixed-bottom {
  margin: 0px;
  padding: 0px;
  position: relative;
  /* bottom: 0; */
  width: 100%;
  /* Set the fixed height of the footer here */
  height: 30px;
  background-color: #f5f5f5;
  /* background: #4f5893; */
  /* color: #e7e7e7; */
  opacity: 0.3;
  filter: alpha(opacity=100);
  /* 针对 IE8 以及更早的版本 */
}
</style>