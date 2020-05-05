# coding=utf-8

class Diamond():
    def diamond(self, n):
        # temp = [(i*2+1) for i in range(n) if i <= n / 2 + 1]
        # temp += temp[-2::-1]
        # for i in temp:
        #     print '*' * i

        # down = 1.0
        # up = 2.0
        # sum = 0.00
        # for i in range(20):
        #     pre = up / down
        #     up, down, sum = (up + down), up, (sum + pre)
        # print sum
        # reduce()

        # sum_1 = 1
        # for i in range(2, n+1):
        #     for j in range(i-1, 0, -1):
        #         i *= j
        #     sum_1 += i
        # print(sum_1)

        # 某位数的阶乘
        # reduce(lambda x, y: x * y, range(1, n))
        # 阶乘之和
        # reduces(lambda x, y: x + y, [reduce(lambda x, y: x * y, range(1, i + 1)) for i in range(1, n)])
        __import__()


if __name__ == '__main__':
    D = Diamond()
    D.diamond(4)