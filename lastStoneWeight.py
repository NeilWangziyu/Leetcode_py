class Solution:
    def lastStoneWeight(self, stones) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        stones.sort(reverse=True)
        stoneA = stones[0]
        stoneB = stones[1]
        if stoneA == stoneB:
            return self.lastStoneWeight(stones[2:])
        else:
            return self.lastStoneWeight(stones[2:] + [abs(stoneA-stoneB)])





stones = [2,7,4,1,8,1]
s = Solution()
print(s.lastStoneWeight(stones))