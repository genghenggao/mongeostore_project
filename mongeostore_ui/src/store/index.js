/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-03 21:26:19
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-19 14:44:41
 */
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    title_message: '地震大数据管理系统', //设置默认标题
    DBorCol: true //设置参数，判断是数据库还是集合
  },
  mutations: {},
  actions: {},
  modules: {}
});
