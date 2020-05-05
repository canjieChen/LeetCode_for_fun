# coding=utf-8

"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = __import__("collections").Counter(s)
        if len(s) == 0: return ' '
        temp = [i for i in temp if temp[i] == 1]
        return s[min([s.find(j) for j in temp])] if len(temp) > 0 else ' '

        #
        # temp = __import__("collections").Counter(s)
        # print s[min([s.find(j) for j in [i for i in temp if temp[i] == 1]])] if len(s) > 0 else " "


if __name__ == '__main__':
    s = Solution()
    # s.firstUniqChar(s = "abaccdeff")
    # s.firstUniqChar(s = "")
    # s.firstUniqChar(s = "s")
    s.firstUniqChar(s = "ss")