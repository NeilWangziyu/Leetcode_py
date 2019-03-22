# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        res = head
        while (head):
            if not head.next:
                break
            head_Val = head.val
            head.val = head.next.val
            head.next.val = head_Val

            try:
                head = head.next.next
            except:
                break
        return res

    def swapPairs2(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head



