# coding=utf-8

"""
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

链接：https://leetcode-cn.com/problems/deep-dark-fraction
"""

class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        cont = cont[::-1]
        cont_1 = []
        # for index, content in enumerate(cont):
        while len(cont) != 1:
            if len(cont) == 0:
                cont_1.append(pow(cont, -1))

            else:
                cont_1.append(pow(cont, -1) + cont[index + 1])
        else:
            if len(cont) == 0:
                return cont[0]
            else:
                pass

if __name__ == '__main__':
    s = Solution()
    s.fraction(cont=[3, 2, 0, 2])
