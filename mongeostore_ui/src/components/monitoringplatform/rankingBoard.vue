<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2021-01-08 19:25:55
 * @LastEditors: henggao
 * @LastEditTime: 2021-01-08 19:56:26
-->
<template>
  <div id="ranking-board">
    <div class="ranking-board-title">勘探数据记录数量</div>
    <dv-scroll-ranking-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'RankingBoard',
  data () {
    return {
      config: {
        data: [
          {
            name: '地理数据',
            value: 55
          },
          {
            name: '遥感数据',
            value: 120
          },
          {
            name: '钻孔数据',
            value: 78
          },
          {
            name: '测井数据',
            value: 66
          },
          {
            name: '地质数据',
            value: 80
          },
          {
            name: '地震数据',
            value: 500
          },
          {
            name: '用户数据',
            value: 0.029
          },
          {
            name: '其他数据',
            value: 29
          },
          {
            name: '历史数据',
            value: 29
          }
        ],
        rowNum: 9
      }
    }
  }
}
</script>

<style lang="less">
#ranking-board {
  width: 20%;
  box-shadow: 0 0 3px blue;
  display: flex;
  flex-direction: column;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  box-sizing: border-box;
  padding: 0px 30px;

  .ranking-board-title {
    font-weight: bold;
    height: 50px;
    display: flex;
    align-items: center;
    font-size: 20px;
  }

  .dv-scroll-ranking-board {
    flex: 1;
  }
}
</style>
