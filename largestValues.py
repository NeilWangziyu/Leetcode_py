# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        check_this = [root]
        while (check_this):
            next_check = []
            this_level = check_this
            this_level_all = []
            for each in this_level:
                this_level_all.append(each.val)
                if each.left:
                    next_check.append(each.left)
                if each.right:
                    next_check.append(each.right)
            res.append(max(this_level_all))
            check_this = next_check
        return res

