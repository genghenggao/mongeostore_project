'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-15 21:54:42
LastEditors: henggao
LastEditTime: 2020-11-15 22:02:53
'''
import threading
import time

def square(x,y,thr=None):
    """
    docstring
    """

    if thr:
        thr.join()
    else:
        time.sleep(2)

    for i in range(x,y):
        print(str(i*i)+ ";") 


ta = threading.Thread(target=square,args=(1,6))
tb = threading.Thread(target=square,args=(16,21,ta))

ta.start()
tb.start()
