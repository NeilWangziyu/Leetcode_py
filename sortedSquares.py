class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for each in A:
            res.append(each * each)
        res.sort()
        return res



str = [-7,-3,2,3,11]

s = Solution()
print(s.sortedSquares(str))