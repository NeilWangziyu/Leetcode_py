class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def DFS(index, count):
            for each_person in range(len(M[index])):
                if M[index][each_person] == 1:
                    if each_person != index and Stu_num[each_person] == False:
                        Stu_num[each_person] = count
                        DFS(each_person, count)

        if not M:
            return 0

        if len(M)== 1:
            return 1

        count = 1
        Stu_num = [False for _ in range(len(M))]
        for i in range(len(M)):
            if Stu_num[i] == False:
                DFS(i, count)
                count += 1
        return count - 1





M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

s = Solution()
print(s.findCircleNum(M))