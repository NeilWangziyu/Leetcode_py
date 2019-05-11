class Solution:
    def isBoomerang(self, points) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[2] == points[1]:
            return False

        if points[0][0] != points[1][0]:
            K = (points[0][1] - points[1][1])/(points[0][0] - points[1][0])
            b = points[0][1] - K * (points[0][0])

            if points[2][1] == points[2][0]* K + b:
                return False
            else:
                return True
        else:
            if points[2][0] == points[0][0]:
                return False
            else:
                return True


    def isBoomerang2(self, points) -> bool:

        return (points[1][0] - points[0][0]) * (points[2][1] - points[0][1]) - (
                    (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])) != 0



s = Solution()
print(s.isBoomerang(points=[[1,1],[2,2],[3,3]]))