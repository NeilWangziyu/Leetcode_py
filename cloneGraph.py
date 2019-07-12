# Definition for a Node.

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash_store = {}
        stack = []
        if not node:
            return node

        stack.append(node)
        hash_store[node] = Node(val=node.val, neighbors=[])
        while(stack):
            check = stack.pop(0)
            current = hash_store[check]
            for each in check.neighbors:
                if each not in hash_store:
                    hash_store[each] = Node(val=each.val, neighbors=[])
                    stack.append(each)
                current.neighbors.append(hash_store[each])


        return hash_store[node]



# 这题我真的一开始..完全没搞懂他在说啥



if __name__ == "__main__":
    s = Solution()

