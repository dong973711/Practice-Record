# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        con = len(matrix[0])
        cir = 0
        t = []
        while row > 2 * cir and con > 2 * cir:
            for i in range(cir, con - cir):
                t.append(matrix[cir][i])
            if cir < row - cir - 1:
                for i in range(cir + 1, row - cir):
                    t.append(matrix[i][con - cir - 1])
            if con - cir - 1 > cir and row - cir - 1 > cir:
                for i in range(con - cir - 2, cir-1, -1):
                    t.append(matrix[row - cir - 1][i])
            if cir < con - cir - 1 and cir < row - cir - 2:
                for i in range(row - cir - 2, cir, -1):
                    t.append(matrix[i][cir])
            cir += 1
        return t


s = Solution()
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
t = s.printMatrix(a)
print(t)
