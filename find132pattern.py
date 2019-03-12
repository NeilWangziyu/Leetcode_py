class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        min_min = -float('inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min_min:
                return True
            while (stack and nums[i] > stack[-1]):
                #                 stack[-1]始终放i之后，遇见过的最小的数字
                min_min = stack.pop()
            stack.append(nums[i])
        return False


if __name__ == "__main__":
     nums = [3, 1, 4, 2]
     s = Solution()
     print(s.find132pattern(nums))








