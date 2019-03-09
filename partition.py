# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        less_than = ListNode(0)
        less_than_head = less_than
        more_than = ListNode(0)
        more_than_head = more_than
        while(head):
            if head.val < x:
                less_than.next = ListNode(head.val)
                less_than = less_than.next
            else:
                more_than.next = ListNode(head.val)
                more_than = more_than.next
            head = head.next
        less_than.next = more_than_head.next
        return less_than_head.next


    def partition2(self, head, x):
        pass
