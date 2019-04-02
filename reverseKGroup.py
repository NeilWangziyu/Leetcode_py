# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        next_node = None
        check = head
        canProceed = 0
        count = 0
        while (canProceed < k and check != None):
            check = check.next
            canProceed += 1
        if canProceed == k:
            #             reverse
            while (count < k and cur != None):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                count += 1
            if next_node != None:
                #                  // head 为链表翻转后的尾节点
                head.next = self.reverseKGroup(next_node, k)
            return prev
        else:
            return head



