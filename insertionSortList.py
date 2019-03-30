# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        def insertSort(new_list, Node):
            Node.next = None
            if not new_list:
                return Node
            head_t = new_list
            prev = None
            while (head_t and head_t.val <= Node.val):
                prev = head_t
                head_t = head_t.next
            if not prev:
                #                 first one
                Node.next = head_t
                return Node
            else:
                if not head_t:
                    prev.next = Node
                    return new_list
                else:
                    prev.next = Node
                    Node.next = head_t
                    return new_list

        new_list = None
        while (head):
            node_insert = head
            head = head.next
            new_list = insertSort(new_list, node_insert)
        return new_list



