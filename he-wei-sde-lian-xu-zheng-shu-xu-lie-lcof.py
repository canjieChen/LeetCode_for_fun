# coding=utf-8

"""
面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：

1 <= target <= 10^5

"""

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # 自己的解法
        """
        temp = []
        mid = target / 2 + 2
        flag = 1
        for i in range(2, mid):
            temp_1 = range(1, i)
            sum = 0
            if flag:
                for j in range(1, i):
                        sum += j
                        if sum == target:
                            if range(1, j + 1) not in temp:
                                temp.append(range(1, i))
                                break
                            else:
                                flag = 0
                                break
                        elif sum > target:break
            temp_2 = range(i, mid)
            sum = 0
            for k in range(i, mid):
                sum += k
                if sum == target:
                    temp.append(range(i, k + 1))
                    break
                elif sum > target:break
        return sorted(temp)
        """

        # 大佬的解法
        """
        一个以 a1为首项，以 1 为公差，以 n 为项数的等差数列的和为 target，
        target=n*a1 + [n(n−1)]/2
        转化为
        a1 = {target−[n(n−1)]/2}/n
        
        目标是找出所有满足条件的 n、a1对，
        思路是对 n 从 2 开始遍历（题目要求最少是 2 个数），验证 a1是否为正整数。
        有一个问题是 n 遍历到多少呢？
        其实不需要特地去算 n 的上限，随着 n 的递增，a1递减，当 a1 <= 0时跳出循环即可。
        """
        res = []
        for n in range(2, target + 1):
            temp = target - n * (n - 1) // 2
            if temp <= 0:
                break
            if not temp % n:
                a_1 = temp // n
                res.append([a_1 + i for i in range(n)])
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    s.findContinuousSequence(target=15)