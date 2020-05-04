# coding=utf-8

"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # if k >= len(nums): return float(sum(nums)) / float(k)
        # temp = []
        # for i in range(len(nums)-k+1):
        #     temp.append(sum(nums[i:i+k]))
        # return float(max(temp)) / float(k)

        # ————————————————————————————————————————————
        # 解法二：
        sub_max = sum(nums[0:k])
        tmp = sub_max
        for i in range(len(nums) - k):
            tmp = tmp - nums[i] + nums[i + k]
            sub_max = max(tmp, sub_max)
        return sub_max * 1.0 / k

if __name__ == '__main__':
    s = Solution()
    s.findMaxAverage([1,12,-5,-6,50,3], k = 4)