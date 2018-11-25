class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]

        if len(nums) == 2:
            return min(nums)

        first = 0
        end = len(nums)-1

        if nums[first] > nums[end]:
            while (end - first >1):
                mid = first + (end - first) // 2
                print(first, mid, end)
                if nums[mid] >= nums[first]:
                    first = mid
                elif nums[mid] <= nums[end]:
                    end = mid

            return min(nums[end], nums[first])

        else:
            return nums[0]


s = Solution()
print(s.findMin([1,2,3]))
