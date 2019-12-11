# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 返回从尾部到头部的列表值序列，例如[1,2,3]
def printListFromTailToHead(listNode):
    l = []
    while listNode:
        l.append(listNode.val)
        listNode = listNode.next
    l.reverse()
    return l


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = None

l = printListFromTailToHead(l1)
print(l)
