class Solution:
    def longestOnes(self, A, K: int):
        if not A:
            return 0
        if all(A):
            return len(A)

        max = 0
        s = 0
        e = 0
        while(e < len(A)):
            if A[e] == 0:
                K -= 1
            while (K < 0):
                s += 1
                if A[s-1] == 0:
                    K += 1
            if max < e - s + 1:
                max = e - s + 1
            e += 1
        return max




A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
s = Solution()
print(s.longestOnes(A, K))
