class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        num_set = set(nums)
        # print(num_set)
        res = []
        for i in range(1,len(nums)+1):
            if i not in num_set:
                res.append(i)
        return res


s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))