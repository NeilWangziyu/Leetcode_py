# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    hash_dict = {}
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        这道题好像解答有问题..
        """
        if not root:
            return False

        if root.val in self.hash_dict:
            return True
        else:
            self.hash_dict[k - root.val] = True
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


    def findTarget2(self, root, k):
        s = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            s.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for num in s:
            if k - num in s and 2 * (k - num) != k:
                return True
        return False

    def findTarget3(self, root, k):
        hash_dict = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            hash_dict[node.val] = True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for each in hash_dict:
            if k - each in hash_dict and 2*(k-each)!=k:
                return True
        return False







