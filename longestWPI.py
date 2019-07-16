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


    def longestWPI_DP(self, hours: List[int]) -> int:
        a = []
        for x in hours:
            a.append(-1 if x <= 8 else 1)

        ret = 0
        s = 0
        deepest = []
        deepest_index = []

        print(a)

        for i in range(len(a)):
            s += a[i]
            if s > 0:
                ret = i + 1
            else:

                p = -s

                print(s, p, i)

                if p < len(deepest_index) and i - deepest_index[p] >ret:
                    # 说明这段时间内，是高于0的
                    ret = i - deepest_index[p]

                if s < 0 and (len(deepest)==0 or deepest[-1]> s):
                    deepest.append(s)
                    deepest_index.append(i)

        print(deepest)
        print(deepest_index)

        return ret


if __name__ == "__main__":
    hours = [9,9,6,0,6,6,6,6,9,9,9,9,9,9]
    s = Solution()
    print(s.longestWPI(hours))
    print("------------")

    print(s.longestWPI_DP(hours))




