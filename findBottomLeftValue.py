# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def find_left(root, depth):
            if not root:
                return -1, -1

            if not root.left and not root.right:
                return depth, root.val

            else:
                if root.left:
                    left_depth, left_val = find_left(root.left, depth + 1)
                else:
                    left_depth, left_val = -1, -1

                if root.right:
                    right_depth, right_val = find_left(root.right, depth + 1)
                else:
                    right_depth, right_val = -1, -1


                if left_depth >= right_depth:
                    return left_depth, left_val

                else:
                    return right_depth, right_val

        _, val = find_left(root, 0)
        return val


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)



s = Solution()
print(s.findBottomLeftValue(root))