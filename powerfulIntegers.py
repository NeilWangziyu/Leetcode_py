class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound == 0:
            return []

        import math
        results = []

        if x == y == 1:
            if bound >= 2:
                return [2]
            else:
                return []

        if x == 1:
            y_j = math.ceil(math.log(bound, y))
            for j in range(y_j):
                result = x + pow(y, j)
                if result <= bound:
                    if result not in results:
                        results.append(result)
            results.sort()

            return results

        if y == 1:
            x_i = math.ceil(math.log(bound, x))
            for i in range(x_i):
                result = y + pow(x, i)
                if result <= bound:
                    if result not in results:
                        results.append(result)
            results.sort()

            return results

        x_i = math.ceil(math.log(bound, x))
        y_j = math.ceil(math.log(bound, y))
        for i in range(x_i):
            for j in range(y_j):
                result = pow(x, i) + pow(y, j)
                if result <= bound:
                    if result not in results:
                        results.append(result)
        results.sort()

        return results



    def powerfulIntegers2(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # 超时
        res = set()
        for i in range(20):
            for j in range(20):
                if x**i + y ** j > bound:
                    break
                else:
                    res.add(x**i+y**j)
        return list(res)


s = Solution()
print(s.powerfulIntegers(x = 3, y = 5, bound = 15))

print(s.powerfulIntegers2(x = 3, y = 5, bound = 15))
