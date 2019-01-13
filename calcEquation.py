class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        # 利用图来解决该问题
        """








equations = [ ["a","b"],["b","c"] ]
values = [2.0,3.0]
queries = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]

s = Solution()
print(s.calcEquation(equations, values, queries))