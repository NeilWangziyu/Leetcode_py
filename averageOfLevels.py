# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        this_level = [[root]]
        res = []
        while (this_level):
            search = this_level.pop(0)
            next_level = []
            length = len(search)
            sum_search = 0
            for each_node in search:
                if each_node.left:
                    next_level.append(each_node.left)
                if each_node.right:
                    next_level.append(each_node.right)
                sum_search += each_node.val

            res.append(sum_search / length)
            if next_level != []:
                this_level.append(next_level)

        return res


