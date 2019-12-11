# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.q = []
        self.mi = []

    def push(self, node):
        min = self.min()
        if not self.mi or node <= min:
            self.mi.append(node)
        else:
            self.mi.append(min)
        self.q.append(node)

    def pop(self):
        if self.q:
            self.mi.pop()
            return self.q.pop()

    def top(self):
        if self.q:
            return self.q[-1]

    def min(self):
        if self.mi:
            return self.mi[-1]


s = Solution()
s.push(1)
s.push(2)
s.push(5)
s.push(3)
print(s.min())
print(s.pop())
print(s.top())
