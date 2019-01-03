class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1 for _ in range(len(nums))]
        max_round = 0
        for index, each in enumerate(nums):
            checked_num = set()
            if dp[index] == -1:
                i = each
                checked_num.add(each)
                check_index = [index]

                while (nums[i] not in checked_num):
                    checked_num.add(nums[i])
                    check_index.append(i)
                    i = nums[i]

                if len(check_index) > max_round:
                    max_round = len(check_index)
                # print(check_index)
                for each_index in check_index:
                    dp[each_index] = len(check_index)
        print(dp)
        return max_round


A = [5,4,0,3,1,6,2]
s = Solution()
print(s.arrayNesting(A))