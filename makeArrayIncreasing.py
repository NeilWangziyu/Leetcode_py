from typing import List
import bisect
# https://leetcode-cn.com/contest/weekly-contest-153/problems/make-array-strictly-increasing/
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        def dfs(st, val):
            if st == len(arr1):
                return 0
            if (st, val) in dp:
                return dp[(st, val)]
            res = float("inf")
            if arr1[st] > val:
                res = dfs(st + 1, arr1[st])
            index = bisect.bisect_right(arr2, val)
            if index != len(arr2):
                res = min(res, dfs(st + 1, arr2[index]) + 1)
            dp[(st, val)] = res
            return res

        dp = {}
        arr2.sort()
        res = dfs(0, -1)
        return res if res != float("inf") else -1

