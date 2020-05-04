# coding=utf-8

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dic_s = {}
        # dic_t = {}
        # for index, item in enumerate(s):
        #     dic_s.setdefault(item, []).append(index)
        # for index, item in enumerate(t):
        #     dic_t.setdefault(item, []).append(index)
        #
        # if dic_s and dic_t:
        #     [dic_s.pop(i) for i in dic_s.keys() if len(dic_s.get(i)) < 2]
        #     [dic_t.pop(i) for i in dic_t.keys() if len(dic_t.get(i)) < 2]
        # elif dic_s or dic_t:
        #     print False
        # else:
        #     print True
        #
        # if dic_s and dic_t:
        #     [dic_s.pop(i) for i in dic_s.keys() if dic_s.get(i) in dic_t.values()]
        #     return True if len(dic_s.values()) == 0 else False
        # elif dic_s or dic_t:
        #     print False
        # else:
        #     print True
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False

        table = dict()
        for i, x in enumerate(s):
            if x in table:
                if table[x] != t[i]:
                    return False
            else:
                table[x] = t[i]

        return True

if __name__ == '__main__':
    s = Solution()
    s.isIsomorphic(s = "paper", t = "title")