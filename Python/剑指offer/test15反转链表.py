# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        h = pHead
        p = pHead.next
        q = pHead.next.next
        while q:
            p.next = h
            h = p
            p = q
            q = q.next
        p.next = h
        pHead.next = None
        return p


head = ListNode(1)
head.next =None
# t1 = ListNode(2)
# head.next = t1
# t2 = ListNode(3)
# t1.next = t2
# t3 = ListNode(4)
# t2.next = t3
# t4 = ListNode(5)
# t3.next = t4
# t4.next = None
s = Solution()
h = s.ReverseList(head)
print(h.val)
