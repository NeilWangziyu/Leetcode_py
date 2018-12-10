# https://leetcode-cn.com/problems/maximum-binary-tree/submissions/

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            max_num = max(nums)
            max_index = nums.index(max_num)
            res_root = TreeNode(max_num)

            if max_index == 0:
                left_num = None
                right_num = nums[max_index + 1:]
            elif max_index == len(nums):
                left_num = nums[:max_index]
                right_num = None
            else:
                left_num = nums[:max_index]
                right_num = nums[max_index + 1:]
            res_root.left = self.constructMaximumBinaryTree(left_num)
            res_root.right = self.constructMaximumBinaryTree(right_num)

            return res_root
