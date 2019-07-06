class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            if nums[0] > nums[1] * 2:
                return 0
            elif nums[1] > nums[0] * 2:
                return 1
            else:
                return -1
        res = 0
        max_tem = nums[0]
        twice = -float('inf')
        for i in range(1, len(nums)):
            print(nums[i], twice, max_tem)
            if nums[i] > max_tem:
                twice = max_tem * 2
                max_tem = nums[i]
                res = i

            else:
                if nums[i] * 2 > twice:
                    twice = nums[i] * 2
        print(twice, max_tem)
        if twice > max_tem:
            return -1
        else:
            return res


s = Solution()
print(s.dominantIndex([0,0,2,3]))