# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # From answer
        self.p1 = None
        def dfs(now):
            if now == None:
                return
            if now.val == x:
                self.p1 = now
                return
            dfs(now.left)
            dfs(now.right)
        def count(now):
            if now == None:
                return 0
            return 1 + count(now.left) + count(now.right)
        dfs(root)
        l = count(self.p1.left)
        r = count(self.p1.right)
        top = n - l - r - 1
        if top > l+r+1 or l > top+r+1 or r > top+l+1:
            return True
        return False






