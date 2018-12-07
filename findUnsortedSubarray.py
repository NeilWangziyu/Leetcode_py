class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0

        nums_order = nums.copy()
        nums_order.sort()
        if nums_order == nums:
            return 0
        # print(nums_order)
        length = len(nums)
        start = 0
        end = 0
        for i, number in enumerate(nums):
            if number != nums_order[i]:
                start = i
                break

        nums = nums[::-1]
        nums_order = nums_order[::-1]
        # print(nums_order, nums)

        for j, number in enumerate(nums):
            # print(j, number, nums_order[j])
            if number != nums_order[j]:
                end = j
                break


        return length - end - start

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

