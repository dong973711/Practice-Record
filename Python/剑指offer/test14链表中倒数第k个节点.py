# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        t = head
        for i in range(k):
            if not t:
                # print("越界")
                return None
            t = t.next
        h = head
        while t:
            t = t.next
            h = h.next
        return h


head = ListNode(1)
t1 = ListNode(2)
head.next = t1
t2 = ListNode(3)
t1.next = t2
t3 = ListNode(4)
t2.next = t3
t4 = ListNode(5)
t3.next = t4
s = Solution()
r = s.FindKthToTail(head, 6)
print(r.val)
