# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        root_level = [root]
        max_index = 1
        max_sum = -float("inf")
        index = 1
        while (root_level):

            next_level = []
            this_level_sum = 0
            for each in root_level:
                this_level_sum += each.val
                if each.left:
                    next_level.append(each.left)
                if each.right:
                    next_level.append(each.right)
            # print(this_level_sum, max_sum)
            if this_level_sum > max_sum:
                max_index = index
                max_sum = this_level_sum
            if next_level:
                root_level = next_level
                index += 1
            else:
                break
        return max_index

