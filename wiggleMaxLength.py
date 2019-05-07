class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return len(nums)
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)

        # prev_pos = [-1 for _ in range(len(nums)+1)]
        # prev_neg = [-1 for _ in range(len(nums)+1)]
        # prev_neg[0] = 0
        # prev_pos[0] = 0
        # for index, each in enumerate(nums):
        #     if index == 0:
        #         prev_pos[index+1] = 1
        #         prev_neg[index+1] = 1
        #         continue
        #     if each > nums[index-1]:
        #         prev_pos[index+1] = prev_neg[index] + 1
        #         i = index
        #         max_prev_pos = 0
        #         while(i >= 0):
        #             if nums[i] > each:
        #                 max_prev_pos = max(max_prev_pos, prev_pos[i])
        #             i -= 1
        #         prev_neg[index+1] = max_prev_pos + 1
        #         print(each, max_prev_pos)
        #     elif each < nums[index-1]:
        #         print(each)
        #         prev_neg[index+1] = prev_pos[index] + 1
        #         i = index
        #         max_prev_neg = 0
        #         while (i >= 0):
        #             if nums[i] < each:
        #                 max_prev_neg = max(max_prev_neg, prev_neg[i])
        #             i -= 1
        #         prev_pos[index+1] = max_prev_neg + 1
        #     else:
        #         i = index
        #         while (i > 0):
        #             if nums[i] < each:
        #                 break
        #             i -= 1
        #         prev_pos[index+1] = prev_neg[i] + 1
        #         i = index
        #         while (i > 0):
        #             if nums[i] > each:
        #                 break
        #             i -= 1
        #         prev_neg[index+1] = prev_pos[i] + 1
        # print(prev_pos, prev_neg)
        # return max(prev_neg[-1], prev_pos[-1])






nums = [1,17,5,10,13,15,10,5,16,8]
s = Solution()
print(s.wiggleMaxLength(nums))