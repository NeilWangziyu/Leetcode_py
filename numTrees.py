class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        list = [0 for _ in range(n + 1)]
        list[0] = 1
        list[1] = 1
        list[2] = 2
        list[3] = 5

        for i in range(4, n+1):
            tem = 0
            for t in range(0, i):
                tem += list[t]*list[i-1-t]
            list[i] = tem


        print(list)
        return list[-1]

s = Solution()
print(s.numTrees(5))