class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        if len(nums) < 2:
            return False

        nums_dict = {}
        index_min = 100000000
        for index, number in enumerate(nums):
            if number not in nums_dict:
                nums_dict[number] = index
            else:
                delta_index = abs(index - nums_dict[number])
                if delta_index < index_min:
                    index_min = delta_index
                    nums_dict[number] = index

        if index_min == 100000000:
            return False
        if index_min<=k:
            return True
        else:
            return False






        # index_dict = {}
        # min_index = 10000
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         # print(i,j)
        #         if nums[i] == nums[j]:
        #             index = abs(i - j)
        #             # if index not in index_dict:
        #             #     index_dict[index] = 1
        #             if index < min_index:
        #                 min_index = index
        #
        # # each_index = list(index_dict.keys())
        # # if not each_index:
        # #     return False
        # if min_index == 10000:
        #     return False
        #
        # # if min(each_index) <= k:
        # if min_index <= k:
        #     return True
        # else:
        #     return False


# k =35000

nums = [1,2,1,3]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums, k))