class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        //转换成01背包问题，求两堆石头的最小差值。由于石头总和为sum.则问题转换成了
        //背包最多装sum / 2的石头,stones数组里有一大堆石头。求如何装能装下最多重量石头。

        """
        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]

        sums = sum(stones)
        print(sums)
        dp = [0 for _ in range(sums//2+1)]
        for i in range(len(stones)):
            for j in range(sums//2, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])

        print(dp)
        return (sums - dp[-1]*2)

    def lastStoneWeightII2(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        '''
        把所有组合的可能的相加结果放入sets中。最好的粉碎结果是全部粉碎，
        也就是最后刚好能有两块质量一样的石头，所以在检查时从石头总重量的一半开始检查是否在sets中，
        如果不在说明不能刚好全部粉碎，最后会有剩余，故在此基础上-1
        
        set.update:add a list 
        '''
        sets = set()
        for s in stones:
            print(s, sets,  [s + c for c in sets])
            sets.update([s + c for c in sets])
            sets.add(s)
        print(sets)
        sums = sum(stones)
        halfs = sums // 2
        while halfs > 0:
            if halfs in sets:
                return sums - 2 * halfs
            halfs -= 1

    def lastStoneWeightII3(self, A):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i * 2) for i in dp)

s = Solution()
print(s.lastStoneWeightII(stones=[2,7,4,1,8,1]))
print(s.lastStoneWeightII2(stones=[2,7,4,1,8,1]))

