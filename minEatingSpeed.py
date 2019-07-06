class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math

        low = 1
        high = 1000000000

        while (low < high):
            mid = (low + high) // 2

            time = 0
            for each in piles:
                time += math.ceil(each / mid)
            if time <= H:
                high = mid
            else:
                low = mid + 1

        return low

    def minEatingSpeed2(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil
        mini_speed = ceil(sum(piles) / H)
        while 1:
            count = 0
            for x in piles:
                count += ceil(x / mini_speed)
            if count <= H:
                return mini_speed
            else:
                mini_speed += 1


s = Solution()
print(s.minEatingSpeed([312884470], 968709470))