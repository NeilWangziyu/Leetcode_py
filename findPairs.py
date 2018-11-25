class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 该题需使用哈希
        if k<0:
            return 0

        count = 0
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] not in dict_num:
                dict_num[nums[i]] = 1
            else:
                dict_num[nums[i]] += 1
        if k == 0:
            return len([each for each in dict_num if dict_num[each]>1])

        for each in nums:
            if each - k in dict_num:
                count += 1
                print(each, each-k)
                dict_num.pop(each-k)
        return count

        # nums.sort()
        # res = []
        # pre_i = None
        # for i in range(len(nums)):
        #     print("prei",pre_i, nums[i])
        #     pre_j = None
        #     if nums[i] != pre_i:
        #         for j in range(i + 1, len(nums)):
        #             print("prej", pre_j, nums[j])
        #             if nums[j] != pre_j:
        #                 print(i, j)
        #                 if nums[i] + k == nums[j] or nums[j] + k == nums[i]:
        #                     res.append([nums[i], nums[j]])
        #                 pre_j = nums[j]
        #             else:
        #                 pass
        #         pre_i = nums[i]
        #     else:
        #         pass
        #
        # print(res)
        # return len(res)




s = Solution()
print(s.findPairs([1,3,1,2,4,2], k = 1))
