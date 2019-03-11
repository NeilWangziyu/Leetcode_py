class Solution:
    def leastBricks(self, wall) -> int:
        "超时"
        if not wall:
            return 0
        dict_high = {}
        for each_layer in wall:
            start = 0
            for each_block in each_layer:
                for i in range(start + 1, start + each_block):
                    if i not in dict_high:
                        dict_high[i] = 1
                    else:
                        dict_high[i] += 1
                start = start + each_block
        if not dict_high:
            return len(wall)
        res = 10000
        for each in dict_high.keys():
            if res > dict_high[each]:
                res = dict_high[each]
        return res

    def leastBricks2(self, wall) -> int:
        if not wall:
            return 0
        dict_high = {}
        for each_layer in wall:
            start = 0
            for each_block in each_layer:
                # if start not in dict_high:
                #     dict_high[start+1] = 1
                # else:
                #     dict_high[start + 1] += 1

                if start + each_block not in dict_high:
                    dict_high[start + each_block] = 1
                else:
                    dict_high[start + each_block] += 1

                start = start + each_block
        if not dict_high:
            return len(wall)
        res = 0
        check_keys = list(dict_high.keys())
        check_keys.pop(check_keys.index(max(check_keys)))
        for each in check_keys:
            if res < dict_high[each]:
                res = dict_high[each]

        return len(wall) - res


if __name__ == "__main__":
    s = Solution()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(s.leastBricks2(wall))