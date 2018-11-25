class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        # 这种方法容易超出内存范围， 无法处理[[0,2147483647,2147483647]]
        if not building:
            return None
        sky_line = [0 for _ in range(100000)]
        # print(sky_line)
        max_end = 0
        for each in building:
            start = each[0]
            end = each[1]
            height = each[2]
            if  max_end < end:
                max_end = end
            for i in range(start, end):
                if sky_line[i]<height:
                    sky_line[i] = height

        res = sky_line[:max_end+2]
        # print(res)
        first = 0
        res_list = []
        for index, height in enumerate(res):
            if height!=first:
                res_list.append([index, height])
                first = height
        print(res_list)



building = [[0,12,12], [34,56,12]]
s = Solution()
print(s.getSkyline(building))