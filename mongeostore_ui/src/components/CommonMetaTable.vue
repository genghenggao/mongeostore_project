<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-23 09:29:30
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-24 19:15:31
-->
<template>
  <div class="seismictable" style="overflow: scroll; max-height: 775px">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">_id</th>
          <th scope="col">filename</th>
          <th scope="col">contentType</th>
          <th scope="col">length</th>
          <th scope="col">uploadDate</th>
          <th scope="col">publisher</th>
          <th scope="col">aliases</th>
          <th scope="col">metadata</th>
          <th scope="col">md5</th>
          <th scope="col">chunkSize</th>
          <th scope="col">operate</th>
        </tr>
      </thead>
      <tbody id="list"></tbody>
      <!-- <tbody>
        <tr v-for="file in files">
          <td v-text="file._id"></td>
          <td v-text="file.filename"></td>
          <td v-text="file.contentType"></td>
          <td v-text="file.length"></td>
          <td v-text="file.uploadDate"></td>
          <td v-text="file.publisher"></td>
          <td v-text="file.aliases"></td>
          <td v-text="file.metadata"></td>
          <td v-text="file.md5"></td>
          <td v-text="file.chunkSize"></td>
        </tr>
      </tbody> -->
      <!-- <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
          <td>{{files.filename}}</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody> -->
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CommonMetaTable",
  data() {
    return {
      files: [],
      _id: "",
    };
  },
  created() {
    this.showFile();
  },
  mounted() {
    // this.showFile();
  },
  watch: {},
  methods: {
    showFile() {
      const url = "http://127.0.0.1:8000/load/commonmetashow/";
      axios
        .get(url, {
          params: {
            // 设置上传到后端的数据库和集合名称
            dbname: this.$store.state.title_message,
            //   dbname: this.$store.state.temp_database,
          },
        })
        .then((response) => {
          // var res = JSON.parse(response.bodyText);
          //   console.log(response);
          // console.log(response.data.filename);
          var result = response.data.list;
          let dbname = this.$store.state.title_message;
          this.files = result;
          $(response.data.list).each(function (i, values) {
            const url = "http://127.0.0.1:8000/load/commonfiledownload/?_id=";
            $("#list").append(
              "<tr><td>" +
                values._id +
                "</td>" +
                "<td>" +
                values.filename +
                "</ta></td>" +
                "<td>" +
                values.contentType +
                "</td>" +
                "<td>" +
                values.length +
                "</td>" +
                "<td>" +
                values.uploadDate +
                "</td>" +
                "<td>" +
                values.publisher +
                "</td>" +
                "<td>" +
                values.aliases +
                "</td>" +
                "<td>" +
                values.metadata +
                "</td>" +
                "<td>" +
                values.md5 +
                "</td>" +
                "<td>" +
                values.chunkSize +
                "</td>" +
                "<td>" +
                '<button type="button" v-on:click="download" class="btn btn-info">' +
                "<a href=" +
                url +
                values._id +
                "&" +
                "dbname=" +
                dbname +
                ">" +
                "DownLoad" +
                "</button>" +
                "</td></tr>"
            );
          });
          // table
        });
    },
  },
};
</script>

<style>
.seismictable {
  border: 0;
  padding: 0;
  height: 775px;
}
</style>