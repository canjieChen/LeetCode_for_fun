# coding=utf-8

"""面试题 16.26. 计算器
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().replace(' ', '')
        temp = ['+', '-', '*', '/']
        while not str(s).isdigit():

            # 用以判断当前是否有乘除法
            times_index = len(s) if s.find('*') < 0 else s.find('*')
            devide_index = len(s) if s.find('/') < 0 else s.find('/')
            basic_index = times_index if times_index < devide_index else devide_index
            basic_index = -1 if times_index == devide_index else basic_index

            if basic_index > 0:

                # 该循环用以获取乘除法前的数字
                temp_2 = 0
                for index_1, content_1 in enumerate(s[basic_index - 1::-1]):
                    if not content_1.isdigit():
                        temp_2 = basic_index - index_1
                if temp_2 != 0:
                    base = int(s[temp_2 + 1: basic_index])
                else:
                    base = int(s[:basic_index])
                base_index = s[:basic_index].rfind(str(base))
                temp_1 = s[basic_index]

                for index, content in enumerate(s[basic_index + 1:]):
                    if not content.isdigit():
                        now = int(s[basic_index + 1: basic_index + index + 1])

                        if temp.index(temp_1) == 2:
                            base *= now
                        elif temp.index(temp_1) == 3:
                            base /= now

                        if temp_2 != 0:
                            s = s[:base_index] + str(base) + s[basic_index + index + 1:]
                        else:
                            s = str(base) + s[basic_index + index + 1:]
                        break

                    elif index == len(s[basic_index + 1:]) - 1:
                        now = int(s[basic_index + 1:])

                        if temp.index(temp_1) == 2:
                            base *= now
                        elif temp.index(temp_1) == 3:
                            base /= now
                        s = s[:base_index] + str(base)

            else:
                base = 0
                basic_index = 0
                for index_2, content_2 in enumerate(s):
                    if not content_2.isdigit() and index_2 == 0:
                        pass
                    elif not content_2.isdigit():
                        if basic_index == 0:
                            base += int(s[: index_2])
                            basic_index = index_2
                            temp_1 = s[index_2]
                        else:
                            now = int(s[basic_index + 1: index_2])
                            if temp.index(s[basic_index]) == 0:
                                base += now
                            elif temp.index(s[basic_index]) == 1:
                                base -= now
                            s = str(base) + s[index_2:]
                            break
                    elif index_2 == len(s) - 1:
                        now = int(s[basic_index + 1:])
                        if temp.index(temp_1) == 0:
                            base += now
                        elif temp.index(temp_1) == 1:
                            base -= now
                        if base < 0:
                            return base
                        s = str(base)
        return int(s)


if __name__ == '__main__':
    s = Solution()
    s.calculate(s="1+2*3+4*5+6*7+8*9+10")
