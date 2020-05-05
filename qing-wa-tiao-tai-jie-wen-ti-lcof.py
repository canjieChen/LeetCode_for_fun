# coding=utf-8

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
提示：

0 <= n <= 100
"""


class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        使用斐波那契数列运算时，时间复杂度代价较大        
        if n < 2:
            return 1
        else:
            return self.numWays(n - 1) + self.numWays(n - 2)
        """

        temp = [1, 1]
        if n < 2:return temp[n]
        for i in range(2, n):
            temp[0], temp[1] = temp[1], sum(temp[:i]) % 1000000007
        return sum(temp) if n < 44 else sum(temp[:i]) % 1000000007


if __name__ == '__main__':
    s = Solution()
    s.numWays(44)
