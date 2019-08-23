# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = ListNode(-1)
        odd_head = odd
        even = ListNode(-1)
        even_head = even
        c = 0
        while(head):
            if c % 2 == 0:
                even.next = ListNode(head.val)
                even = even.next
                head = head.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next
                head = head.next
            c += 1
        # if odd_head.next:
        #     odd.next = even_head.next
        #     res = odd_head.next
        #     return res
        # else:
        #     return even_head.next
        if even_head.next:
            even.next = odd_head.next
            res = even_head.next
            return res
        else:
            return even_head.next

    def oddEvenList2(self, head: ListNode) -> ListNode:
        # 遍历链表分成奇数链表和偶数链表，然后用奇数链表的尾节点指向偶数链表的头节点
        if not head or not head.next:
            return head
        odd_head, even_head, odd, even = head, head.next, head, head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return odd_head

