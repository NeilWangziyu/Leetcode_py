# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode):
        if not head:
            return []
        stack = []
        root = head
        while(root):
            stack.append(root.val)
            root = root.next
        max = stack[-1]
        prev_list = [max]
        res = []
        for each in stack[::-1]:
            if each >= prev_list[-1]:
                res.insert(0, 0)
                prev_list = [each]
            else:
                i = 0
                while (each >= prev_list[i]):
                    i += 1
                res.insert(0, prev_list[i])
                prev_list = [each] + prev_list[i:]

        return res