# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G_set = set(G)
        count = 0
        max_count = 0
        while (head):
            if head.val in G_set:
                count += 1
            else:
                if count > 0:
                    max_count += 1
                count = 0
            head = head.next

        if count > 0:
            max_count += 1

        return max_count

