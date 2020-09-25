/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-26 17:15:17
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-25 17:25:42
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
    path: "/test",
    name: "Tset",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Test.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
