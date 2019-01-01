class Solution:
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0


    def lenLongestFibSubseq2(self, A):
        import collections
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0

    def lenLongestFibSubseq3(self, A):
        """
        :type A: List[int]
        :rtype: int
        这个想法就特别好，check num1 + num2， 而不是去做减法，能够简单很多很多！！
        """
        max_sub = 0
        max_num = A[-1]
        set_A = set(A)
        length = len(A)
        for i in range(length):
            for j in range(i + 1, length):
                num1, num2 = A[i], A[j]
                num3 = num1 + num2
                if num3 > max_num:
                    break
                sub_len = 2
                while (num3 in set_A):
                    num1, num2 = num2, num3
                    num3 = num1 + num2
                    sub_len += 1
                    max_sub = max(max_sub, sub_len)
                    if (max_sub == length):
                        return length
        return max_sub


t = [1,3,7,11,12,14,18]

s = Solution()
print(s.lenLongestFibSubseq3(t))