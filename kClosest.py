class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        #二分法
        """
        def rank(length, res):
            if len(res) == 1:
                if length > res[0]:
                    return 1
                else:
                    return 0
            # if length <= min(res):
            #     return 0
            # elif length >= max(res):
            #     return len(res)
            lo = 0
            hi = len(res)
            mid = (lo + hi) // 2
            while (lo < hi):
                if length == res[mid]:
                    return mid
                elif length < res[mid]:
                    hi = mid
                else:
                    lo = mid + 1
                mid = (lo + hi) // 2
            return mid

        res_l = []
        res_raw = []
        if K == 0:
            return res_raw
        if not points:
            return res_raw

        for each in points:
            if not res_raw:
                res_l = [each[0] ** 2 + each[1] ** 2]
                res_raw = [each]
            else:
                length = each[0] ** 2 + each[1] ** 2
                index = rank(length, res_l)
                res_raw.insert(index, each)
                res_l.insert(index, length)
        return res_raw[:K]

points = [[-2,10],[-4,-8],[10,7],[-4,-7]]

k = 3
s = Solution()
print(s.kClosest(points, k))