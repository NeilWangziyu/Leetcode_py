def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # 水平方向
    h_list = []
    for each in grid:
        h_list.append(max(each))
    print(h_list)
    v_list = []
    for i in range(len(grid[0])):
        colum_list = []
        for j in range(len(grid)):
            # print(grid[j][i])
            colum_list.append(grid[j][i])
        v_list.append(max(colum_list))
    print(v_list)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += (min(h_list[i], v_list[j])-grid[i][j])
    print(total)
    return total




grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

maxIncreaseKeepingSkyline(grid)




