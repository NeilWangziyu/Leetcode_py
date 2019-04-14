class Solution(object):
    def ShortestWaytoFormStr(self, source, target):
        def source_all_substring(source):
            res = []
            def bfs(depth, start, res_list):
                # 深度优先搜索
                res.append(res_list)
                if depth == len(source):
                    return
                else:
                    for i in range(start, len(source)):
                        bfs(depth + 1, i + 1, res_list + [source[i]])
            bfs(0, 0, [])
            res_hash = set()
            for each in res:
                res_hash.add("".join(each))
            return res_hash


        res_has = source_all_substring(source)
        i = 0
        j = 0
        count = 0
        while(j < len(target)):
            while(target[i:j+1] in res_has and j < len(target)):
                j += 1
            count += 1
            i = j
            j = j
            if target[i:j+1] not in res_has:
                return -1
        return count




if __name__ == "__main__":
    source = "abc"
    target = "abcbc"
    s = Solution()
    print(s.ShortestWaytoFormStr(source, target))
    source = "abc"
    target = "acdbc"
    print(s.ShortestWaytoFormStr(source, target))
    source = "xyz"
    target = "xzyxz"
    print(s.ShortestWaytoFormStr(source, target))

