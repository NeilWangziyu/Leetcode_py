from typing import List

class item:
    def __init__(self, index, val):
        self.index = index
        self.val = val


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        length = len(arr)
        f = [0 for _ in range(length)]
        g = [0 for _ in range(length)]
        for i in range(length):
            f[i] = arr[i]
            if (i > 0 and f[i - 1] > 0):
                f[i] += f[i-1]
        for j in range(length-1, -1, -1):
            g[j] = arr[j]
            if (j < length - 1 and g[j + 1] > 0):
                g[j] += g[j + 1]

        print(f)
        print(g)

        ans = f[0]

        for k in range(length):
            ans = max(ans, max(f[k], g[k]))
            if (k + 1 < length):
                ans = max(ans, f[k] + g[k + 1])
            if (k + 2 < length):
                ans = max(ans, f[k] + g[k + 2])

        return ans

        # stack_test = []
        # max_res = -float("inf")
        # instack_val = 0
        # in_stack_min = []
        # total_in_stack_neg = 0
        # for index, num in enumerate(arr):
        #     if not stack_test:
        #         stack_test.append(item(index, num))
        #         max_res = max(max_res, instack_val)
        #         if num < 0:
        #             total_in_stack_neg = num
        #             in_stack_min.append(item(index, num))
        #
        #     else:
        #         if num >= 0:
        #             stack_test.append(item(index, num))
        #             instack_val += num
        #             max_res = max(max_res, instack_val)
        #         else:
        #             while(stack_test and stack_test[0].val <= 0):
        #                 total_in_stack_neg -= stack_test.pop(0).val
        #
        #             if not stack_test:
        #                 stack_test.append(item(index, num))
        #                 max_res = max(max_res, instack_val)
        #                 in_stack_min = num
        #                 if num < 0:
        #                     total_in_stack_neg = num
        #                 else:
        #                     total_in_stack_neg = 0
        #             else:
        #                 continue
        # return 0

class Solution2:
    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        length = len(arr)
        res = -float("inf")
        for i in range(length):
            for j in range(i+1, length+1):
                # print(arr[i:j])
                if len(arr[i:j]) > 1:
                    res = max(res, max(sum(arr[i:j]), sum(arr[i:j])-min(arr[i:j])))
                else:
                    res = max(res, sum(arr[i:j]))
        return res


s1 = Solution()
s2 = Solution2()
print(s1.maximumSum([1,-2,0,3]))
print(s2.maximumSum([1,-2,0,3]))

print(s1.maximumSum([1,-2,-2,3]))
print(s2.maximumSum([1,-2,-2,3]))

print(s1.maximumSum([-1,-1,-1,-1]))
print(s2.maximumSum([-1,-1,-1,-1]))



