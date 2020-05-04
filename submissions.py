# coding=utf-8


"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。



示例 1：

输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：A = "apple apple", B = "banana"
输出：["banana"]


提示：

0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        temp_A = list(set(A).difference(set(B)))
        temp_B = list(set(B).difference(set(A)))
        for i in A:
            if i in temp_A and A.count(i) > 1:temp_A.remove(i)
        for i in B:
            if i in temp_B and B.count(i) > 1:temp_B.remove(i)
        return temp_A + temp_B
        from itertools import combinations

if __name__ == '__main__':
    s = Solution()
    s.uncommonFromSentences("fv kisxg hfmeq fw gi fpyc ojtr s hfmeq ojtr kisxg",
"chpi hfmeq chpi dq hwtxa orql orql m s fw dq m fw")