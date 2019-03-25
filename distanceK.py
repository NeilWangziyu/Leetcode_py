# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        先将二叉树展开为图在进行bfs
        in this val is unique
        """
        if not root:
            return []
        graph = {}

        def DFS(root):
            if not root:
                return
            if root.left:
                if root.val not in graph:
                    graph[root.val] = [root.left.val]
                else:
                    graph[root.val].append(root.left.val)

                if root.left.val not in graph:
                    graph[root.left.val] = [root.val]
                else:
                    graph[root.left.val].append(root.val)

                DFS(root.left)

            if root.right:
                if root.val not in graph:
                    graph[root.val] = [root.right.val]
                else:
                    graph[root.val].append(root.right.val)

                if root.right.val not in graph:
                    graph[root.right.val] = [root.val]
                else:
                    graph[root.right.val].append(root.val)
                DFS(root.right)

        DFS(root)
        if not graph:
            return []
        checked = set()
        this_level = [target.val]
        for i in range(K):
            next_target = []
            for each in this_level:
                if each not in checked:
                    checked.add(each)
                    for each_not in graph[each]:
                        if each_not not in checked:
                            next_target.append(each_not)
            if next_target:
                this_level = next_target
            else:
                return []
        return this_level






    def distanceK2(self, root, target, K):
        self.path = {}

        def findpath(node):
            if not node: return -1
            if node == target:
                self.path[node] = 0
                return self.path[node]
            l, r = findpath(node.left), findpath(node.right)
            if max(l, r) > -1:
                self.path[node] = max(l, r) + 1
                return self.path[node]
            return -1

        findpath(root)
        # print(self.path,1)
        res = []

        def findnode(dis, node):
            if not node: return
            if dis == K: res.append(node.val)
            if node.left in self.path:
                findnode(self.path[node.left], node.left)
            else:
                findnode(dis + 1, node.left)
            if node.right in self.path:
                findnode(self.path[node.right], node.right)
            else:
                findnode(dis + 1, node.right)

        findnode(self.path[root], root)
        return res
