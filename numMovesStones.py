class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        sorted_list = sorted([a, b, c])
        a = sorted_list[0]
        b = sorted_list[1]
        c = sorted_list[2]
        max_num = c - a - 2
        if c - b > 2 and b - a > 2:
            min_num = 2
        elif c - a == 2:
            min_num = 0
        else:
            min_num = 1

        return [min_num, max_num]




s = Solution()
a = 1
b = 4
c = 5
print(s.numMovesStones(a,b,c))

