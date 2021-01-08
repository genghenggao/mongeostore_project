<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2021-01-08 19:25:55
 * @LastEditors: henggao
 * @LastEditTime: 2021-01-08 19:52:22
-->
<template>
  <div id="scroll-board">
    <dv-scroll-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'ScrollBoard',
  data () {
    return {
      config: {
        header: ['时间', '数据信息', '数量', '区域'],
        data: [
          ['2019-07-01 19:25:00', '区域A-钻孔数据', '105', 'xxxxxxx'],
          ['2019-07-02 17:25:00', '区域B-地理数据', '113', 'xxxxxxx'],
          ['2019-07-03 16:25:00', '区域C-地质数据', '360', 'xxxxxxx'],
          ['2019-07-04 15:25:00', '区域C-地震数据', '200', 'xxxxxxx'],
          ['2019-07-05 14:25:00', '注册用户数据', '10', 'xxxxxxx'],
          ['2019-07-06 13:25:00', '其他数据', '3', 'xxxxxxx'],
          ['2019-07-07 12:25:00', '区域A-遥感数据', '400', 'xxxxxxx'],
          ['2019-07-08 11:25:00', '区域D-地震数据', '200', 'xxxxxxx'],
          ['2019-07-09 10:25:00', '区域B-地震数据', '500', 'xxxxxxx'],
          ['2019-07-10 09:25:00', '区域A-测井数据', '365', 'xxxxxxx']
        ],
        index: true,
        columnWidth: [50, 170, 300],
        align: ['center'],
        rowNum: 7,
        headerBGC: '#1981f6',
        headerHeight: 45,
        oddRowBGC: 'rgba(0, 44, 81, 0.8)',
        evenRowBGC: 'rgba(10, 29, 50, 0.8)'
      }
    }
  }
}
</script>

<style lang="less">
#scroll-board {
  width: 50%;
  box-sizing: border-box;
  margin-left: 20px;
  height: 100%;
  overflow: hidden;
}
</style>
