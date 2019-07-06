class Solution:
    def largestTimeFromDigits(self, A):
        A.sort(reverse=True)
        res = ""
        orig = A.copy()
        if 2 in A:
            res += '2'
            A.pop(A.index(2))

            for i in range(3, -1, -1):
                if i in A:
                    res+=str(i)
                    res+=':'
                    A.pop(A.index(i))
                    tem = A[0]*10 + A[1]
                    if tem >= 0 and tem < 60:
                        res += str(A[0])
                        res += str(A[1])
                        return res
                    else:
                        tem = A[1] * 10 + A[0]
                        if tem >= 0 and tem < 60:
                            res += str(A[1])
                            res += str(A[0])
                            return res
                        else:
                            pass


        A = orig.copy()
        res = ""
        if 1 in A:
            res += '1'
            A.pop(A.index(1))
            next = max(A)
            A.pop(A.index(next))
            res += str(next)
            res += ":"
            tem = A[0] * 10 + A[1]
            if tem >= 0 and tem < 60:
                res += str(A[0])
                res += str(A[1])
                return res
            else:
                tem = A[1] * 10 + A[0]
                if tem >= 0 and tem < 60:
                    res += str(A[1])
                    res += str(A[0])
                    return res
                else:
                    pass

        A = orig.copy()
        res = ""
        if 0 in A:
            res += '0'
            A.pop(A.index(0))
            next = max(A)
            A.pop(A.index(next))
            res += str(next)
            res += ":"
            tem = A[0] * 10 + A[1]
            if tem >= 0 and tem < 60:
                res += str(A[0])
                res += str(A[1])
            else:
                tem = A[1] * 10 + A[0]
                if tem >= 0 and tem < 60:
                    res += str(A[1])
                    res += str(A[0])
                else:
                    return ""
            return res

        else:
            return ""

if __name__ == "__main__":
    A = [2,0,6,6]
    s = Solution()
    print(s.largestTimeFromDigits(A))