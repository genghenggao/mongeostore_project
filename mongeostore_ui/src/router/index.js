/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-18 20:12:11
 */
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Segy from "@/views/Segy.vue";
import Login from "@/views/Login.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
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
    path: "/sidecatalog",
    name: "SideCatalog",
    component: () =>
      import(/* webpackChunkName: "about" */ "../components/SideCatalog.vue")
  },
  {
    path: "/mongeostore",
    name: "MonGeoStore",
    component: () =>
      import(/* webpackChunkName: "about" */ "@/views/MonGeoStore.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
