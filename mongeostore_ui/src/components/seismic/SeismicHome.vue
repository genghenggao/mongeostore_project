<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 10:41:26
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-16 18:43:53
-->
<template>
  <el-container style="min-width: 1100px; overflow: hidden">
    <el-header>
      <h2
        style="
          font-size: 30px;
          padding-top: 10px;
          color: #870000;
          min-width: 1100px;
          overflow: hidden;
          text-align: left;
        "
      >
        <i class="el-icon-caret-right" /> 地震数据信息
      </h2>
    </el-header>
    <el-main style="padding-top: 10px; min-width: 1100px; overflow: hidden">
      <!-- <div style="">
        <h3>钻孔编号：{{ ZK_num }}</h3>
      </div> -->
      <el-row :gutter="20" style="margin: 0">
        <el-col :span="16" :offset="4">
          <el-tabs :tab-position="tabPosition">
            <el-tab-pane label="地震道头信息">
              <div>
                <el-collapse v-model="activeNames" @change="handleChange">
                  <el-scrollbar style="height: 720px">
                    <el-collapse-item title="道头信息TraceHeader" name="1">
                      <div>
                        <el-card
                          shadow="hover"
                          :body-style="{ padding: '0px' }"
                        >
                          <img
                            src="@/assets/images/seismicprofile.jpg"
                            class="image"
                          />
                          <div style="padding: 14px">
                            <pre>
    C 1 SEGY OUTPUT FROM Petrel 2013.2 (64-bit) Wednesday, October 17 2018 12:37:30
    C 2 Name: LX_mig2 \xd5Crop\xe5 1 Type: 3D seismic                              
    C 3                                                                            
    C 4 First inline: 730    Last inline: 1790                                     
    C 5 First xline:  200    Last xline:  440                                      
     C 6 CRS: Undefined                                                              
    C 7 X min: 472427.00 max: 477247.00 delta: 4820.00                             
    C 8 Y min: 4216434.00 max: 4237654.00 delta: 21220.00                          
    C 9 Time min: -2000.50 max: 0.50 delta: 2001.00                                
    C10 Lat min: - max: - delta: -                                                 
    C11 Long min: - max: - delta: -                                                
    C12 Trace min: -2000.00 max: 0.00 delta: 2000.00                               
    C13 Seismic (template) min: ~-245391.69 max: ~208256.25 delta: ~453647.94      
    C14 Amplitude (data) min: ~-245391.69 max: ~208256.25 delta: ~453647.94        
    C15 Trace sample format: IBM floating point                                    
    C16 Coordinate scale factor00000                                               
    C17                                                                            
    C18 Binary healocations:                                                       
    C19 Sample interval             : by17-18                                      
    C20 Number of samples per trace : by21-22                                      
    C21 Trace date format           : by25-26                                      
    C22                                                                            
    C23 Trace healocations:                                                        
    C24 Inline number               : by5-8                                        
    C25 Xline number                : by21-24                                      
    C26 Coordinate scale factor     : bytes 71-72                                  
    C27 X coordinate                : bytes 73-76                                  
    C28 Y coordinate                : bytes 77-80                                  
    C29 Trace start time/depth      : bytes 109-110                                
    C30 Number of samples per trace : bytes 115-116                                
    C31 Sample interval             : bytes 117-118                                
    C32                                                                            
    C33                                                                            
    C34                                                                            
    C35                                                                            
    C36                                                                            
    C37                                                                            
    C38                                                                            
    C39                                                                            
    C40 END EBCDIC                                                                 
                            </pre>
                          </div>
                        </el-card>
                      </div>
                    </el-collapse-item>
                    <el-collapse-item title="卷头信息TraceText" name="2">
                      <img
                        src="@/assets/images/seismicprofile.jpg"
                        class="image"
                      />
                      <div style="text-align: left; padding: 14px">
                        C 1 SEGY OUTPUT FROM Petrel 2013.2 (64-bit) Wednesday,
                        October 17 2018 12:37:30 <br />
                        C 2 Name: LX_mig2 \xd5Crop\xe5 1 Type: 3D seismic <br />
                        C 3 <br />
                        C 4 First inline: 730 Last inline: 1790 <br />
                        C 5 First xline: 200 Last xline: 440 <br />
                        C 6 CRS: Undefined <br />
                        C 7 X min: 472427.00 max: 477247.00 delta: 4820.00
                        <br />
                        C 8 Y min: 4216434.00 max: 4237654.00 delta: 21220.00
                        <br />
                        C 9 Time min: -2000.50 max: 0.50 delta: 2001.00 <br />
                        C10 Lat min: - max: - delta: - <br />
                        C11 Long min: - max: - delta: - <br />
                        C12 Trace min: -2000.00 max: 0.00 delta: 2000.00 <br />
                        C13 Seismic (template) min: ~-245391.69 max: ~208256.25
                        delta: ~453647.94 <br />
                        C14 Amplitude (data) min: ~-245391.69 max: ~208256.25
                        delta: ~453647.94 <br />
                        C15 Trace sample format: IBM floating point <br />
                        C16 Coordinate scale factor: 1.00000 <br />
                        C17 <br />
                        C18 Binary header locations: <br />
                        C19 Sample interval : bytes 17-18 <br />
                        C20 Number of samples per trace : bytes 21-22 <br />
                        C21 Trace date format : bytes 25-26 <br />
                        C22 <br />
                        C23 Trace header locations: <br />
                        C24 Inline number : bytes 5-8 <br />
                        C25 Xline number : bytes 21-24 <br />
                        C26 Coordinate scale factor : bytes 71-72 <br />
                        C27 X coordinate : bytes 73-76 <br />
                        C28 Y coordinate : bytes 77-80 <br />
                        C29 Trace start time/depth : bytes 109-110 <br />
                        C30 Number of samples per trace : bytes 115-116 <br />
                        C31 Sample interval : bytes 117-118 <br />
                        C32 <br />
                        C33 <br />
                        C34 <br />
                        C35 <br />
                        C36 <br />
                        C37 <br />
                        C38 <br />
                        C39 <br />
                        C40 END EBCDIC <br />
                      </div>
                    </el-collapse-item>
                    <el-collapse-item title="其他信息Bin" name="3">
                      <el-card shadow="hover">
                        <div>
                          {JobID: 1, LineNumber: 1, ReelNumber: 1, Traces: 1,
                          AuxTraces: 0, Interval: 1000, IntervalOriginal: 0,
                          Samples: 2001, SamplesOriginal: 0, Format: 1,
                          EnsembleFold: 1, SortingCode: 4, VerticalSum: 1,
                          SweepFrequencyStart: 0, SweepFrequencyEnd: 0,
                          SweepLength: 0, Sweep: 0, SweepChannel: 0,
                          SweepTaperStart: 0, SweepTaperEnd: 0, Taper: 0,
                          CorrelatedTraces: 0, BinaryGainRecovery: 0,
                          AmplitudeRecovery: 0, MeasurementSystem: 1,
                          ImpulseSignalPolarity: 1, VibratoryPolarity: 0,
                          SEGYRevision: 0, TraceFlag: 0, ExtendedHeaders: 0}
                        </div>
                      </el-card>
                    </el-collapse-item>
                    <el-collapse-item title="可控 Controllability" name="4">
                      <div>
                        用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；
                      </div>
                      <div>
                        结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。
                      </div>
                    </el-collapse-item>
                  </el-scrollbar>
                </el-collapse>
              </div>
            </el-tab-pane>
            <el-tab-pane label="地震卷头信息">
              <ProjectInfoUpload />
            </el-tab-pane>
            <el-tab-pane label="单位信息上传">
              <CompanyInfoUpload />
            </el-tab-pane>
            <el-tab-pane label="其他信息上传">其他信息上传</el-tab-pane>
          </el-tabs>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from "axios";
import DrillMetaUpload from "@/components/drill/DrillMetaUpload.vue";
import ProjectInfoUpload from "@/components/drill/ProjectInfoUpload.vue";
import CompanyInfoUpload from "@/components/drill/CompanyInfoUpload.vue";
export default {
  name: "SeismicHome",
  components: {
    DrillMetaUpload,
    ProjectInfoUpload,
    CompanyInfoUpload,
  },
  data() {
    return {
      // 折叠面板
      activeNames: ["1"],
      // 柱状图
      url:
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      srcList: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
        "https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg",
      ],
      tabPosition: "right", //标签页位置设置
      tableData: {
        钻孔编号: "	ZK2",
        // 钻孔柱状图: "浏览",
        钻孔柱状图: "浏览",
        原始资料档号: "2010091",
        勘探线号: "1-1",
        钻孔名称: "ZK2",
        钻孔类型: "灾害地质勘查钻孔",
        钻孔位置: "广元市剑阁县上寺乡",
        孔口高程H: "608.6",
        终孔深度Z: "	16.94",
        终孔日期: "2010/4/2",
        施工单位: "重庆长江工程勘察设计研究院",
        测井报告: "无",
        原始地质记录表: "有",
        钻孔岩心: "无",
      },
      ProjectInformation: {
        项目名称: "广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查",
        资料名称: "广元市剑阁县上寺乡望牛石不稳定斜坡（滑坡）应急勘查报告",
        成果资料档号: "	aa548",
        项目结束时间: "	2010/4/25",
      },
      FileInformation: {
        上传人员: "ghg",
        上传日期: "2020/11/11",
        单位名称: "中国矿业大学（北京）",
        通讯地址: "北京市海淀区学院路丁11号",
      },

      search: "", //搜索框
      // 分页数据，默认第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 100,
      // 个数选择器（可修改）
      pageSizes: [10, 20, 50, 100],
      // 默认每页显示的条数（可修改)
      PageSize: 10,
      //   图片
      imgurl:
        "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      srcList: [
        "https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg",
        "https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg",
      ],
    };
  },
  created() {
    this.showMetaData();
    // this.tableData = JSON.parse(JSON.stringify(this.tableData));
  },
  methods: {
    //   折叠面板
    handleChange(val) {
      console.log(val);
    },
    showMetaData() {
      console.log(typeof this.tableData);
      console.log(this.tableData);
      // let url = "http://127.0.0.1:8000/load/commonmetashow/";
      // axios
      //   .get(url, {
      //     params: {
      //       // 每页显示的条数
      //       PageSize: n1,
      //       // 显示第几页
      //       currentPage: n2,
      //     },
      //   })
      //   .then((res) => {
      //     console.log("success");
      //     console.log(res.data);
      //   })
      //   .catch((err) => {
      //     console.log("err");
      //   });
    },
  },
};
</script>

<style  lang='scss' scoped>
.myTable {
  border-collapse: collapse;
  margin: 0 auto;
  text-align: center;
}

.myTable td,
.myTable th {
  border: 1px solid #cad9ea;
  color: #666;
  height: 60px;
  width: 450px;
  padding-top: 20px; //设置文字居中
}
.el-scrollbar__wrap {
  overflow-x: hidden; //设置滚动条隐藏
}
</style>