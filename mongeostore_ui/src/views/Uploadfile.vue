<template>
  <div style="padding-top:20px;">
    <el-button ref="VideoChose" id="VideoChose" size="mini">选择文件</el-button>
    <el-button ref="VideoChose" type="primary" size="mini" @click="FileUplodeOn"
      >开始上传</el-button
    >
    <el-card style="margin-top:20px;">
      <el-table :data="fileList" style="width: 100%">
        <el-table-column prop="id" label="文件id"></el-table-column>
        <el-table-column prop="name" label="文件名称"></el-table-column>
        <el-table-column prop="type" label="文件类型"></el-table-column>
        <el-table-column prop="size" label="文件大小" v-slot="{ row }">
          {{ row.size }}MB
        </el-table-column>
        <el-table-column prop="upload_date" label="上传时间"></el-table-column>
        <el-table-column prop="publisher" label="上传人员"></el-table-column>
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
  </div>
</template>

<script>
import plupload from "plupload";
import axios from "axios";
import { stringify } from "qs";
export default {
  name: "UploadFile",
  data() {
    return {
      show: false,
      fileList: [],
      fileOptions: {
        browse_button: "VideoChose",
        // url: "http://127.0.0.1:8000/load/uploadfile/",
        url: "http://127.0.0.1:8000/load/fileinfo/",
        flash_swf_url: "script/Moxie.swf",
        silverlight_xap_url: "script/Moxie.xap",
        // chunk_size: "10mb", //分块大小  ,注销掉或者改chunk_size：'0mb'为解决文件大于10M存为blob问题
        max_retries: 3,
        unique_names: true,
        multi_selection: true,
        views: {
          list: true,
          thumbs: true, // Show thumbs
          active: "thumbs"
        },
        filters: {
          mime_types: [
            //文件格式
            {
              title: "files",
              extensions:
                "png,jpg,svg,mp4,rmvb,mpg,mxf,avi,mpeg,wmv,flv,mov,ts,docx,doc,pdf,segy" //文件格式
            }
          ],
          max_file_size: "10240mb", //最大上传的文件
          prevent_duplicates: true //不允许选取重复文件
        },
        multipart_params: {
          uuid: "" //参数
          // testparams: "Must can see me",
          // "testparams2": "Must can see me2"
        }
      }
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
    let url = `http://127.0.0.1:8000/load/fileinfo/`;
    axios.get(url).then(({ data }) => {
      this.fileOptions.multipart_params.uuid = data;
    });
  },
  computed: {
    //实例化一个plupload上传对象
    uploader() {
      return new plupload.Uploader(this.fileOptions);
    }
  },
  methods: {
    //绑定进队列
    FilesAdded(uploader, files) {
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
          filename: val.name,
          publisher: val.publisher,
          type: val.type,
          upload_date: new Date().toLocaleString()
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
    FileUplodeOn() {
      this.uploader.start();
    }
  }
};
</script>