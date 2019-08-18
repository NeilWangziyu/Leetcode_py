from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # stack is used to store index
        lenth = len(nums)
        res = [-1 for _ in range(lenth)]
        stack = []
        stack_len = 0
        for i in range(lenth):
            while(stack_len > 0 and nums[stack[stack_len-1]] < nums[i]):
                res[stack[stack_len-1]] = nums[i]
                stack.pop()
                stack_len -= 1
            stack.append(i)
            stack_len += 1

        # print(stack)
        # print(stack_len)

        for i in range(lenth):
            while(stack_len > 0 and nums[stack[stack_len-1]] < nums[i]):
                res[stack[stack_len-1]] = nums[i]
                stack.pop()
                stack_len -= 1

        # print(stack)
        # print(res)
        for num in stack:
            res[num] = -1

        return res

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        new_nums = nums + nums[:-1]
        dict_stack = []
        hash_map = {}
        for index, i in enumerate(new_nums):
            while(dict_stack and new_nums[dict_stack[-1]] < i):
                a = dict_stack.pop()
                hash_map[a] = i
            dict_stack.append(index)
        # print(hash_map)

        res = [-1 for _ in range(len(nums))]
        for each in hash_map.keys():
            if each < len(nums):
                res[each] = hash_map[each]
        return res



s = Solution()
nums = [1,2,1]
print(s.nextGreaterElements(nums))