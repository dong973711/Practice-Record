# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def push(self, node):
        # write code here
        self.Stack1.append(node)

    def pop(self):
        # return xx
        if not self.Stack2 and not self.Stack1:
            return
        if self.Stack2:
            return self.Stack2.pop()
        else:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.push(4)
s.push(5)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
