# https://leetcode-cn.com/problems/palindrome-partitioning/
from typing import List
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s)+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                right_res = self.partition(right)
                for each in right_res:
                    res.append([left]+each)
        return res

    def partition2(self, s: str) -> List[List[str]]:
        if not s: return []
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif j - i > 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
        print(dp)
        res = []

        def recurse(i, tmp):
            if i >= len(s):
                res.append(tmp)
                return

            for k in range(i, len(s)):
                if dp[i][k]:
                    recurse(k + 1, tmp + [s[i:k + 1]])

        recurse(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("bb"))
    print(s.partition2("aab"))
    print(s.partition2("bb"))