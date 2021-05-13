'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-23 17:12:43
LastEditors: henggao
LastEditTime: 2021-05-11 23:22:09
'''


# import numpy as np

# mySeis = np.zeros((10, 10), dtype=np.float32)
# print(mySeis)

# data1 = [1, 2]
# data2 = [3, 4]

# # data3 = [data1,data2]
# data3 = []
# data3.append(data1)
# print(data3)


# a,b = 1,2
# print(a)
# print(b)


# import urllib
# from numpy import *
# a = array([[1,2,3],[4,5,6]])
# b = array([[1,2,3],[4,5,6]])
# print(a+b)

# a = arange(10)
# print(sin(a))


# from  urllib import request
# response = request.urlopen("http://www.jd.com")
# html = response.read()
# html = html.decode('utf-8')
# print(html)

# import requests
# url = "http://baidu.com"
# strhtml = requests.get(url)
# print(strhtml.text)
# print(strhtml.status_code)


import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36','referer':"www.mmjpg.com" }


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    # print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # print(soup)
    ranks = soup.select("span.pc_temp_num")
    # print(ranks)
    titles = soup.select("div.pc_temp_songlist > ul > li > a")
    # print(titles)
    times = soup.select("span.pc_temp_tips_r > span")
    # print(times)
    for rank, title, time in zip(ranks, titles, times):
        data = {
            "rank": rank.get_text().strip(),
            "singer": title.get_text().split('-')[0],
            "song": title.get_text().split('-')[1],
            "time": time.get_text().strip()
        }
        print(data)


# def main():
#     urls = [
#         "http://www.kugou.com/yy/rank/home/{}-8888.html".format(str(i)) for i in range(1, 24)]
#     for url in urls:
#         # print(url)
#         get_info(url)
#         time.sleep(1)
# main()


if __name__ == '__main__':
    urls = [
        "https://www.kugou.com/yy/rank/home/{}-8888.html".format(str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
        # time.sleep(1)
