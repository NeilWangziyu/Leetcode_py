class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        if len(A) == 1:
            return 0

        res = 0
        length_row = len(A[0])
        for i in range(length_row):
            init = 'a'
            for each in A:
                print(each[i])
                if each[i] < init:
                    print("wrong")
                    res += 1
                    break
                init = each[i]
        return res







A = ["cba", "daf", "ghi"]
s = Solution()
print(s.minDeletionSize(A))
