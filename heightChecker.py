class Solution:
    def heightChecker(self, heights) -> int:
        # ？？？
        # 这题目意思不清楚
        if not heights:
            return 0
        if len(heights) == 1:
            return 1

        dp = [-1 for _ in range(len(heights))]
        dp[0] = 0

        for index, each in enumerate(heights):
            trace = index - 1
            while(trace>=0):
                if heights[trace] <= each:
                    break
                trace -= 1
            if trace >= 0:
                dp[index] = dp[trace] + 1
            else:
                dp[index] = 1
        print(dp)
        return len(dp) - max(dp)


    def heightChecker2(self, heights) -> int:
        true_list = sorted(heights)
        count = 0
        for index, each in enumerate(true_list):
            if each != heights[index]:
                count += 1
        return count






heights = [1,1,4,2,1,3]

s = Solution()
print(s.heightChecker(heights))
print(s.heightChecker2(heights))

heights = [1,2,1,2,1,1,1,2,1]
print(s.heightChecker(heights))
print(s.heightChecker2(heights))