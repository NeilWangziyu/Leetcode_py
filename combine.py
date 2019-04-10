class Solution:
    def combine(self, n: int, k: int):
        res = []
        if k > n:
            return []
        if k == n:
            return [[i+1 for i in range(n)]]

        res = []
        # numbers = [i+1 for i in range(n)]

        def DFS(index, num_left, res_list):
            if num_left == 0:
                res.append(res_list)
                return

            if index > n:
                return

            else:

                for check in range(index+1, n+1):
                    DFS(check, num_left-1, res_list+[check])

        DFS(0, k, [])
        return res

    def combine2(self, n, k):
        from itertools import combinations
        com_list = []
        for i in range(n + 1):
            if i == 0:
                continue
            com_list += [i]
        return list(combinations(com_list, k))


    def combine3(self, n: int, k: int):
        # C(m,n)=C(m-1,n)+C(m-1,n-1)
        ans = []

        if n < k:
            return []

        if k == 0:
            return [[]]

        if k == 1:
            return [[i] for i in range(1, n + 1)]

        if k == n:
            return [[i for i in range(1, n + 1)]]

        ans = self.combine(n - 1, k)
        for i in self.combine(n - 1, k - 1):
            i.append(n)
            ans.append(i)
        return ans


n = 4
k = 2
s = Solution()
print(s.combine(n, k))