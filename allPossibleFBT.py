# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        现在这个树一共是N个节点的话，根节点算一个，左子树一共i个，那右子树一共就N-1-i个。
        然后迭代的时候每次左边+2个，右边-2个。把所有的结果加起来就好啦。
        """
        if N == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        if N % 2 == 0:
            return []

        left_num = 1
        right_num = N - 2
        res = []

        while (right_num > 0):
            lefts = self.allPossibleFBT(left_num)
            rights = self.allPossibleFBT(right_num)
            for i in range(len(lefts)):
                for j in range(len(rights)):
                    root = TreeNode(0)
                    root.left = lefts[i]
                    root.right = rights[j]
                    res.append(root)
            left_num += 2
            right_num -= 2
        return res

    def allPossibleFBT2(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        ans = []
        if N == 0:
            return ans
        if N == 1:
            ans.append(TreeNode(0))
            return ans

        for i in range(1, (N + 1) // 2, 2):
            j = N - i - 1
            if i == j:
                # 两边是一样的
                tree = self.allPossibleFBT(i)
                for left in tree:
                    for right in tree:
                        root = TreeNode(0)
                        root.left, root.right = left, right
                        ans.append(root)
            else:
                # 两边不是一样的
                for left in self.allPossibleFBT(i)[:]:
                    for right in self.allPossibleFBT(j)[:]:
                        root = TreeNode(0)
                        root.left, root.right = left, right
                        ans.append(root)
                        root = TreeNode(0)
                        root.left, root.right = right, left
                        ans.append(root)
        return ans


s = Solution()
N = 7
print(s.allPossibleFBT(N))