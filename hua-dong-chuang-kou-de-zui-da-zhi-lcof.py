# coding=utf-8

"""面试题59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = []
        # end_index = len(nums) - k + 1
        # for i in range(0, end_index):
        #     temp.append(max(nums[i: i + k] if i != len(nums) - k else nums[i:]))
        # return temp
        # print [max(nums[i: i + k] if i != len(nums) - k else nums[i:]) for i in range(0, end_index)]
        # while len(nums) != k:
        #     temp.append(max(nums[0: k]))
        #     nums = nums[1:]
        # else:
        #     return temp

        s = "  hello       world!  "
        a = s.strip().split(' ')
        for index, content in a:
            if i == '':
                a.remove(i)


if __name__ == '__main__':
    s = Solution()
    s.maxSlidingWindow( nums = [1,3,-1,-3,5,3,6,7], k=3)