class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        new_nums = nums + nums[:-1]
        print(new_nums)
        dict_stack = []
        hash_map = {}
        for index, i in enumerate(new_nums):
            while(dict_stack and new_nums[dict_stack[-1]] < i):
                a = dict_stack.pop()
                hash_map[a] = i
            dict_stack.append(index)
        print(hash_map)

        res = [-1 for _ in range(len(nums))]
        for each in hash_map.keys():
            if each < len(nums):
                res[each] = hash_map[each]
        return res

    def nextGreaterElements2(self, nums):
        ans = [-1 for _ in nums]
        stack = []

        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                ans[stack.pop()] = val
            stack.append(i)

        for val in nums:
            while stack and nums[stack[-1]] < val:
                ans[stack.pop()] = val
        return ans



nums = [1,2,1]
s = Solution()
print(s.nextGreaterElements(nums))
nums = [100,1,11,1,120,111,123,1,-1,-100]
print(s.nextGreaterElements(nums))
