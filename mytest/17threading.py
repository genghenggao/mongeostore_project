'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-15 21:47:02
LastEditors: henggao
LastEditTime: 2020-11-15 21:50:50
'''
import threading

def square(x,y):
    """
    docstring
    """
    for i in range(x,y):
        print(str(i*i)+ ";")

ta = threading.Thread(target=square,args=(1,6))
tb = threading.Thread(target=square,args=(16,21))

ta.start()
tb.start()