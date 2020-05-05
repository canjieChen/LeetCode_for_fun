# coding=utf-8

"""
面试题49. 丑数
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。

"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 自己的解法
        """
        if n <= 6: return n
        temp, num, n = 0, 6, n - 6
        while n:
            num += 1
            temp = num
            while temp > 5:
                if temp % 5 == 0:
                    temp /= 5
                elif temp % 3 == 0:
                    temp /= 3
                elif temp % 2 == 0:
                    temp /= 2
                else:
                    break
            else:
                n -= 1
        return num
        """

        # 官方解法
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.nthUglyNumber(33)