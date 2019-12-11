# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, root1, root2):
        # write code here
        if not root1 or not root1:
            return False
        return self.doesTreeHashTree2(root1, root2) or self.HasSubtree(root1.right, root2) or self.HasSubtree(
            root1.left, root2)

    def doesTreeHashTree2(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.doesTreeHashTree2(root1.left, root2.left) and self.doesTreeHashTree2(root1.right, root2.right)


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

tree2 = TreeNode(2)
t3 = TreeNode(4)
t4 = TreeNode(5)
tree2.left = t3
tree2.right = t4

print(s.HasSubtree(tree1, tree2))
