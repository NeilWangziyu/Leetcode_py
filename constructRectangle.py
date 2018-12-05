class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        t = int(math.sqrt(area))
        while(area%t!=0):
            t = t -1
        return [area//t,t]





s = Solution()
print(s.constructRectangle(6))
