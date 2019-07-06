class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)<1:
            return 0
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[1]>nums[0]:
                return 2
            else:
                return 1
        new_list = []
        for i in range(len(nums)-1):
            new_list.append(nums[i+1]-nums[i])

        print(new_list)
        count = 0
        max_num = 0
        for i in range(len(new_list)):
            if count > max_num:
                max_num = count
            if new_list[i] <= 0:
                count = 0
            else:
                count += 1

            if count > max_num:
                max_num = count
        return max_num + 1





s = Solution()
print(s.findLengthOfLCIS([1,1,1,1,1]))




