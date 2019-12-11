# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        p = ListNode(0)
        pNew = p
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next
        if not p1:
            p.next = p2
        elif not p2:
            p.next = p1
        return pNew.next


head1 = ListNode(1)
t1 = ListNode(3)
head1.next = t1
t2 = ListNode(5)
t1.next = t2
t2.next = None

head2 = ListNode(2)
t1 = ListNode(4)
head2.next = t1
t2 = ListNode(6)
t1.next = t2
t2.next = None

s = Solution()
print(s.Merge(head1, head2).next.val)
