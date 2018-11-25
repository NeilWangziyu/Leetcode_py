class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def dfs(init, total):
            res.append(init)
            if init * 10 <= total:
                dfs(init * 10, total)
            if init + 1 <= total and (init+1)%10!=0:

                dfs(init + 1, total)

        if n < 0:
            return list(range(1, n + 1))
        else:
            res = []
            dfs(1, n)

            return res

s = Solution()
print(s.lexicalOrder(100))

