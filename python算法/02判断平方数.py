'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-20 17:06:11
LastEditors: henggao
LastEditTime: 2020-10-20 17:24:32
'''
class Solution:
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while (r - l > 1):
            mid = (l + r) / 2
            if (mid * mid <= num):
                l = mid
                # print("l的值：" ,  l)
            else:
                r = mid
                # print("r的值：" , r)
        ans = l
        if (l * l < num):
            ans = r
        return ans * ans == num
#主函数
if __name__ == '__main__':
    num = 16
    print("初始值：", num)
    solution = Solution()
    print("结果：", solution.isPerfectSquare(num))
