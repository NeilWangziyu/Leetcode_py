# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None

        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        if pre[1] == post[-2]:
            # 没有左子树：
            right_length = len(pre[1:])
            right_post = post[:right_length]
            right_pre = pre[1:]
            left_pre = None
            left_post = None

        else:
            post_left_index = post.index(pre[1])
            length_left = post_left_index + 1
            left_pre = pre[1:1 + length_left]
            left_post = post[:post_left_index + 1]
            right_pre = pre[1 + length_left:]
            right_post = post[post_left_index + 1:-1]
        print(left_pre, left_post)
        print(right_pre, right_post)
        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)
        return root

    def constructFromPrePost2(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root
