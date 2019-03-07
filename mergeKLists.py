# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):

        list_sum = []
        for each in lists:
            while(each!=None):
                list_sum.append(each.val)
                each = each.next
        list_sum.sort()
        head = ListNode(None)
        first = head
        for each in list_sum:
            head.next = ListNode(each)
            head = head.next
        return first.next


    def mergetwolists(self,l1,l2):#首先合并两个链表的
        l3 = ListNode(0)#空链表
        cur = l3
        while (l1 != None) & (l2!=None):
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        l3 = l3.next
        return l3
    def mergeKLists2(self, lists) -> ListNode:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.mergetwolists(lists[0],lists[1])
        temp = [self.mergetwolists(lists[0],lists[1])]
        if len(lists)>=3:
            for i in range(0,len(lists)-2):
                temp.append(self.mergetwolists(temp[i],lists[i+2]))
            return temp[len(lists)-2]
