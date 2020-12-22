'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-21 20:49:10
LastEditors: henggao
LastEditTime: 2020-12-22 15:03:16
'''
import sys, time
def progress(percent, width=50):  # 设置进度条的宽度
    if percent >= 100:            # 当百分比 >= 100 时；
        percent = 100             # 直接将百分比设置为 100%
    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * '#')  # ('[%%-%ds]' % 50)%(int(50 * 10 / 100) * '#')
    print('\r%s %d%%' % (show_str, percent), file=sys.stdout, flush=True, end='')   # \r 是指回到行首 覆盖形式的在打印
#
total_size = 102561               # 数据的总大小
recv_size = 0                     # 接收或传送了多少
while recv_size < total_size:     # 如果接收或发送的 总大小 小于 数据总大小
    time.sleep(0.01)              # 模拟下载的网络延迟
    recv_size += 1024             # 一直循环 发送 数据每次 1024
    recv_per = int(100 * recv_size / total_size)        # 获取 当前传输 百分比 如 31%
    progress(recv_per)            # 将这个值 31 传给 progress