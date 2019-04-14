class Solution:
    def sumSubseqWidths(self, A):
        A.sort()
        res = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if i == j:
                    res += 0
                else:
                    delta = j - i - 1
                    res += (A[j]-A[i]) * (2**delta)
        return res % (10**9+7)


    def sumSubseqWidths2(self, A):
        mod =  (10**9+7)
        A.sort()
        res = 0
        power2 = [1]
        for i in range(1, len(A)):
            power2.append(power2[-1]*2 %  (10**9+7))

        for i, num in enumerate(A):
            res = (res + (power2[i] - power2[len(A) - 1 - i]) * num) % mod
        return res




s = Solution()
print(s.sumSubseqWidths(A=[2,1,3,4,5]))
print(s.sumSubseqWidths2(A=[2,1,3,4,5]))