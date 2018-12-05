class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_c = 0
        for each in nums:
            if each == 1:
                count += 1
            else:
                if count > max_c:
                    max_c = count
                count = 0
        if nums[-1] == 1:
            if count > max_c:
                max_c = count
        return max_c

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))