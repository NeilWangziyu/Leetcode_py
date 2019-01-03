class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for each in nums:
            if each not in dict:
                dict[each] = 1
            else:
                dict[each] += 1
        res = []
        for each in dict.keys():
            if dict[each] == 2:
                res.append(each)
        return res

    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        b = set()
        for each in nums:
            if each  in b:
                a.append(each)
            else:
                b.add(each)
        return a


