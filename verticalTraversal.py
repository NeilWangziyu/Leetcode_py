# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode):
        overall_dict = {}

        def check_item(root, col, row):
            if not root:
                return

            if col not in overall_dict:
                overall_dict[col] = [[root.val, row]]
            else:
                overall_dict[col].append([root.val, row])
            check_item(root.left, col - 1, row + 1)
            check_item(root.right, col + 1, row + 1)

        check_item(root, 0, 0)
        res = []
        dict_keys = list(overall_dict.keys())
        dict_keys.sort()

        for each in dict_keys:
            res_tem = []
            unsort = overall_dict[each]
            s = sorted(unsort, key=lambda x: x[1] * 1000 + x[0], reverse=False)
            for each_row in s:
                res_tem.append(each_row[0])
            res.append(res_tem)
        return res


    def verticalTraversal2(self, root: 'TreeNode') -> 'List[List[int]]':
        from collections import defaultdict
        self.tree = defaultdict(lambda: defaultdict(list))
        self.dfs(root, 0, 0)
        res = list()
        for x in sorted(self.tree.keys()):
            tmp = list()
            for y in sorted(self.tree[x].keys()):
                tmp += sorted(self.tree[x][y])
            res.append(tmp)

        return res

    def dfs(self, root, x, y):
        if root:
            self.tree[x][y].append(root.val)
            self.dfs(root.left, x - 1, y + 1)
            self.dfs(root.right, x + 1, y + 1)


