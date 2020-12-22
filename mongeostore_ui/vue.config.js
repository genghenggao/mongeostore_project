/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-29 16:00:58
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-22 21:42:56
 */
const webpack = require('webpack');
const path = require('path');  //引入path模块（node）
const resolve = (dir) => path.join(__dirname, dir); //将文件组成绝对路径

module.exports = {
  // ico图标设置
  pwa: {
    iconPaths: {
      favicon32: 'favicon.ico',
      favicon16: 'favicon.ico',
      appleTouchIcon: 'favicon.ico',
      maskIcon: 'favicon.ico',
      msTileImage: 'favicon.ico'
    }
  },

  // 跨域配置
  devServer: {
    open: true,
    host: 'localhost',
    port: 8080,
    https: false,
    //以上的ip和端口是我们本机的;下面为需要跨域的
    proxy: {//配置跨域
      '/api': {
        target: 'http://127.0.0.1:8000/api/',//这里后台的地址模拟的;应该填写你们真实的后台接口
        ws: true,
        changOrigin: true,//允许跨域
        pathRewrite: {
          '^/api': ''//请求的时候使用这个api就可以
        }
      }

    }
  },

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