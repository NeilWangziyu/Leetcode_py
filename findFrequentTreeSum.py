# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def return_list_of_each(root):
            if not root.left and not root.right:
                return [root.val]
            t = root.val
            if root.left:
                left_list = return_list_of_each(root.left)
                t += left_list[0]
            else:
                left_list = []
            if root.right:
                right_list = return_list_of_each(root.right)
                t += right_list[0]
            else:
                right_list = []
            return [t] + left_list + right_list

        if not root:
            return []

        res_list = return_list_of_each(root)
        # print(res_list)
        from collections import Counter
        res = Counter(res_list).most_common()
        # print(res)
        highest = res[0][1]
        return_list = []
        for each in res:
            if each[1] == highest:
                return_list.append(each[0])
        return return_list







