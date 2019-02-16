class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        if len(points) < 4:
            return 0
        MAX = 10000
        dict_X = set()
        res = float('inf')
        for i in range(len(points)):
            for j in range(len(points)):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    continue
                if (points[i][0]*MAX+points[j][1]) in dict_X and (points[j][0]*MAX+points[i][1]) in dict_X:
                    res = min(res, abs(points[i][0]-points[j][0]) * abs(points[i][1]-points[j][1]) )

            dict_X.add(points[i][0]*MAX+points[i][1])

        if res == float('inf'):
            return 0
        else:
            return res

    def minAreaRect2(self, points):
        """
               :type points: List[List[int]]
               :rtype: int
               """
        mem = set()
        result = float("inf")
        for x1, y1 in points:
            for x2, y2 in mem:
                if (x1, y2) in mem and (x2, y1) in mem:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < result:
                        result = area
            mem.add((x1, y1))
        return result if result != float("inf") else 0


points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
s = Solution()
print(s.minAreaRect2(points))