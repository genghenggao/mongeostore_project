<template>
  <el-form ref="form" :model="form" label-width="100px">
    <el-form-item label="钻孔编号">
      <el-input v-model="form.zk_num"></el-input>
    </el-form-item>
    <el-form-item label="钻孔类型">
      <el-input v-model="form.zk_type"></el-input>
    </el-form-item>
    <el-form-item label="钻孔深度">
      <el-input v-model="form.final_depth"></el-input>
    </el-form-item>
    <el-form-item label="终孔时间">
      <el-date-picker
        type="date"
        placeholder="选择日期"
        v-model="form.final_date"
        style="width: 100%"
      ></el-date-picker
    ></el-form-item>

    <el-form-item label="项目名称">
      <el-input v-model="form.project_name"></el-input>
    </el-form-item>
    <el-form-item label="单位名称">
      <el-input v-model="form.company_name"></el-input>
    </el-form-item>
    <el-form-item label="上传人员">
      <el-input v-model="form.uploader"></el-input>
    </el-form-item>
    <el-form-item label="上传时间">
      <el-date-picker
        type="date"
        placeholder="选择日期"
        v-model="form.uploaddate"
        style="width: 100%"
      ></el-date-picker
    ></el-form-item>

    <el-form-item label="钻孔柱状图">
      <el-row>
        <el-button ref="VideoChose" id="VideoChose" size="medium "
          >选择文件</el-button
        >
      </el-row>
      <el-card style="margin-top: 20px">
        <el-table :data="fileList" style="width: 100%">
          <el-table-column prop="id" label="文件id"></el-table-column>
          <el-table-column prop="name" label="文件名称"></el-table-column>
          <el-table-column prop="type" label="文件类型"></el-table-column>
          <el-table-column prop="size" label="文件大小" v-slot="{ row }">
            {{ row.size }}MB
          </el-table-column>
          <el-table-column label="进度" v-slot="{ row }">
            <el-progress
              :text-inside="true"
              :stroke-width="16"
              :percentage="row.percentage"
            ></el-progress>
          </el-table-column>
          <el-table-column label="取消上传" v-slot="{ row }">
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              circle
              @click="removeFile(row.id)"
            ></el-button>
          </el-table-column>
          <el-table-column label="上传状态" v-slot="{ row }">
            <el-link
              :type="
                row.loadType == 0
                  ? 'info'
                  : row.loadType == 1
                  ? 'warning'
                  : row.loadType == 2
                  ? 'success'
                  : 'danger'
              "
              :underline="false"
              >{{
                row.loadType == 0
                  ? "等待上传"
                  : row.loadType == 1
                  ? "正在上传"
                  : row.loadType == 2
                  ? "上传成功"
                  : "上传失败"
              }}</el-link
            >
          </el-table-column>
        </el-table>
      </el-card>
    </el-form-item>
    <el-form-item>
      <el-button
        ref="VideoChose"
        type="primary"
        size="medium  "
        @click="onSubmit"
        >提交</el-button
      >
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import plupload from "plupload";
import axios from "axios";
import { stringify } from "qs";
export default {
  name: "UploadFile",
  data() {
    return {
      form: {
        zk_num: "",
        zk_type: "",
        final_depth: "",
        final_date: "",
        depth: "",
        project_name: "",
        company_name: "",
        uploader: "",
        uploaddate: "",
      },
      show: false,
      fileList: [],
      fileOptions: {
        browse_button: "VideoChose",
        // url: "http://127.0.0.1:8000/load/uploadfile/",
        url: "http://127.0.0.1:8000/load/drillmeta/",
        flash_swf_url: "script/Moxie.swf",
        silverlight_xap_url: "script/Moxie.xap",
        // chunk_size: "10mb", //分块大小  ,注销掉或者改chunk_size：'0mb'为解决文件大于10M存为blob问题
        max_retries: 3,
        unique_names: true,
        multi_selection: false, //是否允许选择多文件
        views: {
          list: true,
          thumbs: true, // Show thumbs
          active: "thumbs",
        },
        filters: {
          mime_types: [
            //文件格式
            {
              title: "files",
              extensions:
                // "png,jpg,svg,mp4,rmvb,mpg,mxf,avi,mpeg,wmv,flv,mov,ts,docx,doc,pdf,segy,xls,xlsx,csv", //文件格式
                "png,jpg",
            },
          ],
          max_file_size: "10240mb", //最大上传的文件
          prevent_duplicates: true, //不允许选取重复文件
        },
        multipart_params: {
          uuid: "", //参数
          // testparams: "Must can see me",
          // "testparams2": "Must can see me2"
        },
      },
    };
  },

  mounted() {
    //实例化一个plupload上传对象
    this.uploader.init();
    //绑定进队列
    this.uploader.bind("FilesAdded", this.FilesAdded);
    //绑定进度
    this.uploader.bind("UploadProgress", this.UploadProgress);
    //上传之前
    this.uploader.bind("BeforeUpload", this.BeforeUpload);
    //上传成功监听
    this.uploader.bind("FileUploaded", this.FileUploaded);
    //获取uuid
    // let url = `http://127.0.0.1:8000/api/uploadinfo/`;
    let url = `http://127.0.0.1:8000/load/drillmeta/`;
    axios.get(url).then(({ data }) => {
      this.fileOptions.multipart_params.uuid = data;
    });
  },
  computed: {
    //实例化一个plupload上传对象
    uploader() {
      return new plupload.Uploader(this.fileOptions);
    },
  },
  methods: {
    //绑定进队列
    FilesAdded(uploader, files) {
      console.log(this.form);
      let data = this.form;
      if (files[0].name.length > 25) {
        // $.messager.show("提示", "文件名称太长！", "info");
        this.$message({
          type: "error",
          message: "文件名称太长！",
        });
        return;
      }
      if (uploader.files.length > 1) {
        // 最多上传3张图
        // $.messager.show("提示", "只能上传一个文件，请删除多余文件！", "info");
        this.$message({
          type: "error",
          message: "只能上传一个文件,请先删除！",
        });
        uploader.removeFile(files[0]);
        return;
      }
      let objarr = files.map((val, ind) => {
        let obj = {};
        obj.id = val.id;
        obj.name = val.name;
        obj.type = val.type;
        // obj.upload_date = val.upload_date;
        obj.upload_date = new Date().toLocaleString(); //获取日期与时间
        // obj.publiser = val.publiser;
        obj.publisher = "publisher"; //获取当前登录用户信息
        obj.size = parseInt((val.origSize / 1024 / 1024) * 100) / 100;
        obj.percentage = 0;
        obj.loadType = 0;
        console.log(obj);
        return obj;
      });
      this.fileList.push(...objarr);
    },
    //上传之前回调
    BeforeUpload(uploader, file) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          val.loadType = 1;
        }

        //设置参数
        console.log(val.name);
        uploader.setOption("multipart_params", {
          // form: this.form, //设置表单擦不能输
          zk_num: this.form["zk_num"],
          zk_type: this.form["zk_type"],
          final_depth: this.form["final_depth"],
          final_date: this.form["final_date"].getTime(), //时间转为时间戳方便后端解析 对比toLocaleString()
          depth: this.form["depth"],
          project_name: this.form["project_name"],
          company_name: this.form["company_name"],
          uploader: this.form["uploader"],
          uploaddate: this.form["uploaddate"].getTime(),
          filename: val.name,
          publisher: val.publisher,
          type: val.type,
          upload_date: new Date().toLocaleString(),
          // size:val.size
        });

        uploader.settings.multipart_params.size = val.size;
        uploader.settings.multipart_params.id = val.id;
        return val;
      });
    },
    //上传进度回调
    UploadProgress(uploader, file) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          val.percentage = file.percent;
        }
        return val;
      });
    },
    // 上传成功回调
    FileUploaded(uploader, file, responseObject) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          // if (JSON.parse(responseObject.response).status == 0) {
          if (status == 0) {
            val.loadType = 2;
          } else {
            val.loadType = 3;
          }
        }
        return val;
      });
    },
    //取消上传回调
    removeFile(id) {
      this.uploader.removeFile(id);
      this.fileList = this.fileList.filter((val, ind) => {
        if (val.id == id) {
          return false;
        } else {
          return true;
        }
      });
    },
    //开始上传
    // FileUplodeOn() {
    //   this.uploader.start();
    // },
    onSubmit() {
      this.uploader.start();
    },
  },
};
</script>