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

        if nums[first] >= nums[end]:
            while (end - first >1):
                mid = first + (end - first) // 2
                print(first, mid, end)
                if nums[mid] > nums[first]:
                    first = mid
                elif nums[mid] < nums[end]:
                    end = mid
                elif nums[mid] == nums[end] and nums[mid] == nums[first]:
                    return min(self.findMin(nums[mid:end]) ,self.findMin(nums[first:mid]))
                elif nums[mid] == nums[end]:
                    end = mid
                else:
                    first = mid

            return min(nums[end], nums[first])

        else:
            return nums[0]



# num = [3,4,5,1,2,3]
# num = [2,2,2,0,1]
num = [10,1,10,10,10]

s = Solution()
print(s.findMin(num))
