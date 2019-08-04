from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 0


        # one way: 0 > 1
        # the other 1 > 0
        count1 = 0
        count2 = 0

        # 0 > 1
        first_num_small = nums[0]
        for index, num in enumerate(nums):
            if index == 0:
                continue
            if index == len(nums)-1:
                if index% 2 == 0:
                    pass
                else:
                    if num >= nums[index-1]:
                        count1 += (num - nums[index-1] + 1)
                continue
            elif index % 2 != 0:
                if num >= nums[index-1] or num >= nums[index+1]:
                    count1 += (num - min(nums[index - 1], nums[index+1]) + 1)

        # 1 > 0
        for index, num in enumerate(nums):
            if index == 0:
                if num >= nums[index + 1]:
                    count2 += (num - nums[index + 1] + 1)
                continue
            if index == len(nums)-1:
                if index % 2 ==0:
                    if num >= nums[index-1]:
                        count2 += (num - nums[index - 1] + 1)
                continue
            elif index % 2 == 0:
                if num >= nums[index-1] or num >= nums[index+1]:
                    count2 += (num - min(nums[index - 1], nums[index+1]) + 1)


        return min(count2, count1)









s = Solution()

nums = [1, 2, 3]
print(s.movesToMakeZigzag(nums))

nums = [9,6,1,6,2]
print(s.movesToMakeZigzag(nums))

