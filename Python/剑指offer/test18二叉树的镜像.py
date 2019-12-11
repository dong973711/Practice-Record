# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.Mirror(root.left)
        elif root.right:
            self.Mirror(root.right)


s = Solution()
tree1 = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(5)
tree1.left = t1
tree1.right = t2
t1.left = t3
t1.right = t4

s.Mirror(tree1)
print(tree1.right.right.val)
