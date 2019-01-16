class Solution:
    count = 0
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if  N <= 2:
            return N

        list_check = list(range(1, N + 1))
        res = []

        def check_list(list_input):
            for i in range(len(list_input)):
                if (i+1) % list_input[i] != 0  and list_input[i] % (i+1) != 0:
                    return False
            return True


        def DFS(left_n, depth, tem_list):
            if depth == N:
                if check_list(tem_list):
                    res.append(tem_list)
            else:
                for i in range(len(left_n)):
                    DFS(left_n[:i] + left_n[i + 1:], depth + 1, tem_list + [left_n[i]])

        DFS(list_check, 0, [])
        print(res)
        return len(res)



    def countArrangement2(self, N):
        if  N <= 2:
            return N

        def DFS(start, N, L):
            if start == N+1:
                self.count += 1
                return
            for i in range(1, N+1):
                if i in L:
                    continue
                if start % i == 0 or i % start == 0:
                    DFS(start+1, N, L+[i])

        DFS(1, N, [])
        return self.count

N = 9

s = Solution()
print(s.countArrangement(N))
print(s.countArrangement2(N))
