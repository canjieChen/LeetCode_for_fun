# coding=utf-8

"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        alpha = []
        dic_num = {}
        permutations_alpha = []
        for i in S:
            if i.isalpha():alpha.append(i)
            elif i.isdigit():dic_num[str(S.index(i))] = i
        n = len(alpha)
        for i in alpha:
            if len(alpha) != 2 * n:
                alpha.append(i.upper())
            else:break
        from itertools import permutations
        for i in permutations(alpha, n):
            flag = 0
            temp = ''.join(i)
            if (temp.startswith(alpha[0].lower()) or temp.startswith(alpha[0].upper())) and (temp.endswith(alpha[-1].lower()) or temp.endswith(alpha[-1].upper())):
                for j in temp:
                    if j.lower() in temp and j.upper() in temp:
                        flag += 1
                        break
                if flag == 0: permutations_alpha.append(temp)
                if len(permutations_alpha) == 2 ** n:break
        for i in range(len(permutations_alpha)):
            for j in dic_num.keys():
                i = i[:j] + dic_num[j] + i[j:]
        return permutations_alpha


if __name__ == '__main__':
    s = Solution()
    s.letterCasePermutation(S = "a1b2")