class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_m = m
        min_n = n
        for each in ops:
            if each[0] < min_m:
                min_m = each[0]
            if each[1] < min_n:
                min_n = each[1]
        return min_m*min_n






m = 3
n = 3
operations = [[2,2],[3,3]]

s = Solution()
print(s.maxCount(m, n, ops=operations))