class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        final_low = -1
        final_high = -1
        # check low
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    final_low = mid
                    break
                else:
                    high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if final_low == -1:
            return [-1, -1]

#         check high
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    final_high = mid
                    break
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return [final_low, final_high]



if __name__ == "__main__":
    s = Solution()
    nums = [2,2]
    target = 2
    print(s.searchRange(nums, target))

