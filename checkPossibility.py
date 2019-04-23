class Solution:
    # 非递减
    def checkPossibility(self, nums) -> bool:
        if not nums:
            return True
        if len(nums) < 3:
            return True
        count = 0
        if nums[1] < nums[0]:
            nums[0] = nums[1]
            count += 1

        for i in range(1, len(nums)-1):
            right = nums[i+1]
            if (nums[i] > right):
                count += 1
                if count > 1:
                    return False

                left = nums[i - 1]
                if (left > right):
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = left
        return True




nums = [4,2,3]
s = Solution()
print(s.checkPossibility(nums))


nums =[4,2,1]
print(s.checkPossibility(nums))

nums = [3,4,2,3]
print(s.checkPossibility(nums))

