"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 解法一： 使用hash存储原结点和克隆结点的映射关系，通过映射关系处理克隆结点的random指针
        if not head:
            return head
        node_hash = {}
        init = head
        node_hash[None] = None
        while(init):
            node_hash[init] = Node(init.val, next=None, random=Node)
            init = init.next


        init = head
        while(init):
            node_hash[init].next = node_hash[init.next]
            node_hash[init].random = node_hash[init.random]
            init = init.next
        return node_hash[head]

    def copyRandomList2(self, head: 'Node') -> 'Node':
    #     原地处理，将克隆结点放在原结点后面，在原链表上处理克隆结点的random指针，最后分离两个链表
        if not head:
            return head
        node = head
        while(node):
            tem = node.next
            node.next = Node(node.val, node.next, None)
            node = tem

        node = head
        while(node):
            if node.random:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next

        node = head

        cloneHead = head.next

        while (node.next):
            temp = node.next
            node.next = node.next.next
            node = temp
        return cloneHead




    def copyRandomList3(self, head):
        def copyNode(node, res):
            if not node: return None
            if node in res: return res[node]
            copy = Node(node.val, None, None)
            res[node] = copy
            copy.next = copyNode(node.next, res)
            copy.random = copyNode(node.random, res)
            return copy

        return copyNode(head, {})


if __name__ == "__main__":
    s = Solution()
    head = Node(1,None, None)
    head.next = Node(2, None, Node)
    head.random = head.next
    head.next.random = head.next
    res = s.copyRandomList(head)
    while(res):
        print(res.val)
        res = res.next

