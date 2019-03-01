# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        hi = n
        while (low < hi):
            mid = (low + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                low = mid + 1
        return hi
