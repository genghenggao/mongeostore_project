<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 15:37:36
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-24 09:51:23
-->
<template>
  <div>
    <div>
      <h2 style="color: #810000; padding-top: 30px">地震剖面图信息</h2>
    </div>
    <div class="content">
      <img src="@/assets/images/LX_SEGY001.jpg" alt="" />
    </div>
  </div>
</template>

<script>
export default {
  name: "SeismicProfile",
};
</script>

<style lang="scss" scoped>
.content img {
  padding-top: 50px;
  width: 800px;
  height: 600px;
}
</style>