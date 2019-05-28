class Solution:
    def numMovesStonesII(self, stones):
        if not stones:
            return [0, 0]
        stones_sorted = sorted(stones)
        # print(stones_sorted)
        first = stones_sorted[0]
        last = stones_sorted[-1]
        total_number = len(stones_sorted)

        space = last - first - total_number + 1
        place_hold = min(stones_sorted[1] - stones_sorted[0] - 1, stones_sorted[-1] - stones_sorted[-2] - 1)
        max_number = space - place_hold

        min_number = float('inf')
        j = 0
        for i in range(total_number):
            while (j + 1 < total_number  and stones_sorted[j + 1] - stones_sorted[i] + 1 <= total_number):
                j += 1

            cost = total_number - (j - i + 1)
            if j - i + 1 == total_number - 1 and stones_sorted[j] - stones_sorted[i] + 1 == total_number - 1:
                # 空间，真实数字都差一个
                cost = 2

            min_number = min(min_number, cost)
        return [min_number, max_number]

    def numMovesStonesII2(self, stones):
        # maximum
        s_stones = sorted(stones)
        n = len(s_stones)

        mx = s_stones[-1] - s_stones[0] + 1 - n
        unavail = min(s_stones[n - 1] - s_stones[n - 2] - 1, s_stones[1] - s_stones[0] - 1)
        mx -= unavail

        # minimum 这里mi=mx是给最小值附一个值方便在后面更新mi的值
        mi = mx
        i = 0
        j = 0
        for i in range(n):
            while j < n - 1 and s_stones[j + 1] - s_stones[i] + 1 <= n:
                j += 1
                cost = n - (j - i + 1)
                if j - i + 1 == n - 1 and s_stones[j] - s_stones[i] + 1 == n - 1:
                    cost = 2
                # 更新值
                mi = min(mi, cost)
        return [mi, mx]


s = Solution()
stones = [7,4,9]
print(s.numMovesStonesII(stones))

stones = [1,2,5]
print(s.numMovesStonesII(stones))

stones = [6,5,4,3,10]
print(s.numMovesStonesII(stones))

stones = [6,5,4,3,10,11]
print(s.numMovesStonesII(stones))

stones = [100,101,104,102,103]
print(s.numMovesStonesII(stones))