class Solution(object):
    # def minAreaFreeRect(self, points):
    #     """
    #     :type points: List[List[int]]
    #     :rtype: float
    #     """
    #     length_dict = {}
    #     for i in range(len(points)):
    #         for j in range(i+1, len(points)):
    #             # print(points[i], points[j])
    #             if points[i][0] == points[j][0]:
    #                 K = float('inf')
    #                 length2 = (points[i][0] - points[i][1])**2 + (points[j][0] - points[j][1])**2
    #
    #
    #             else:
    #                 K = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
    #                 length2 = (points[i][0] - points[i][1])**2 + (points[j][0] - points[j][1])**2
    #
    #             if length2 not in length_dict:
    #                 length_dict[length2] = [(K,points[i], points[j])]
    #             else:
    #                 length_dict[length2].append((K,points[i], points[j]))
    #     # print(length_dict)
    #
    #     min_res = float('inf')
    #     for each in length_dict.keys():
    #         if len(length_dict[each]) >= 2:
    #             print(each, length_dict[each])
    #             for i in range(len(length_dict[each])):
    #                 for j in range(i+1, len(length_dict[each])):
    #                     if length_dict[each][i][0] == 0:
    #                         if length_dict[each][j][0] == float('inf'):
    #                                 min_res = min(min_res, each)
    #                     elif length_dict[each][i][0] == float('inf'):
    #                         if length_dict[each][j][0] == 0:
    #                                 min_res = min(min_res, each)
    #                     else:
    #                         if length_dict[each][i][0]*length_dict[each][j][0]==-1:
    #                                 min_res = min(min_res, each)
    #
    #     return min_res

    def minAreaFreeRect(self, points):
        """
        其实这题的思路就是比较简单的，暴力求解
        """
        res = 0  # 已知，所有的点都是不同的
        d = dict()  # 存储中点坐标相同的点序号列表，相同则可以进入下一步判断（使用坐标和代替中点坐标）
        num = len(points)
        for i in range(num - 1):
            for j in range(i, num):
                x = points[i][0] + points[j][0]
                y = points[i][1] + points[j][1]
                if (x, y) not in d:
                    d[(x, y)] = []
                d[(x, y)].append((i, j))
        print(d)
        for key in d:
            if len(d[key]) < 2:
                continue
            dl = dict()  # 存储边长和边向量坐标
            for i, j in d[key]:
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                l = dx * dx + dy * dy
                if l not in dl:
                    dl[l] = []
                dl[l].append((dx, dy))
            for l in dl:
                if len(dl[l]) < 2:
                    continue
                # 出现矩形，对于圆的内接矩形而言，邻边长度差越大则面积越小，这里直接用对角向量叉积求取面积
                num = len(dl[l])
                for i in range(num - 1):
                    for v2 in dl[l][i:]:
                        v1 = dl[l][i]
                        area = abs(v1[0] * v2[1] - v2[0] * v1[1])  # 实际面积的两倍
                        if area:
                            if not res or area < res:
                                res = area
        if res:
            res /= 2.0
        return res







s = Solution()
points = [[1,2],[2,1],[1,0],[0,1]]
print(s.minAreaFreeRect(points))

points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
print(s.minAreaFreeRect(points))

points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
print(s.minAreaFreeRect(points))


points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
print(s.minAreaFreeRect(points))
