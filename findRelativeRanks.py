class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # rank = nums.copy()
        # rank.sort(reverse = True)
        rank = sorted(nums)[::-1]
        for i in range(len(rank)):
            if i == 0:
                index = nums.index(rank[i])
                nums[index] = "Gold Medal"
            elif i == 1:
                index = nums.index(rank[i])
                nums[index] = "Silver Medal"
            elif i == 2:
                index = nums.index(rank[i])
                nums[index] = "Bronze Medal"
            else:
                index = nums.index(rank[i])
                nums[index] = str(i+1)
        return nums


    def findRelativeRanks2(self, nums):
        sort = sorted(nums)[::-1]
        root = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        print(root)
        return list(map(dict(zip(sort, root)).get, nums))


s = Solution()
print(s.findRelativeRanks2([0, 5, 4, 3, 2, 1]))
