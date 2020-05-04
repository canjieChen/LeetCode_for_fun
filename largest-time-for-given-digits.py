# coding=utf-8


"""
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。



示例 1：

输入：[1,2,3,4]
输出："23:41"
示例 2：

输入：[5,5,5,5]
输出：""


提示：

A.length == 4
0 <= A[i] <= 9

"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        from itertools import permutations
        temp = sorted(list(set(permutations(A))))
        while len(temp) > 0:
            a = int(''.join(map(str,temp[-1])))
            if a > 2359:temp.pop(-1)
            elif a % 100 > 59:temp.pop(-1)
            elif len(str(a)) < 4:
                a = '0' * (4-len(str(a))) + str(a)
                return str(a)[:2] + ':' + str(a)[2:]
            else:return str(a)[:2] + ':' + str(a)[2:]
        else:return ''

if __name__ == '__main__':
    s = Solution()
    s.largestTimeFromDigits([9,0,6,9])