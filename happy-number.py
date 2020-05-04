# coding=utf-8

"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例:

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


from math import pow

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = 0
        while n >= 1 and flag < 100:
            list1 = []
            sum = 0
            several = len(str(n))
            several -= 1
            a = int(n/pow(10, several))
            if a != 0: list1.append(a)
            while several > 0:
                b = int(n % pow(10, several) / pow(10, several-1))
                several -= 1
                # dic[several] = b
                if b != 0: list1.append(b)
            for i in list1:
                sum += pow(i, 2)
            if sum == 1:
                return True
            else: n = int(sum)
            flag += 1
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    s.isHappy(7)