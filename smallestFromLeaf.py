# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        import collections
        res = 'z'*1000
        que = collections.deque([root])
        pre = collections.deque([''])
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                prefix = pre.popleft()
                char = chr(node.val+ord('a'))
                if not (node.left or node.right):
                    res = min(res, (prefix+char)[::-1])
                    continue
                if node.left:
                    pre.append(prefix+char)
                    que.append(node.left)
                if node.right:
                    pre.append(prefix+char)
                    que.append(node.right)
        return res
