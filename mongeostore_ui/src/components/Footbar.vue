<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-28 20:21:57
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-28 20:24:41
-->
<template>
  <div>
    <ul class="nav justify-content-center">
      <li class="nav-item">
        <a class="nav-link active" href="#">Active</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"
          >Disabled</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "FootBar",
  props: {
    msg: String
  }
};
</script>

<style>
</style>