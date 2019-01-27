class Solution:
    res = None
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == 0 and B == 0:
            return ""

        def DFE(a_n, b_n, str):
            if self.res == None:
                if a_n == A and b_n == B:
                    # print(str)
                    if self.res == None:
                        self.res = str
                    return
                if a_n > A or b_n > B:
                    return
                if len(str)< 2:
                    DFE(a_n+1, b_n, str+'a')
                    DFE(a_n , b_n+1, str + 'b')
                    return
                else:
                    if str[-1] == str[-2]:
                        if str[-2] == 'a':
                            DFE(a_n, b_n + 1, str + 'b')
                        else:
                            DFE(a_n + 1, b_n, str + 'a')
                    else:

                        if a_n == A:
                            DFE(a_n, b_n + 1, str + 'b')
                            return
                        elif b_n == B:
                            DFE(a_n + 1, b_n, str + 'a')
                            return
                        else:
                            DFE(a_n, b_n + 1, str + 'b')
                            DFE(a_n + 1, b_n, str + 'a')
                            return

        self.res = None
        DFE(0, 0, "")
        return self.res

    def strWithout3a3b2(self, A, B):
        """
        实际上还是分情况进行讨论，强行取到最大值
        :param A:
        :param B:
        :return:
        """
        if A < B:
            n = (B - 1) // 2
            ans = ''
            for i in range(n):
                ans += 'bb'
                if i < A - n:
                    ans += 'aa'
                else:
                    ans += 'a'
            ans += 'b' * (B - n * 2)
            a = ans.count('a')
            ans += 'a' * (max(0, A - a))
            return ans
        else:
            n = (A - 1) // 2
            ans = ''
            for i in range(n):
                ans += 'aa'
                if i < B - n:
                    ans += 'bb'
                else:
                    ans += 'b'
            ans += 'a' * (A - n * 2)
            b = ans.count('b')
            ans += 'b' * (max(0, B - b))
            return ans


A = 98
B = 89
s = Solution()
print(s.strWithout3a3b2(A, B))