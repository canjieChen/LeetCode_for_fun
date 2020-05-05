# coding=utf-8

"""
面试题29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:return []
        if not matrix[0]:return []
        if len(matrix[0]) == 1:return [i.pop(-1) for i in matrix]
        temp = matrix[0]
        matrix = matrix[1:]
        while matrix:
            for i in matrix:
                if i != matrix[-1]:
                    if len(i) != 1:
                        temp.append(i.pop(-1))
                    else:
                        temp += [i.pop(-1) for i in matrix]
                        matrix = []
                        break
                else:
                    temp += (matrix.pop(-1))[::-1]
                    matrix = [i[::-1] for i in matrix[::-1]]
        else:
            return temp


if __name__ == '__main__':
    s = Solution()
    # s.spiralOrder(matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
    s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    # s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    # s.spiralOrder(matrix = [[1,2],[3,4],[5,6],[7,8]])
    # s.spiralOrder(matrix = [[1],[2],[3],[4],[5],[6],[7],[8]])
    # s.spiralOrder(matrix = [[],[]])
    # s.spiralOrder(matrix = [])
