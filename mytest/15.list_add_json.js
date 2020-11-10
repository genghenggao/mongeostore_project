/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-11-10 16:21:02
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-10 16:26:16
 */
// 生成一个赛选字段ZKx
let tem_list = []
for (let i = 0; i < 55; i++) {
    // const element = array[i];
    ZK = "ZK"
    let ZKX = ZK + i;
    // {text:"ZKX",value;"ZKX"}
    json_data = { text: ZKX, value: ZKX }
    tem_list.push(json_data)
}
console.log(tem_list)