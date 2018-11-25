class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return_head = ListNode(head.val)
        while(head.next):
            head = head.next
            previous = return_head
            return_head = ListNode(head.val)
            return_head.next = previous
            head = head.next

        return return_head
s = Solution()
