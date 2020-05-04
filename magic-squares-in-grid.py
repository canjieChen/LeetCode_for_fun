# coding=utf-8

"""
3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。



示例 1:

输入: [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出: 1
解释:
下面的子矩阵是一个 3 x 3 的幻方：
438
951
276

而这一个不是：
384
519
762

总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
提示:

1 <= grid.length = grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = {}
        row = len(grid) - 2
        clounm = len(grid[0]) - 2
        # 幻方子矩阵总个数为：
        if row <= 0 or clounm <= 0:return 0
        flag = row * clounm
        temp = []
        while 1:
            for i in range(len(grid) - 2):
                for clounm in range(len(grid[0]) - 2):
                    for row in range(i, len(grid)):
                        print grid[row][clounm], grid[row][clounm + 1], grid[row][clounm + 2]
                        if (grid[row][clounm] not in dic.keys() and grid[row][clounm + 1] not in dic.keys() and grid[row][clounm + 2] not in dic.keys()) and (grid[row][clounm] < 10 and grid[row][clounm + 1] < 10 and grid[row][clounm + 2] < 10) and (grid[row][clounm] > 0 and grid[row][clounm + 1] > 0 and grid[row][clounm + 2] > 0):
                            temp.append([grid[row][clounm], grid[row][clounm + 1], grid[row][clounm + 2]])
                            dic[grid[row][clounm]] = 1
                            dic[grid[row][clounm + 1]] = 1
                            dic[grid[row][clounm + 2]] = 1
                            if len(dic.keys()) % 3 != 0:
                                flag -= 1
                                temp = []
                                dic = {}
                                print '==' * 10
                                break
                        else:
                            flag -= 1
                            temp = []
                            dic = {}
                            print '==' * 10
                            break
                        if len(temp) == 3:
                            if not (sum(temp[0]) == sum(temp[1]) == sum(temp[2]) == (temp[0][0] + temp[1][0] + temp[2][0]) == (temp[0][1] + temp[1][1] + temp[2][1]) == (temp[0][2] + temp[1][2] + temp[2][2]) == (temp[0][0] + temp[1][1] + temp[2][2]) == (temp[0][2] + temp[1][1] + temp[2][0])):
                                flag -= 1
                            temp = []
                            dic = {}
                            print '==' * 10
                            break
            break
        return flag


if __name__ == '__main__':
    s = Solution()
    s.numMagicSquaresInside([[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]])