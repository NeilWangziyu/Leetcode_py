class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]

        ans = []
        dict_use = {}
        # for i, num in enumerate(nums):
        #     if num not in dict_use:
        #         dict_use[num] = True
        #
        #         n = nums[:i] + nums[i + 1:]
        #         for temp_list in self.permuteUnique(n):
        #             ans.append([num] + temp_list)
        #         print('-----End-----')
        #     else:
        #         print("used")
        #         pass
        # return ans

        for i in range(len(nums)):
            if nums[i] not in dict_use:
                dict_use[nums[i]] = True
                n = nums[:i]+nums[i+1:]
                for tem in self.permuteUnique(n):
                    ans.append([nums[i]]+tem)
            else:
                pass
        return ans




s = Solution()
print(s.permuteUnique([1,1,2]))