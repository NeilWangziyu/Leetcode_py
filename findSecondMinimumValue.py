# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    set_v = set()

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """
        给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。
        """
        self.set_v = set()
        if not root:
            return -1
        if not root.left and not root.right:
            return -1

        def dfs(r):
            if not r:
                return
            else:
                self.set_v.add(r.val)
                dfs(r.left)
                dfs(r.right)

        dfs(root)
        if len(self.set_v) <= 1:
            return -1
        else:
            return sorted(list(self.set_v))[1]

