# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f = [0, 1, 1]
        if n <= 1:
            return f[n]
        if n == 2:
            return f[2]
        else:
            for i in range(3, n+1):
                f.append(f[i - 1] + f[i - 2])
            return f[n]


s = Solution()
print(s.Fibonacci(2))
print(s.Fibonacci(3))
print(s.Fibonacci(4))
print(s.Fibonacci(5))