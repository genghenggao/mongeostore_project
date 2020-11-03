<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-03 15:11:11
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-03 16:24:13
-->
<template>
  <!-- 主界面-->
  <div class="maincontent">
    <!-- 子导航 -->
    <nav>
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <a
          class="nav-item nav-link active"
          id="nav-home-tab"
          data-toggle="tab"
          href="#nav-home"
          role="tab"
          aria-controls="nav-home"
          aria-selected="true"
          >Home</a
        >
        <a
          class="nav-item nav-link"
          id="nav-profile-tab"
          data-toggle="tab"
          href="#nav-profile"
          role="tab"
          aria-controls="nav-profile"
          aria-selected="false"
          >Profile</a
        >
        <a
          class="nav-item nav-link"
          id="nav-metadata-tab"
          data-toggle="tab"
          href="#nav-metadata"
          role="tab"
          aria-controls="nav-metadata"
          aria-selected="false"
          >MetaData</a
        >
        <a
          class="nav-item nav-link"
          id="nav-uploadfile-tab"
          data-toggle="tab"
          href="#nav-uploadfile"
          role="tab"
          aria-controls="nav-uploadfile"
          aria-selected="false"
          >UploadFile</a
        >
      </div>
    </nav>
    <div class="tab-content" id="nav-tabContent">
      <div
        class="tab-pane fade show active"
        id="nav-home"
        role="tabpanel"
        aria-labelledby="nav-home-tab"
      >
        <MapView />
      </div>

      <div
        class="tab-pane fade"
        id="nav-profile"
        role="tabpanel"
        aria-labelledby="nav-profile-tab"
      >
        <Home />
      </div>
      <div
        class="tab-pane fade"
        id="nav-metadata"
        role="tabpanel"
        aria-labelledby="nav-metadata-tab"
      >
        <SeiTable />
      </div>
      <div
        class="tab-pane fade"
        id="nav-uploadfile"
        role="tabpanel"
        aria-labelledby="nav-uploadfile-tab"
      >
        <UploadFile />
      </div>
    </div>
  </div>
</template>

<script>
import MapView from "@/views/MapView.vue";
import Home from "@/views/Home.vue";
import UploadFile from "@/views/UploadFile.vue";
import SeiTable from "@/components/SeiTable.vue";
export default {
  name: "MainContent",
  components: {
    MapView,
    Home,
    SeiTable,
    UploadFile
  },
  data() {
    return {
      activeIndex: "1"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<style>
</style>