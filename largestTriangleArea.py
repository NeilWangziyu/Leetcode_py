class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        while(len(points)>=2):
            tem = points.pop(0)
            check = []
            for each in points:
                check.append([tem[0] - each[0],tem[1] - each[1]])


            for i in range(len(check) -1):
                for j in range(i, len(check)):
                    if (abs(check[i][1]*check[j][0] - check[i][0]*check[j][1]))/2 > max_area:
                        max_area = (abs(check[i][1]*check[j][0] - check[i][0]*check[j][1]))/2

        return max_area







points = [[8,10],[2,7],[9,2],[4,10]]


s = Solution()
print(s.largestTriangleArea(points))