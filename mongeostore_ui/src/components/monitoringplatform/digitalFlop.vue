<template>
  <div id="digital-flop">
    <div
      class="digital-flop-item"
      v-for="item in digitalFlopData"
      :key="item.title"
    >
      <div class="digital-flop-title">{{ item.title }}</div>
      <div class="digital-flop">
        <dv-digital-flop
          :config="item.number"
          style="width: 100px; height: 50px"
        />
        <div class="unit">{{ item.unit }}</div>
      </div>
    </div>

    <dv-decoration-10 />
  </div>
</template>

<script>
export default {
  name: "DigitalFlop",
  data() {
    return {
      digitalFlopData: [],
    };
  },
  methods: {
    createData() {
      const { randomExtend } = this;

      this.digitalFlopData = [
        {
          title: "平台总量",
          number: {
            number: [randomExtend(2000, 3000)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#4d99fc",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "地理数据",
          number: {
            number: [randomExtend(200, 300)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#f46827",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "地质数据",
          number: {
            number: [randomExtend(200, 300)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#40faee",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "遥感数据",
          number: {
            number: [randomExtend(100, 200)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#4d99fc",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "钻孔数据",
          number: {
            number: [randomExtend(100, 200)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#f46827",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "测井数据",
          number: {
            number: [randomExtend(200, 400)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#40faee",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "地震数据",
          number: {
            number: [randomExtend(1000, 2000)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#4d99fc",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
        {
          title: "用户数据",
          number: {
            number: [randomExtend(10, 50)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#f46827",
              fontWeight: "bold",
            },
          },
          unit: "GB",
        },
        {
          title: "其他数据",
          number: {
            number: [randomExtend(150, 550)],
            content: "{nt}",
            textAlign: "right",
            style: {
              fill: "#40faee",
              fontWeight: "bold",
            },
          },
          unit: "TB",
        },
      ];
    },
    randomExtend(minNum, maxNum) {
      if (arguments.length === 1) {
        return parseInt(Math.random() * minNum + 1, 10);
      } else {
        return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
      }
    },
  },
  mounted() {
    const { createData } = this;

    createData();

    setInterval(createData, 30000);
  },
};
</script>

<style lang="less">
#digital-flop {
  position: relative;
  height: 15%;
  flex-shrink: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(6, 30, 93, 0.5);

  .dv-decoration-10 {
    position: absolute;
    width: 95%;
    left: 2.5%;
    height: 5px;
    bottom: 0px;
  }

  .digital-flop-item {
    width: 11%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-left: 3px solid rgb(6, 30, 93);
    border-right: 3px solid rgb(6, 30, 93);
  }

  .digital-flop-title {
    font-size: 20px;
    margin-bottom: 20px;
  }

  .digital-flop {
    display: flex;
  }

  .unit {
    margin-left: 10px;
    display: flex;
    align-items: flex-end;
    box-sizing: border-box;
    padding-bottom: 13px;
  }
}
</style>
