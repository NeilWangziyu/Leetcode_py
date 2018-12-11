class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(M) == 0:
            return M


        row = len(M)
        col = len(M[0])
        M_smooth = [[0 for _ in range(col)] for _ in range(row)]

        if row == 1 and col == 1:
            return M

        if row == 1:
            for j in range(col):
                if j == 0:
                    M_smooth[0][j] = (M[0][j] + M[0][j+1])// 2
                elif j == col - 1:
                    M_smooth[0][j] = (M[0][j] + M[0][j-1]) // 2
                else:
                    M_smooth[0][j] = (M[0][j] + M[0][j-1] + M[0][j+1]) // 3
            return M_smooth
        if col == 1:
            for i in range(row):
                if i == 0:
                    M_smooth[i][0] = (M[i][0]+ M[i+1][0]) // 2
                elif i == row - 1:
                    M_smooth[i][0] = (M[i][0] + M[i-1][0])// 2
                else:
                    M_smooth[i][0] = (M[i][0] + M[i-1][0] + M[i+1][0]) // 3
            return M_smooth


        for i in range(row):
            for j in range(col):
                if i == 0:
                    if j == 0:
                        M_smooth[i][j] = (M[i][j] + M[i+1][j] + M[i][j+1] + M[i+1][j+1])//4
                    elif j == col-1:
                        M_smooth[i][j] = (M[i][j] + M[i + 1][j] + M[i][j - 1] + M[i + 1][j - 1]) // 4
                    else:
                        M_smooth[i][j] = (M[i][j] + M[i + 1][j] + M[i][j-1] + M[i+1][j-1]+M[i][j+1] + M[i+1][j+1]) // 6
                elif i == row - 1:
                    if j == 0:
                        M_smooth[i][j] = (M[i][j] + M[i-1][j] + M[i][j+1] + M[i-1][j+1])//4
                    elif j == col-1:
                        M_smooth[i][j] = (M[i][j] + M[i - 1][j] + M[i][j - 1] + M[i - 1][j - 1]) // 4
                    else:
                        M_smooth[i][j] = (M[i][j] + M[i - 1][j] + M[i][j-1] + M[i-1][j-1]+M[i][j+1] + M[i-1][j+1]) // 6
                else:
                    if j == 0:
                        M_smooth[i][j] = (M[i][j] + M[i-1][j]+M[i][j+1]+M[i-1][j+1]+ M[i+1][j]+ M[i+1][j+1]) // 6
                        print(i,j,M_smooth[i][j])
                        print(M[i][j] ,M[i-1][j],M[i][j+1],M[i-1][j+1],M[i+1][j],M[i+1][j+1])

                    elif j == col - 1:
                        M_smooth[i][j] = (M[i][j] + M[i-1][j] + M[i][j-1] + M[i-1][j-1]+ M[i+1][j]+ M[i+1][j-1]) // 6
                    else:
                        M_smooth[i][j] = (M[i][j] + M[i-1][j] + M[i][j-1] + M[i-1][j-1]+M[i][j+1]+M[i-1][j+1]+ M[i+1][j]+ M[i+1][j-1]+ M[i+1][j+1]) // 9
        return M_smooth

M = [[2,3,4],
     [5,6,7],
     [8,9,10],
     [11,12,13],
     [14,15,16]]

s = Solution()
print(s.imageSmoother(M))