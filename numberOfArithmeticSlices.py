class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        continue list, so just focus on continues 3 data
        """
        if not A:
            return 0
        if len(A) <= 2:
            return 0

        dp = 0
        sum = 0
        delta = A[1] - A[0]
        for i in range(2, len(A)):
            delta2 = A[i] - A[i-1]
            if delta == delta2:
                dp += 1
                sum += dp
            else:
                dp = 0
            delta = delta2
        return sum

    def numberOfArithmeticSlices2(self, A) -> int:
        if not A or len(A) < 3:
            return 0
        difs = []
        for i in range(1, len(A)):
            difs.append(A[i] - A[i - 1])

        def find_ari(begin):
            if begin == len(difs):
                return 0
            end = begin + 1
            while end < len(difs) and difs[begin] == difs[end]:
                end += 1
            return (end - begin) * (end - begin - 1) / 2 + find_ari(end)

        return int(find_ari(0))


A = [1,2,3,8,9,10]

s = Solution()
print(s.numberOfArithmeticSlices(A))