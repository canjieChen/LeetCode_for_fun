# coding=utf-8

"""
LCP 2. 分式化简
有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？



连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。



输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。



示例 1：

输入：cont = [3, 2, 0, 2]
输出：[13, 4]
解释：原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。
示例 2：

输入：cont = [0, 0, 3]
输出：[3, 1]
解释：如果答案是整数，令分母为1即可。
限制：

cont[i] >= 0
1 <= cont的长度 <= 10
cont最后一个元素不等于0
答案的n, m的取值都能被32位int整型存下（即不超过2 ^ 31 - 1）。

"""

class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        if len(cont) == 1:return cont + [1]
        init_list = [1] + [cont.pop(-1)]
        while len(cont):
            if init_list[0] < 0 and init_list[1] < 0:init_list = list(abs(init_list[0]), abs(init_list[1]))
            elif init_list[0] > 0 and init_list[1] < 0:init_list = 0 - init_list[0], abs(init_list[1])
            if len(cont) == 1:init_list = cont[-1] * init_list[1] + init_list[0], init_list[1]
            elif cont[-1] == 0:init_list = init_list[::-1]
            else:init_list = init_list[1], cont[-1] * init_list[1] + init_list[0]
            cont.pop(-1)
        small = init_list[1] if init_list[1] < init_list[0] else init_list[0]
        big_item = 0
        for num in range(1, small + 1):
            if init_list[0] % num == 0 and init_list[1] % num == 0:
                big_item = num if num > big_item else big_item
        return [init_list[0] / big_item, init_list[1] / big_item]


if __name__ == '__main__':
    s = Solution()
    s.fraction(cont = [0, 0, 3])