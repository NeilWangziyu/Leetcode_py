# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # split {1,2,3,4,5} to {1,2,3}{4,5}
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        # reverse the second {4,5} to {5,4}
        cur, pre = head2, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        # merge
        cur1, cur2 = head1, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2

head = ListNode(0)
head_s = head
for i in range(1, 7):
    head.next = ListNode(i)
    head = head.next

s = Solution()
s.reorderList(head_s)

while(head_s):
    print(head_s.val)
    head_s = head_s.next





