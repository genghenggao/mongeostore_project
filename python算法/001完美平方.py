'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-18 20:30:31
LastEditors: henggao
LastEditTime: 2020-10-19 08:37:30
'''
class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            print(i)
            temp = i * i
            if temp <= n:
                if int((n - temp) ** 0.5) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3


# 主函数
if __name__ == '__main__':
    n = 13
    print("初始值：", n)
    solution = Solution()
    print("结果：", solution.numSquares(n))
