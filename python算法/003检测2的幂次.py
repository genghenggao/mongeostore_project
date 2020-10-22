'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-20 19:30:24
LastEditors: henggao
LastEditTime: 2020-10-20 19:50:49
'''


class Solution:
    def checkPowerOf2(self, n):
        ans = 1
        for i in range(31):  # 当nums1= 2**32时，报错！
            if ans == n:
                return True
            ans = ans << 1
        return False


if __name__ == '__main__':
    temp = Solution()
    nums1 = 2**32
    nums2 = 65
    print(("输入："+str(nums1)))
    print(("输出："+str(temp.checkPowerOf2(nums1))))
    print(("输入："+str(nums2)))
    print(("输出："+str(temp.checkPowerOf2(nums2))))

# 思考，按位运算


class Solution2:
    def checkPowerOf2(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


temp2 = Solution2()
nums = 2**33
print("输入：" + str(nums))
print(("输出：" + str(temp2.checkPowerOf2(nums))))

