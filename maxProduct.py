class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(max(nums[0], nums[1]), nums[0] * nums[1])

        dp_list_pos = [0 for _ in range(len(nums))]
        dp_list_neg = [0 for _ in range(len(nums))]
        # 以i为结尾的最大乘积和最小乘积
        dp_list_pos[0] = nums[0]
        dp_list_neg[0] = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            dp_list_pos[i] = max(max(nums[i], dp_list_neg[i-1]*nums[i]), dp_list_pos[i-1] * nums[i])
            dp_list_neg[i] = min(min(nums[i], dp_list_neg[i-1]*nums[i]), dp_list_pos[i-1] * nums[i])
            max_num = max(max_num, dp_list_pos[i])

        return max_num



        # if nums[0] > 0:
        #     dp_list_pos[0] = nums[0]
        #     dp_list_neg[0] = 1
        # elif nums[0]<0:
        #     dp_list_pos[0] = 1
        #     dp_list_neg[0] = nums[0]
        # else:
        #     dp_list_neg[0] = 0
        #     dp_list_pos[0] = 0
        # # pos:if next is pos, this line is max
        # # neg: if next is neg, this list is max
        #
        #
        # max_count = nums[0]
        #
        # for i in range(1, len(nums)):
        #     if dp_list_pos[i-1] == 0:
        #         if nums[i] > 0:
        #             dp_list_pos[i] = nums[i]
        #             dp_list_neg[i] = 1
        #         elif nums[i] < 0:
        #             dp_list_pos[i] = 1
        #             dp_list_neg[i] = nums[i]
        #         else:
        #             dp_list_neg[i] = 0
        #             dp_list_pos[i] = 0
        #
        #
        #
        #
        #     else:
        #         if nums[i] == 0:
        #             dp_list_neg[i] = 0
        #             dp_list_pos[i] = 0
        #             if dp_list_pos[i - 1] > max_count:
        #                 max_count = dp_list_pos[i - 1]
        #             if 0 > max_count:
        #                 max_count = 0
        #         elif nums[i] > 0:
        #             dp_list_pos[i] = dp_list_pos[i-1] * nums[i]
        #             dp_list_neg[i] = 1



                # if nums[i] == 0:
                #     dp_list_pos[i] = 0
                #     dp_list_neg[i] = 0
                #     if dp_list_pos[i - 1] > max_count:
                #         max_count = dp_list_pos[i - 1]
                #     if max_count < 0:
                #         max_count = 0
                #
                #
                # elif dp_list_neg[i-1] > 0:
                #     if nums[i] > 0:
                #         dp_list_pos[i] = dp_list_pos[i-1] * nums[i]
                #         dp_list_neg[i] = dp_list_neg[i-1] * nums[i]
                #     else:
                #         dp_list_pos[i] = dp_list_pos[i - 1]
                #         dp_list_neg[i] = dp_list_neg[i - 1] * nums[i]
                #
                # elif dp_list_neg[i-1] < 0:
                #     if nums[i] > 0:
                #         dp_list_pos[i] = max(dp_list_pos[i - 1], nums[i])
                #         dp_list_neg[i] = dp_list_neg[i - 1] * nums[i]
                #     else:
                #         dp_list_pos[i] = max(dp_list_neg[i - 1] * nums[i], dp_list_pos[i-1])
                #         dp_list_neg[i] = dp_list_neg[i - 1] * nums[i]

        # print(dp_list_pos)
        # print(dp_list_neg)
        # print(max_count)
        # return max(max_count, dp_list_pos[-1])





s = Solution()
print(s.maxProduct(nums=[2,-5,-2,-4,3]))


