# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return head
        head_ptr = head
        all_num = []
        sum_init = 0
        sum_num = [0]
        while (head_ptr):
            sum_init += head_ptr.val
            sum_num.append(sum_init)
            all_num.append(head_ptr.val)
            head_ptr = head_ptr.next
        tem_dict = {}
        for i in range(len(sum_num)):
            if sum_num[i] not in tem_dict:
                tem_dict[sum_num[i]] = i
            else:
                # print(i, tem_dict[sum_num[i]])
                init = tem_dict[sum_num[i]]
                delete_num = i - init
                c = 0
                head_ptr = head
                if init != 0:
                    while (c < init - 1):
                        head_ptr = head_ptr.next
                        c += 1
                    head_ptr2 = head_ptr
                    p = 0
                    while (p < delete_num):
                        p += 1
                        head_ptr2 = head_ptr2.next
                    head_ptr.next = head_ptr2.next

                    return self.removeZeroSumSublists(head)
                else:
                    delete_num = i
                    p = 0
                    while (p < delete_num):
                        head = head.next
                        p += 1
                    return self.removeZeroSumSublists(head)
        return head


s = Solution()

