# coding=utf-8

"""面试题60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


限制：

1 <= n <= 11
"""


class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        """
        from itertools import product
        nums = range(1, 7)
        result = list(product(nums, repeat=n))
        result_total = len(list(result))

        # print(list(result))

        from collections import defaultdict
        dic = defaultdict(int)

        for i in result:
            sum_1 = reduce(lambda x, y: x + y, i)
            dic[sum_1] += 1

        rate = defaultdict(float)
        for j in dic.items():
            rate_temp = j[1] / float(result_total)
            rate[j[0]] = round(rate_temp, ndigits=5)
        print(rate.values())
        """

        """
        results = list(__import__('itertools').product(range(1, 7), repeat=n))
        total = float(len(results))
        counts = __import__('collections').defaultdict(int)
        for result in results:
            counts[sum(result)] += 1
        print [float('%.5f' % (count / total)) for count in counts.values()]
        """

        a = range(1, 7)
        if n == 1:return [float('%.5f' % (1 / float(len(a)))) for num in a]
        from collections import defaultdict
        b = defaultdict(int)
        count = 0
        for i in range(n - 1):
            for j in a:
                for k in a:
                    sum_1 = j
                    sum_1 += k
                    b[sum_1] += 1
                    count += 1
        return [float('%.5f' % (v / float(count))) for v in b.values()]


if __name__ == '__main__':
    s = Solution()
    s.twoSum(3)