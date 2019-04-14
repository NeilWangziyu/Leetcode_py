# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    max_diff = -1

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return

        def pre_order(root, max_prev_val, min_perv_val):
            if not root:
                return
            if max_prev_val == None:
                max_prev_val = root.val
                min_perv_val = root.val
            else:
                self.max_diff = max(self.max_diff, max(abs(max_prev_val - root.val), abs(min_perv_val - root.val)))
            if root.left:
                pre_order(root.left, max(max_prev_val, root.val), min(min_perv_val, root.val))
            if root.right:
                pre_order(root.right, max(max_prev_val, root.val), min(min_perv_val, root.val))

        pre_order(root, None, None)
        return self.max_diff
