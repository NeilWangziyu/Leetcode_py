class Solution:
    res = []
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n <= 2:
            return list(range(1, n + 1))
        list_check = list(range(1, n + 1))

        def check_set(list_input):
            new_list = [abs(list_input[i] - list_input[i - 1]) for i in range(1, len(list_input))]
            return len(set(new_list))

        def DFS(left_n, depth, tem_list):
            if self.res != []:
                return
            if depth == n:
                if check_set(tem_list) == k:
                    self.res = tem_list
            else:
                for i in range(len(left_n)):
                    DFS(left_n[:i] + left_n[i + 1:], depth + 1, tem_list + [left_n[i]])

        DFS(list_check, 0, [])
        return self.res


    def constructArray2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [1, k + 1]
        for i in range(k - 1):
            if i & 1:
                res.append(res[-2] - 1)
            else:
                res.append(res[-2] + 1)
        res += [i for i in range(k + 2, n + 1)]
        return res


n = 92
k = 80
s = Solution()
print(s.constructArray(n, k))