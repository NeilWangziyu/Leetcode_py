class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        n**2时间复杂度
        """
        res = 0
        AB_map = {}
        for eachA in A:
            for eachB in B:
                if eachA+eachB not in AB_map:
                    AB_map[eachA + eachB] = 1
                else:
                    AB_map[eachA + eachB] += 1
        for eachC in C:
            for eachD in D:
                if -(eachC+eachD) in AB_map:
                    res += AB_map[-(eachC+eachD)]
        return res