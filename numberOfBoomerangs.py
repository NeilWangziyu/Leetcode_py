class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dis(x, y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2

        if len(points) < 3:
            return 0

        tem_list = [{} for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                dis_tem = dis(points[i], points[j])
                if dis_tem not in tem_list[i]:
                    tem_list[i][dis_tem] = 1
                else:
                    tem_list[i][dis_tem] += 1
        print(tem_list)
        res = 0
        for each in tem_list:
            for each_key in each.keys():
                if each[each_key] > 1:
                    res += each[each_key]*(each[each_key]-1)
        return res








points =[[0,0],[1,0],[-1,0],[0,1],[0,-1]]

s = Solution()
print(s.numberOfBoomerangs(points))