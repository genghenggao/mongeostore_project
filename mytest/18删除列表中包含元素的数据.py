'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-16 16:05:39
LastEditors: henggao
LastEditTime: 2020-11-16 19:10:02
'''

import re
alist = ['bar.files', 'barbar.files', 'foo.chunks', 'foos.files',
         'barbares', 'foofoos', 'bares', 'files']
for i in alist:
    print(alist)
    print(i)

    if '.files' in i:
        print("包含.files")
        alist.remove(i)
    # elif '.chunks' in i:
    #     print('包含.chuncks')
    #     alist.remove(i)
    # else:
    #     print("都不包含")

    print(alist)
# alist = alist
for i in alist:
    print(alist)
    print(i)

    if '.files' in i:
        print("包含.files")
        alist.remove(i)

