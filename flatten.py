
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class Solution:

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        list_res = []

        def preOrder(root):
            if not root: return None

            list_res.append(root.val)
            if root.child:
                preOrder(root.child)
            if root.next:
                preOrder(root.next)

        preOrder(head)
        start = Node(0, None, None, None)
        res = start
        for each in list_res:
            # print(each)
            start.next = Node(each, start, None, None)
            start = start.next
        if res.next:
            res.next.prev = None
        return res.next




