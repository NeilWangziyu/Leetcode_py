class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        dict_num = {}
        for each in nums:
            if each not in dict_num:
                dict_num[each] = 1
            else:
                dict_num[each] += 1
        print(dict_num.keys())
        print(dict_num)
        res = sorted(dict_num.keys(), key=lambda x:dict_num[x], reverse=True)
        print(res[:k])

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,2,2,2,3,4], k = 2))


