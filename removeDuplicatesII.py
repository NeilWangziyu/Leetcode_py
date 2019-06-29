# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        init = 0
        right = 1
        length = len(nums)
        while(right < length):
            if nums[right] != nums[init]:
                init = right
                right += 1
            else:
                if right - init == 1:
                    right += 1
                    continue
                else:
                    nums.pop(right)
                    length -= 1
        return length

    def removeDuplicates2(self, nums) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[l] != nums[l - 1]:
                if l == r:
                    l += 1
                else:
                    l += 1
                    nums[l] = nums[r]
            else:
                if nums[r] != nums[l]:
                    l += 1
                    nums[l] = nums[r]
        return len(nums[:l + 1])


nums = [1,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))