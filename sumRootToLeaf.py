# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = 0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        def check(r, prev):
            if not r.right and not r.left:
                self.res += (int(prev+str(r.val),2) % (10**9+7))
            else:
                if r.left:
                    check(r.left, prev+str(r.val))
                if r.right:
                    check(r.right, prev + str(r.val))
        check(root, "")
        return (self.res) % (10**9+7)