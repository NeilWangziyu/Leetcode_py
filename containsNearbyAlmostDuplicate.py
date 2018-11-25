class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
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
        index_min = k+1
        for index, number in enumerate(nums):
            if nums_dict != {}:
                for tem in range(number-t, number+t+1):
                    print(tem)
                    if tem in nums_dict:
                        delta_index = abs(index - nums_dict[tem])
                        if delta_index < index_min:
                            index_min = delta_index
                            nums_dict[number] = index

                    if index_min <= k:
                        return True

            if number not in nums_dict:
                nums_dict[number] = index
        return False


        # if index_min == 100000000:
        #     return False
        # if index_min<=k:
        #     return True
        # else:
        #     return False

        # return index_min






# nums =  [1,2,3,1]
# k = 3
# t = 0


nums = [-1,2147483647]
k = 1
t = 2147483647

s = Solution()
print(s.containsNearbyAlmostDuplicate(nums, k,t))