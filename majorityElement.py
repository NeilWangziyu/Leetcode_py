class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_count = {}
        hreshold = len(nums) // 3
        res = []
        for each in nums:
            if each not in dict_count:
                dict_count[each] = 1
                if dict_count[each] > hreshold:
                    dict_count[each] = "full"
                    res.append(each)
            elif dict_count[each] != "full":
                dict_count[each] += 1
                if dict_count[each] > hreshold:
                    dict_count[each] = "full"
                    res.append(each)
            else:
                pass
        return res


s = Solution()
print(s.majorityElement([3,2,3]))
