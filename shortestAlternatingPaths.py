from typing import List

class Solution:
    def shortestAlternatingPaths0(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 超时，对球自循环处理不好
        def DFS(start, prev, count):
            # print(start, prev, count)
            if prev == "start":
                if start in res_hash:
                    start_rout_red = res_hash[start]
                    for each in start_rout_red:
                        if count + 1 < res_from_red[each]:
                            res_from_red[each] = count + 1


                        DFS(each, "red", count + 1)
                if start in blue_hash:
                    start_rout_blue = blue_hash[start]
                    for each in start_rout_blue:

                        if count + 1 < res_from_blue[each]:
                            res_from_blue[each] = count + 1

                        DFS(each, "blue", count + 1)

            elif prev == "blue":
                if check_ed_red[start] == True and count > res_from_red[start]+1:
                    return
                check_ed_red[start] = True

                if start in res_hash:
                    start_rout_red = res_hash[start]
                    for each in start_rout_red:
                        if count + 1 < res_from_red[each]:
                            res_from_red[each] = count + 1

                        DFS(each, "red", count+1)
            elif prev == "red":
                if check_ed_blue[start] == True and count > res_from_blue[start]+1:
                    return
                check_ed_blue[start] = True
                if start in blue_hash:
                    start_rout_blue = blue_hash[start]
                    for each in start_rout_blue:
                        if count + 1 < res_from_blue[each]:
                            res_from_blue[each] = count + 1
                        DFS(each, "blue", count+1)


            return


        if n == 0:
            return []
        if n == 1:
            return [0]

        res_hash = {}
        blue_hash ={}
        for each in red_edges:
            if each[0] not in res_hash:
                res_hash[each[0]] = [each[1]]
            else:
                res_hash[each[0]].append(each[1])

        for each in blue_edges:
            if each[0] not in blue_hash:
                blue_hash[each[0]] = [each[1]]
            else:
                blue_hash[each[0]].append(each[1])

        check_ed_red = [False for _ in range(n)]
        check_ed_blue = [False for _ in range(n)]


        res_from_red = [float("inf") for _ in range(n)]
        res_from_blue = [float("inf") for _ in range(n)]

        res_from_red[0] = 0
        res_from_blue[0] = 0

        DFS(0, "start", 0)
        res = [-1 for _ in range(n)]
        for i in range(n):
            if res_from_blue[i] == float("inf") and res_from_red[i] == float("inf"):
                continue
            else:
                res[i] = min(res_from_red[i], res_from_blue[i])
        # print(res)
        # print(check_ed_red, check_ed_blue)
        return res

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # others' result
        dis = [-1] * (n * 2)
        dis[0] = 0
        dis[n] = 0
        que = [0, n]
        blues = [[] for _ in range(n)]
        reds = [[] for _ in range(n)]
        for re in red_edges:
            reds[re[0]].append(re[1] + n)
        for bl in blue_edges:
            blues[bl[0]].append(bl[1])
        while len(que) > 0:
            u = que[0]
            que.pop(0)
            e = reds[u] if u < n else blues[u - n]
            for d in e:
                if dis[d] == -1:
                    dis[d] = dis[u] + 1
                    que.append(d)
        ans = [-1] * n
        for i in range(n):
            if dis[i] > -1:
                ans[i] = dis[i]
            if dis[i + n] > -1:
                ans[i] = dis[i + n] if ans[i] == -1 else min(dis[i + n], ans[i])
        return ans


if __name__ == "__main__":
    s = Solution()
    n = 3
    red_edges = [[0, 1]]
    blue_edges = [[2, 1]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 3
    red_edges = [[0, 1], [1, 2]]
    blue_edges = []
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 3
    red_edges = [[0, 1]]
    blue_edges = [[1, 2]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 3
    red_edges = [[0,1],[0,2]]
    blue_edges = [[1,0]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))


    n = 5
    red_edges = [[0,1],[1,2],[2,3],[3,4]]
    blue_edges = [[1,2],[2,3],[3,1]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 5
    red_edges = [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
    blue_edges = [[1,3],[0,0],[0,3],[4,2],[1,0]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
    # [0, 1, 2, 1, 1]

    n = 3
    red_edges = [[1, 0]]
    blue_edges = [[2, 1]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    print("---------------------")
    n = 6
    red_edges = [[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]]
    blue_edges = [[5,5],[5,0],[4,4],[0,3],[1,0]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
    # [0,-1,4,1,-1,2]



    n = 9
    red_edges = [[8, 6], [2, 0], [8, 3], [5, 1], [1, 3], [5, 7], [6, 8], [6, 2]]

    blue_edges = [[0, 1], [0, 6], [1, 4], [2, 8], [8, 8], [3, 3], [3, 6], [3, 7], [2, 1], [4, 0], [8, 1], [2, 2], [1, 7], [0, 8],
     [6, 5], [7, 8], [5, 0], [6, 7], [5, 4]]
    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))

    n = 100
    red_edges =[[23, 30], [63, 11], [92, 53], [53, 51], [74, 47], [19, 13], [25, 67], [22, 62], [15, 57], [61, 7], [84, 11],
     [54, 1], [1, 67], [28, 12], [93, 3], [57, 78], [43, 17], [21, 12], [48, 30], [81, 19], [76, 11], [64, 61], [37, 3],
     [65, 54], [81, 73], [39, 4], [29, 64], [72, 59], [37, 49], [22, 19], [52, 66], [34, 85], [62, 29], [19, 68],
     [43, 74], [93, 50], [91, 22], [2, 69], [6, 9], [27, 44], [19, 41], [21, 99], [18, 96], [42, 26], [88, 38], [54, 2],
     [31, 60], [92, 1], [12, 49], [43, 58], [31, 37], [89, 83], [15, 42], [98, 15], [96, 26], [63, 20], [54, 47],
     [12, 94], [10, 7], [16, 6], [14, 17], [97, 6], [6, 28], [84, 33], [17, 83], [76, 0], [29, 14], [53, 24], [61, 41],
     [66, 10], [2, 37], [72, 81], [85, 47], [29, 36], [94, 24], [17, 42], [53, 80], [1, 38], [56, 49], [13, 96],
     [64, 9], [37, 31], [45, 31], [35, 12], [91, 80], [0, 39], [38, 41], [34, 18], [36, 8], [12, 86], [9, 83], [17, 18],
     [31, 16], [64, 81], [17, 17], [65, 75], [32, 93], [40, 6], [8, 28], [57, 84], [24, 87], [33, 75], [86, 38],
     [34, 33], [79, 40], [60, 35], [99, 79], [72, 9]]
    blue_edges = [[5, 78], [33, 51], [92, 13], [32, 15], [73, 8], [40, 41], [71, 16], [86, 47], [33, 94], [57, 44], [68, 9],
     [89, 52], [13, 97], [40, 15], [61, 79], [51, 2], [77, 86], [66, 24], [54, 12], [42, 92], [29, 44], [11, 55],
     [98, 35], [63, 59], [79, 95], [33, 90], [63, 85], [78, 10], [14, 7], [8, 36], [54, 41], [95, 74], [67, 72],
     [83, 87], [77, 81], [66, 43], [59, 58], [34, 19], [46, 34], [24, 3], [50, 0], [47, 83], [37, 87], [92, 92],
     [0, 94], [25, 2], [72, 97], [79, 24], [16, 15], [31, 33], [4, 46], [65, 63], [76, 18], [64, 89], [11, 85],
     [68, 62], [26, 91], [47, 75], [17, 43], [70, 22], [53, 98], [55, 39], [53, 48], [45, 51], [51, 24], [79, 50],
     [82, 73], [27, 26], [76, 11], [1, 50], [59, 63], [42, 78], [60, 35], [47, 51], [76, 72], [96, 35], [97, 12],
     [87, 6], [33, 40], [15, 35], [46, 37], [57, 59], [89, 48], [3, 27], [4, 61], [34, 40], [60, 61], [32, 43],
     [40, 12], [60, 23], [90, 64], [81, 75], [36, 61], [47, 73], [89, 29], [34, 78], [45, 74], [75, 13], [86, 76],
     [13, 93], [94, 56], [93, 91], [53, 19], [95, 6], [20, 12], [2, 45], [49, 33], [20, 78], [50, 56], [79, 14],
     [85, 32], [65, 45], [0, 48], [81, 82], [61, 87], [50, 15], [43, 70], [86, 38], [62, 2], [89, 97], [17, 14],
     [52, 2], [46, 87], [0, 16], [16, 54], [86, 5], [2, 69], [80, 77], [37, 3], [89, 59], [45, 32], [47, 17], [19, 29],
     [69, 81], [12, 28], [52, 73], [88, 1], [10, 92], [1, 80], [21, 57], [11, 74], [19, 25], [11, 15], [25, 29],
     [44, 88], [86, 13], [60, 22], [97, 55], [3, 95], [73, 51], [85, 56], [58, 97], [78, 16], [42, 84], [26, 98],
     [46, 10], [28, 18], [14, 12], [76, 26], [79, 12], [58, 40], [72, 89], [5, 81], [41, 65], [46, 28], [18, 25],
     [65, 5], [0, 85], [10, 65], [28, 56], [39, 49], [22, 17], [30, 26], [53, 6], [12, 12], [16, 16], [70, 52],
     [96, 55], [37, 10], [72, 15], [80, 84], [50, 60], [58, 1], [76, 74], [96, 45], [42, 77], [15, 22], [99, 19],
     [86, 48], [98, 11], [50, 4], [71, 44], [49, 10], [4, 31], [67, 52], [52, 94], [35, 75], [83, 63], [7, 7], [99, 38],
     [71, 67], [18, 84], [80, 46], [80, 15], [18, 86], [10, 75], [81, 93], [67, 31], [72, 69], [18, 24], [57, 42],
     [93, 8], [93, 58]]

    print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
    res = s.shortestAlternatingPaths(n, red_edges, blue_edges)
    if res != [0,6,10,3,11,9,2,10,15,8,9,6,7,8,5,7,1,3,4,7,6,-1,9,9,2,5,3,11,8,10,2,7,-1,6,-1,9,12,8,6,1,7,8,4,5,9,11,13,2,1,2,7,3,7,6,9,7,9,8,6,8,8,9,9,5,12,9,8,6,8,11,-1,-1,7,3,6,3,9,5,5,-1,7,8,9,3,5,1,5,5,13,13,7,11,5,9,1,11,10,7,7,-1]:
        print("wrong")
    else:
        print("true")