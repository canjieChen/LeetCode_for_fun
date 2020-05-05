# coding=utf-8

"""
面试题66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。



示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]


提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000

"""

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        """
        flag = 0
        temp = []
        while flag < len(a):
            b = a[:]
            b.remove(b[flag])
            temp.append(reduce(lambda x, y: x * y, b))
            flag += 1
        else:
            return temp
        """

        """
        if not A: return []
        forward = [1]
        for a in A[:-1]:
            forward.append(forward[-1] * a)

        backward = [1]
        for a in A[::-1][:-1]:
            backward.append(backward[-1] * a)
        backward = backward[::-1]

        B = [f * b for f, b in zip(forward, backward)]
        return B
        """

        forward = [1] + [reduce(lambda x, y: x * y, a[:i]) for i in a][:-1]
        backward = [reduce(lambda x, y: x * y, a[::-1][:i]) for i in a[::-1]][1:] + [1]
        return [reduce(lambda x, y: x * y, item) for item in zip(forward, backward)]


if __name__ == '__main__':
    s = Solution()
    s.constructArr([1,2,0,4,5])