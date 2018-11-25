class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        length = len(nums)
        tem = nums[0]
        head = nums[0]
        res = []
        for i in range(1, length):
            if nums[i] == tem + 1:
                tem = nums[i]
            else:
                if tem == head:
                    res.append(str(tem))
                    tem = nums[i]
                    head = nums[i]
                else:
                    res.append(str(head)+"->"+str(tem))
                    tem = nums[i]
                    head = nums[i]

        if head == nums[-1]:
            res.append(str(head))
        else:
            res.append(str(head) + "->" + str(tem))

        return res


s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))
