class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        lenth_t = len(A)
        t = A
        while(lenth_t < len(B) + len(A)):
            t = t + A
            lenth_t += len(A)
        for i in range(lenth_t):
            if t[i:i+len(B)] == B:
                print(t[i:i+len(B)])
                return math.floor((i+len(B)-1)/len(A)) + 1

        return -1



A = "abcd"
B = "abcdabcd"
s = Solution()
print(s.repeatedStringMatch(A, B))