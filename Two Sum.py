# encoding:utf-8
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         temp = []
#         tempList = []
#         for i in range(0, len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j]) == target and nums[i] not in temp and nums[j] not in temp:
#                     print str(nums[i]) + '+' + str(nums[j]) + '=' + str(target)
#                     temp.append(nums[i])
#                     temp.append(nums[j])
#                     tempList.append(i)
#                     tempList.append(j)
#                 else:
#                     pass
#         return tempList if len(temp) != 0 else ''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums = [num for num in nums if (num <= target and (target - num) in nums)]

        # while 1:
        #     for index, num in enumerate(nums):
        #         if num > target:
        #             nums.pop(index)
        #             break
        # print nums


        # [for index,num in enumerate(nums) if (target - num) in nums]
        # a = []
        for index, content in enumerate(nums):
            # b = target - content
            if target > content and target - content in nums[index + 1:]:
                return [index, nums[index + 1:].index(target - content) + index + 1]


if __name__ == '__main__':
    s = Solution()
    s.twoSum([8, 3, 6, 4, 11, 15, 6], 8)
