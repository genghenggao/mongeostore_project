/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2021-03-29 21:24:03
 */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Segy from "@/views/Segy.vue";
import Login from "@/views/Login.vue";

Vue.use(VueRouter);

// 避冗余导航
const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
// 路由
const routes = [
  {
    path: "/home",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Register.vue")
  },
  {
    path: "/segy",
    name: "Segy",
    component: Segy
    // component: () =>
    // import(/* webpackChunkName: "about" */ "../views/Segy.vue")
  },
  {
    path: "/login",
    name: "Login",
    component: Login
    // component: () =>
    // import(/* webpackChunkName: "about" */ "../views/Segy.vue")
  },
  {
    path: "/404",
    name: "NotFound",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/404.vue")
  },
  {
    path: "/homepage",
    name: "HomePage",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/HomePage.vue")
  },
  {
    path: "/homepage1",
    name: "HomePage1",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/HomePage1.vue"),
    children: [
      {
        path: "/maincontent",
        name: "MainContent",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/MainContent.vue")
      }]
  },
  {
    path: "/test",
    name: "Test",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Test.vue")
  },
  {
    path: "/test2",
    name: "Test2",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Test2.vue")
  },
  {
    path: "/test3",
    name: "Test3",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Test3.vue")
  },
  {
    path: "/test5",
    name: "Test5",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/Test5.vue")
  },
  {
    path: "/test6",
    name: "Test6",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/Test6.vue")
  },
  // 监控页面
  {
    path: "/monitor",
    name: "monitor",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/components/monitoringplatform/index.vue")
  },
  {
    path: "/mapview",
    name: "MapView",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/MapView.vue")
  },
  {
    path: "/uploadfile",
    name: "UploadFile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/UploadFile.vue")
  },
  {
    path: "/uploadcsv",
    name: "UploadCSV",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/UploadCSV.vue")
  },
  {
    path: "/uploadexcel",
    name: "UploadExcel",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/UploadExcel.vue")
  },
  {
    path: "/downloadfile",
    name: "DownloadFile",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DownloadFile.vue")
  },
  {
    path: "/uploadfile2",
    name: "Uploadfile2",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Uploadfile2.vue")
  },
  // 关于MonGeoStore设置
  {
    path: "/mongeostorehome",
    // path: "/",
    name: "MonGeoStoreHome",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/MonGeoStoreHome.vue")
  },
  // 关于MonGeoStore设置
  {
    path: "/sidecatalog",
    name: "SideCatalog",
    component: () =>
      import(/* webpackChunkName: "about" */ "../components/SideCatalog.vue")
  },
  // 关于SpatialIndex 天地图
  {
    path: "/spatialindex",
    name: "SpatialIndex",
    component: () =>
      import(/* webpackChunkName: "about" */ "../components/drill/SpatialIndex.vue")
  },
  {
    path: "/mongeostore",
    name: "MonGeoStore",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/MonGeoStore.vue"),
    children: [
      // 钻孔元数据
      {
        path: "drillmetahome",
        name: "DrillMetaHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/drill/DrillMetaHome.vue")
      },
      {
        path: "drillmetadata",
        name: "DrillMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/drill/DrillMetaData.vue")
      },
      {
        // path: "drilldetails/:_id",
        path: "drilldetails/:zk_num",
        name: "DrillDetails",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/drill/DrillDetails.vue")
      },
      {
        path: "drillupload",
        name: "DrillUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/drill/DrillUpload.vue")
      },
      // 钻孔定位表主页
      {
        path: "drilllocationhome",
        name: "DrillLocationHome",
        component: () =>
          import("@/components/drill/DrillLocationHome.vue")
      },
      // 钻孔定位表数据
      {
        path: "drilllocationdata",
        name: "DrillLocationData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/drill/DrillLocationData.vue")
      },
      // 地震首页
      {
        path: "seismichome",
        name: "SeismicHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicHome.vue")
      },
      // 地震数据信息
      {
        path: "seismicdatainfo",
        name: "seismicdatainfo",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicDataInfo.vue")
      },
      // 地震数据
      {
        path: "seismicmetadata",
        name: "SeismicMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicMetaData.vue")
      },
      // 地震剖面图
      {
        path: "seismicprofile",
        name: "SeismicProfile",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicProfile.vue")
      },
      // 地震数据解析
      {
        path: "seismicanalysis",
        name: "SeismicAnalysis",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicAnalysis.vue")
      },
      // 地震数据上传
      {
        path: "seismicupload",
        name: "SeismicUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeismicUpload.vue")
      },
      // 地理数据首页
      {
        path: "geographicalhome",
        name: "GeographicalHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geographical/GeographicalHome.vue")
      },
      // 地理信息
      {
        path: "geographicalmap",
        name: "GeographicalMap",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geographical/GeographicalMap.vue")
      },
      // 地理数据
      {
        path: "geographicalview",
        name: "GeographicalView",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geographical/GeographicalView.vue")
      },
      // 遥感首页
      {
        path: "remotehome",
        name: "RemoteHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/remote_sensing/RemoteHome.vue")
      },
      // 遥感元数据
      {
        path: "remotemetadata",
        name: "RemoteMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/remote_sensing/RemoteMetaData.vue")
      },
      // 遥感上传
      {
        path: "remoteupload",
        name: "RemoteUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/remote_sensing/RemoteUpload.vue")
      },
      // 测井首页
      {
        path: "logginghome",
        name: "LoggingHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/logging/LoggingHome.vue")
      },
      // 测井元数据
      {
        path: "loggingmetadata",
        name: "LoggingMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/logging/LoggingMetaData.vue")
      },
      // 测井上传
      {
        path: "loggingupload",
        name: "LoggingUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/logging/LoggingUpload.vue")
      },
      // 地质首页
      {
        path: "geologicalhome",
        name: "GeologicalHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geological/GeologicalHome.vue")
      },
      // 地质元数据
      {
        path: "geologicalmetadata",
        name: "GeologicalMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geological/GeologicalMetaData.vue")
      },
      // 地质上传
      {
        path: "geologicalupload",
        name: "GeologicalUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/geological/GeologicalUpload.vue")
      },
      // 水文首页
      {
        path: "hydrologicalhome",
        name: "HydrologicalHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/hydrological/HydrologicalHome.vue")
      },
      // 水文元数据
      {
        path: "hydrologicalmetadata",
        name: "HydrologicalMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/hydrological/HydrologicalMetaData.vue")
      },
      // 水文上传
      {
        path: "hydrologicalupload",
        name: "HydrologicalUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/hydrological/HydrologicalUpload.vue")
      },
      // 地震采集首页
      {
        path: "seiAcquisitionhome",
        name: "seiAcquisitionHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiAcquisitionHome.vue")
      },
      // 地震采集元数据
      {
        path: "seiAcquisitionmetadata",
        name: "SeiAcquisitionMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiAcquisitionMetaData.vue")
      },
      // 地震采集上传
      {
        path: "seiAcquisitionupload",
        name: "SeiAcquisitionUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiAcquisitionUpload.vue")
      },
      // 地震处理首页
      {
        path: "seiprocesshome",
        name: "SeiprocessHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiprocessHome.vue")
      },
      // 地震处理元数据
      {
        path: "seiprocessmetadata",
        name: "SeiprocessMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiprocessMetaData.vue")
      },
      // 地震处理上传
      {
        path: "seiprocessupload",
        name: "SeiprocessUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiprocessUpload.vue")
      },
      // 地震解释首页
      {
        path: "seiInterpretationhome",
        name: "SeiInterpretationHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiInterpretationHome.vue")
      },
      // 地震处理元数据
      {
        path: "seiInterpretationmetadata",
        name: "SeiInterpretationMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiInterpretationMetaData.vue")
      },
      // 地震处理上传
      {
        path: "seiInterpretationupload",
        name: "seiInterpretationUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeiInterpretationUpload.vue")
      },
      // 地震历史首页
      {
        path: "seihistoricalhome",
        name: "SeihistoricalHome",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeihistoricalHome.vue")
      },
      // 地震历史元数据
      {
        path: "seihistoricalmetadata",
        name: "SeihistoricalMetaData",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeihistoricalMetaData.vue")
      },
      // 地震历史上传
      {
        path: "seihistoricalupload",
        name: "SeihistoricalUpload",
        component: () =>
          import(/* webpackChunkName: "about" */ "@/components/seismic/SeihistoricalUpload.vue")
      },
    ]
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
