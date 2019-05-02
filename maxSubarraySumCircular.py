class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        # if not A:
        #     return None


        max_sum = -float('inf')
        min_sum = float('inf')
        min_prev_sum = 0
        max_prev_sum = 0
        total_sum = 0
        flag = False
        for each in A:
            if each > 0: flag = True
            max_prev_sum = max(max_prev_sum, 0) + each
            min_prev_sum = min(min_prev_sum, 0) + each
            max_sum = max(max_prev_sum, max_sum)
            min_sum = min(min_prev_sum, min_sum)
            total_sum += each
        if flag:
            # 存在大于0的数
            return max(max_sum, total_sum - min_sum)
        # max_sum:最大连续递增和
        # min_sum:最小连续递增和
        else:
            return max_sum

    def maxSubarraySumCircular2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        curr_max = 0
        result_max = 0

        for num in A:
            curr_max += num
            if curr_max <= 0:
                curr_max = 0
            if curr_max > result_max:
                result_max = curr_max

        if result_max == 0:
            result = max(A)
            return result

        curr_min = 0
        result_min = 0

        for num in A:
            curr_min += num
            if curr_min >= 0:
                curr_min = 0
            if curr_min < result_min:
                result_min = curr_min

        result = max(result_max, sum(A) - result_min)

        return result


A = [1,-2,3,-2]
s = Solution()
print(s.maxSubarraySumCircular(A))