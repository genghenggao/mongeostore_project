'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2021-05-12 08:54:14
LastEditors: henggao
LastEditTime: 2021-05-12 14:48:14
'''
import requests
import os
import re
import time


def Picture_Download(url_img_path, img_title):
    filename = img_title.replace('/', '').strip()  # 文件名不能有/，替换为空，不然会报错
    try:
        resullt = requests.get(url_img_path.strip())  # 使用GET方法请求图片地址
    except:
        print(url_img_path, 'Download failed')
    else:
        if resullt.status_code == 200:  # 如果状态码位200，说明文件存在，保存图片
            File = open(filename + '.jpg', 'wb')
            File.write(resullt.content)
            File.close()


def Img_Url(url):  # 传入网址，获取图片地址及图片标题
    result = requests.get(url)
    result.encoding = 'gbk'  # 该网页编码为GBK编码
    compile = re.compile(r'<img src="(.*?)" alt="(.*?)" />')  # 使用正则获取图片

    all = compile.findall(result.text)
    for item in all:
        print(item[0], item[1])
        Picture_Download(item[0], item[1])  # 循环出一页每个图片地址和名称


def main():
    for i in range(1, 4):
        if i == 1:
            Img_Url(r'http://www.netbian.com/weimei/index.htm')
        else:
            Img_Url(r'http://www.netbian.com/weimei/index_%d.htm' % i)
            time.sleep(1)  # 提取一页就暂停2秒，防止访问过快被屏蔽


if __name__ == '__main__':
    main()
