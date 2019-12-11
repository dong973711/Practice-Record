# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        f = [0, 1, 2]
        for i in range(3, number + 1):
            f.append(f[i - 1] + f[i - 2])
        return f[number]


s = Solution()
print(s.rectCover(4))
