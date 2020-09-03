/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-29 16:00:58
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-01 10:45:26
 */
const webpack = require('webpack');
const path = require('path');  //引入path模块（node）
const resolve = (dir) => path.join(__dirname, dir); //将文件组成绝对路径

module.exports = {
  // 用于引入jquery开始
  lintOnSave: false,
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
        Popper: ['popper.js', 'default']
      })
    ]
  },
  // 用于引入jquery结束
  publicPath: '/',
  // 输出文件目录
  outputDir: 'dist',
  assetsDir: 'static',
  lintOnSave: false,// 关闭eslint
  // webpack相关配置
  chainWebpack: (config) => {
    config.resolve.symlinks(true) //热更新
  },
}