class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        做的不好，其实应该可以少循环一次的
        """
        res = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        check_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    check_list.append([i,j])
        check_times = 0
        print(res)
        while(check_list):
            next_list = []
            for each in check_list:
                res[each[0]][each[1]] = check_times

            for each in check_list:
                if each[0] > 0:
                    if res[each[0]-1][each[1]] == -1:
                        next_list.append([each[0]-1,each[1]])
                if each[0] < len(matrix) - 1:
                    if res[each[0]+1][each[1]] == -1:
                        next_list.append([each[0]+1,each[1]])

                if each[1] > 0:
                    if res[each[0]][each[1]-1] == -1:
                        next_list.append([each[0],each[1]-1])

                if each[1] < len(matrix[0]) - 1:
                    if res[each[0]][each[1]+1] == -1:
                        next_list.append([each[0],each[1] + 1])

            check_times += 1
            check_list  = next_list
        return res




matrix = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]


s = Solution()
print(s.updateMatrix(matrix))