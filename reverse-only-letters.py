# coding=utf-8

"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。



示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"


提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含 \ or "
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # dic = {}
        # temp_dic = {}
        # [dic.setdefault(item, []).append(index) for index, item in enumerate(S) if not item.isalpha()]
        # temp = [i for i in S if i.isalpha()][::-1]
        # [temp_dic.setdefault(index, item) for index, item in enumerate(S) if not item.isalpha()]
        # for i in sorted(temp_dic.keys()):
        #     temp.insert(i, temp_dic[i][0])
        # return ''.join(temp)
        #————————————————————————————————————————————————————————————————————————————
        # 解法二：牛逼！！
        # S = list(S)
        # i = 0
        # j = len(S) - 1
        # while i < j:
        #     while i < j and not S[i].isalpha():
        #         i += 1
        #     while i < j and not S[j].isalpha():
        #         j -= 1
        #
        #     if i < j:
        #         S[i], S[j] = S[j], S[i]
        #         i += 1
        #         j -= 1
        #
        # return "".join(S)

if __name__ == '__main__':
    s = Solution()
    s.reverseOnlyLetters("Test1ng-Leet<*code-Q!!")