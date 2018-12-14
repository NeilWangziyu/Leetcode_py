class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0

        total_num = len(nums)
        start = 0
        end = len(nums)-1
        while(start<=end):

            mid = (start + end) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


s = Solution()
print(s.search([-1,0,3,5,9,12],5))

