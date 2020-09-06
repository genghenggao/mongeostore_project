import axios from '../axios'

/* 
 * 系统注册模块
 */

// 注册
export const register = data => {
    return axios({
        url: 'register',
        method: 'post',
        data
    })
}

