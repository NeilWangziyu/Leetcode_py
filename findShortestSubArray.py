class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dict = {}
        for index,  each in enumerate(nums):
            if each not in dict:
                dict[each] = [index]
            else:
                dict[each].append(index)
        print(dict)

        max_length = 0
        max_num = []
        for each in dict:
            if len(dict[each]) > max_length:
                max_length = len(dict[each])
                max_num = [each]
            elif len(dict[each]) == max_length:
                max_num.append(each)

        if max_length == 1:
            return 1
        else:
            res = len(nums)
            for each in max_num:
                if dict[each][-1] - dict[each][0] < res:
                    res = dict[each][-1] - dict[each][0]
            return res + 1

    def findShortestSubArray2(self, nums):
        import collections
        dic=collections.Counter(nums)
        # 这一条语句一直都想不到
        # 诶
        ma=max(dic.values())
        if ma==1:
            return 1
        l1=[]
        l2=[]
        ll=len(nums)
        for i in dic:
            if dic[i]==ma:
                l1.append(i)
        numr=nums[::-1]
        for i in l1:
            j=nums.index(i)
            k=ll-numr.index(i)
            l=k-j
            l2.append(l)
        return min(l2)


s = Solution()
print(s.findShortestSubArray2([1, 2, 2, 3, 1]))