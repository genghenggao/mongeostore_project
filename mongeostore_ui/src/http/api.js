/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-09-01 13:53:42
 * @LastEditors: henggao
 * @LastEditTime: 2020-09-01 20:01:48
 */
/* 
 * 接口统一集成模块
 */
import * as login from './modules/login'
import * as user from './modules/user'
import * as dept from './modules/dept'
import * as role from './modules/role'
import * as menu from './modules/menu'
import * as dict from './modules/dict'
import * as config from './modules/config'
import * as log from './modules/log'
import * as loginlog from './modules/loginlog'


// 默认全部导出
export default {
    login,
    user,
    dept,
    role,
    menu,
    dict,
    config,
    log,
    loginlog
}