class Solution:
    check = set("")
    res = 0
    def numTilePossibilities(self, tiles: str) -> int:
        self.check = set("")
        self.res = 0
        from collections import Counter
        def calcul(str):
            strlist = list(str)
            counter = Counter(strlist)
            totol_num = len(strlist)
            if len(counter.keys()) == 1:
                # print(strlist, "1")
                return 1
            tem_total = 1
            for i in range(1, totol_num + 1):
                tem_total = tem_total * i
            # print(tem_total, totol_num, strlist)
            for each_key in counter.keys():
                tem_C = 1
                for i in range(1, counter[each_key] + 1):
                    tem_C = tem_C * i
                # print(counter[each_key], tem_C)
                tem_total /= tem_C
            # print(tem_total)
            return tem_total




        def DFS(depth,length,  tem):
            if depth > length:
                return
            else:
                for i in range(depth, length):
                    if "".join(sorted(tem + tiles[i])) not in self.check:
                        self.check.add(tem + tiles[i])
                        self.res += calcul(tem + tiles[i])
                    DFS(i+1, length, tem + tiles[i])

        tiles = "".join(sorted(tiles))
        DFS(0, len(tiles), "")
        print(self.check)
        return int(self.res)









s = Solution()
tiles = "AAB"
print(s.numTilePossibilities(tiles=tiles))

tiles = "AAABBC"
print(s.numTilePossibilities(tiles=tiles))

tiles = "CDC"
print(s.numTilePossibilities(tiles=tiles))


tiles = "DCC"
print(s.numTilePossibilities(tiles=tiles))