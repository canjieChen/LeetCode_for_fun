# coding=utf-8

"""
1360. 日期之间隔几天
请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。



示例 1：

输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
示例 2：

输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15


提示：

给定的日期是 1971 年到 2100 年之间的有效日期。
"""

class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        date1, date2 = date1, date2 if date1 < date2 else date2, date1
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        date11 = date1.split('-')
        date22 = date2.split('-')

        day_count = 0

        if date11[0] == date22[0]:
            if date11[1] == date22[1]:
                return date22[2] - date11[2]
            else:
                left = sum(days[:date1[1]]) - date11[2]
                right = sum(days[:date22[1] - 1]) + date22[2]
                return right - left
        else:

            if date22[2] % 4 == 0 and date22[0] != 2100:
                day_count += 1
            year_diff = date22[0] - date11[0]
            if year_diff <= 4:
                day_count += (year_diff % 4)
            elif year_diff >= 4:
                day_count += (year_diff % 4)
            if date22[0] % 4 < 3:
                day_count += 1

            left = 365 - sum(days[:date1[1]]) - date11[2]
            right = sum(days[:date22[1] - 1]) + date22[2]
            365 * (date22[0] - date11[0] - 1)
            hex()


if __name__ == '__main__':
    s = Solution()
    s.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31")