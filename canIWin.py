class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        cache = {}

        def dp(cur, used):
            if used in cache:
                return cache[used]
            print(cache)

            for i in range(maxChoosableInteger, 0, -1):
                if used & (1 << i):
                    # 说明i已经使用过了，继续下一个
                    continue
                if cur + i >= desiredTotal:
                    cache[used] = True
                    return True
                if not dp(cur + i, used | (1 << i)):
                    cache[used] = True
                    return True
            cache[used] = False
            return False

        return dp(0, 0)


    def canIWin2(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
            if maxChoosableInteger > desiredTotal:
                return True
            if sum(range(maxChoosableInteger + 1)) < desiredTotal:
                return False

            def win(max_num, total, visited, status):
                if status.get(visited):
                    return status.get(visited)
                for i in range(1, max_num + 1):
                    tmp = 1 << i
                    if visited & tmp == 0:
                        if i >= total or not win(max_num, total - i, visited | tmp, status):
                            status[visited] = True
                            return True
                status[visited] = False
                return False

            status = {}
            return win(maxChoosableInteger, desiredTotal, 0, status)


maxChoosableInteger = 10
desiredTotal = 11
s = Solution()
print(s.canIWin(maxChoosableInteger, desiredTotal))
