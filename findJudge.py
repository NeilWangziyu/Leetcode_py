class Solution:
    def findJudge(self, N: 'int', trust: 'List[List[int]]') -> 'int':
        init_N = [True for _ in range(N)]
        init_trust = [set() for _ in range(N)]

        for each in trust:
            init_N[each[0]-1] = False
            init_trust[each[1]-1].add(each[0]-1)
        print(init_N, init_trust)
        for index, each in enumerate(init_N):
            if each == True:
                if len(init_trust[index]) == N-1:
                    return index+1
        return -1








N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

s = Solution()
print(s.findJudge(N, trust))