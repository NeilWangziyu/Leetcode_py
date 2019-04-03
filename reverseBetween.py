# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverse(start, end, next_node):
            print(start.val, end.val)
            new_start = next_node
            while (start != end):
                tem = new_start
                new_start = start
                start = start.next
                new_start.next = tem
            tem = new_start
            tem = new_start
            new_start = start
            new_start.next = tem
            return new_start

        if n - m < 1:
            return head

        if m != 1:
            start = head
            c = 0
            while (c < m - 2):
                head = head.next
                c += 1
            init = head
            while (c < n - 1):
                head = head.next
                c += 1
            end = head
            init.next = reverse(init.next, end, end.next)
            return start
        else:
            start = head
            c = 0
            while (c < n - 1):
                head = head.next
                c += 1
            end = head
            return reverse(start, end, end.next)

    def reverseBetween2(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        Head = dummy
        for i in range(m - 1):
            Head = Head.next
        pre = Head.next
        node = pre.next
        while node and m < n:
            pre.next = node.next
            node.next = Head.next
            Head.next = node
            node = pre.next
            m += 1
        return dummy.next

if __name__ == "__main__":
    s = Solution()
