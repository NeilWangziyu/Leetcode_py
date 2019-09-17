# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:  # 特殊判定
            return 0
        res = 0
        temp = {}  # 定义一个temp来记录树中每一层对应的编号

        def dfs(a, k, j):
            if k not in temp:
                temp[k] = []
            temp[k].append(j)  # 将每一层对应的编号放进hash表
            if a.left:
                dfs(a.left, k + 1, j * 2)  # 编码规则，左节点为当前值的二倍
            if a.right:
                dfs(a.right, k + 1, j * 2 + 1)  # 编码规则，右节点为当前值的二倍加一

        dfs(root, 0, 0)  # 调用core函数
        for x in temp:  # 找到每一层中的编号最大差值，即为所求
            res = max(res, temp[x][-1] - temp[x][0] + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.right = TreeNode(12)
    root.left.left = TreeNode(14)

    print(s.widthOfBinaryTree(root))