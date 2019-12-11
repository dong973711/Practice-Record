# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            head = TreeNode(pre[0])
            head.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0]) + 1], tin[0:tin.index(pre[0])])
            head.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
            return head


if __name__ == '__main__':
    s = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    ans = s.reConstructBinaryTree(pre, tin)
    print(ans.right.val)
