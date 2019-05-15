class Solution:
    sum_of_all = 0

    def sumSubarrayMins(self, A) -> int:
        # 连续子数组！！！
        if not A:
            return 0
        if len(A) == 1:
            return min(A)


        def DFS(start, depth, tem_list):
            if tem_list:
                # print(tem_list)
                self.sum_of_all += tem_list
            if depth == len(A):
                return
            else:
                if not tem_list:
                    for i in range(start, len(A)):
                        DFS(i+1, depth+1, A[i])
                else:
                    if start < len(A):
                        if A[start]>tem_list:
                            DFS(start + 1, depth + 1, tem_list)
                        else:
                            DFS(start + 1, depth + 1, A[start])

        DFS(0, 0, None)
        # print(self.sum_of_all)
        return self.sum_of_all % (10**9+7)



    def sumSubarrayMins2(self, A) -> int:
        # 维护一个单调递增栈
        if (len(A) == 0):
            return 0
        stack = []
        sum = 0
        A.insert(0, 0)
        A.append(0)
        for i in range(len(A)):
            print(stack)
            while stack and A[i] < A[stack[-1]]:
                out = stack.pop(-1)
                sum += (out - stack[-1]) * (i - out) * A[out]
            stack.append(i)
        return sum % (pow(10, 9) + 7)

    def sumSubarrayMins3(self, A) -> int:
        A = [0] + A
        # result[i]是所有以A[i]为结束的子序列的结果
        # 比如 result[2] = min([3,1,2])+min([1,2])+min([2])
        result = [0] * len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop()
                # A[j]是序列中第一个小于A[i]的值
            # 在不包含A[j]的子序列A[j+1:i+1]，A[j+2:i+1]...中，最小值为A[i]
            # 因此 result[i] = result[j] + (i-j)*A[i]
            j = stack[-1]
            result[i] = result[j] + (i - j) * A[i]
            stack.append(i)
        return sum(result) % (10 ** 9 + 7)






A = [3,1,2,4]
s = Solution()
print(s.sumSubarrayMins(A))

print(s.sumSubarrayMins2(A))
print(s.sumSubarrayMins3(A))

