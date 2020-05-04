# coding=utf-8


"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。



示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。


提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # S = list(S)
        # T = list(T)
        # while '#' in S:
        #     if S.index('#') != 0:
        #         S.pop(S.index('#') - 1)
        #     S.pop(S.index('#'))
        # while '#' in T:
        #     if T.index('#') != 0:
        #         T.pop(T.index('#') - 1)
        #     T.pop(T.index('#'))
        # return ''.join(S) == ''.join(T)
        #————————————————————————————————————————————————————————————————————————————
        # 解法二：
        stackS = []
        stackT = []

        for c in S:
            if c == '#':
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        for c in T:
            if c == '#':
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)

        return stackS == stackT
    from collections import defaultdict
    from itertools import product
    from itertools import permutations
    from itertools import combinations


if __name__ == '__main__':
    s = Solution()
    s.backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz",
"oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz")