class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum_total = sum(nums)
        set_num = set(nums)
        sum_unique = sum(set_num)
        len_unique = len(set_num)
        return (sum_total - sum_unique) // (length - len_unique)

#         one very interesting way
#         head = slow = fast = nums[0]

#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break
#         while head != slow:
#             head = nums[head]
#             slow = nums[slow]
#         return head

