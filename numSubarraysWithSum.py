class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        超时
        若干 0 和 1  组成， that information should be used
        """
        if not A:
            return 0
        count = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if i == j:
                    if A[i] == S:
                        count += 1
                    init = A[i]
                else:
                    init = init + A[j]
                    if init == S:
                        count += 1
        return count

    def numSubarraysWithSum2(self, A, S):
        COUNT_list = [0 for _ in range(len(A)+1)]
        n = 0
        for i in range(len(A)):
            if A[i] == 0:
                COUNT_list[n] += 1
            else:
                n += 1
        n += 1
        print(COUNT_list, n)
        res = 0
        i = 0
        # n:表示最大能有几个1， n == 6：表示最多到达5
        while(i+S < n):
            if S == 0:
                res += (COUNT_list[i] + 1) * COUNT_list[i] / 2
            else:
                res += (COUNT_list[i] + 1) * (COUNT_list[i + S] + 1)
            i += 1

        return res

    def numSubarraysWithSum3(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        longA = len(A)  # 原数组长度
        l = [-1]  # 列表 l 用来储存 1 的位置，假设 A[-1] 为 1
        count = 0

        if not longA:
            return 0

        for i in range(longA):
            if A[i] == 1:
                l.append(i)  # 找出 1 的下标

        l.append(longA)  # 假设 A[longA] 为1
        longL = len(l)

        if not S:  # 如果 S == 0
            i = 0
            while i + 1 < longL:
                x = l[i + 1] - l[i] - 1  # 区间内 0 的个数
                count += (1 + x) * x / 2  # 此区间 sum == 0 的子序列数
                i += 1
        else:
            a = 0
            b = S
            while b < longL - 1:
                count += (l[a + 1] - l[a]) * (l[b + 1] - l[b])
                b += 1
                a += 1

        return int(count)


A = [1,0,1,0,0,1,0,0,0,1,0,1]
S = 3
s = Solution()
print(s.numSubarraysWithSum(A, S))
print(s.numSubarraysWithSum2(A, S))