class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) == 1:
            return 1


        points_sorted = sorted(points, key=lambda x:x[1])
        print(points_sorted)

        check_point_init = 1
        end = points_sorted[0][1]
        for i in range(len(points_sorted)):
            if points_sorted[i][0] <= end:
                continue
            else:
                check_point_init += 1
                end = points_sorted[i][1]
        return check_point_init






if __name__ == "__main__":
    s = Solution()
    points = [[10,16], [2,8], [1,6], [7,12]]

    print(s.findMinArrowShots(points))