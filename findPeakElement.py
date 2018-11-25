class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<0:
            return -1
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        first = 0
        end = len(nums)-1
        while (end > first):
            mid = first + (end - first) // 2
            print(mid)
            if nums[mid] >nums[mid+1]:
                end = mid
            else:
                first = mid + 1
        return first






nums = [1,2,3,4,3]
s = Solution()
print(s.findPeakElement(nums))