from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        if not hours:
            return 0

        work_day = [1 if hours[x] > 8 else -1 for x in range(len(hours))]
        print(work_day)

        ans = 0
        for i in range(len(hours)):
            tem = 0
            for j in range(i, len(hours)):
                tem += work_day[j]

                if (tem > 0):
                    ans = max(ans, j-i+1)

        return ans

if __name__ == "__main__":
    hours = [9,9,6,0,6,6,9]
    s = Solution()
    print(s.longestWPI(hours))



