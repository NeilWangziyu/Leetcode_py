class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(res, left_num, right_num, string_to_add):
            print(left_num, right_num, string_to_add)
            if left_num == n and right_num == n:
                res.append(string_to_add)
                return

            if left_num < n:
                dfs(res, left_num+1, right_num, string_to_add+'(')


            if left_num > right_num:
                dfs(res, left_num, right_num+1, string_to_add+')')

        res = []
        dfs(res, 0, 0, '')
        return res



s = Solution()
print(s.generateParenthesis(3))

