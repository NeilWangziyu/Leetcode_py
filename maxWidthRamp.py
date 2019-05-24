class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        if len(A) < 2:
            return 0
        res = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] <= A[j]:
                    res = max(res, j-i)
        return res


    def maxWidthRamp2(self, A):
        if not A:
            return 0
        if len(A) < 2:
            return 0

        A_list = sorted(range(len(A)), key=lambda x:A[x])
        last = len(A)
        res = 0
        for each in A_list:
            if each < last:
                last = each
            else:
                res = max(res, each - last)

        return res

    def maxWidthRamp3(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        re = 0
        stack = []

        for i in range(len(A)):
            if len(stack) == 0 or A[stack[-1]] > A[i]:  # 防止下标越界，不用A[i]>A[i+1}
                print(A[i])
                stack.append(i)  # stack中存放下标 ，按值升序


        print(stack)

        for j in range(len(A) - 1, re - 1, -1):  # 最大堆的左端肯定在单调栈内
            print(j, stack)
            while stack and A[stack[-1]] <= A[j]:
                k = j - stack.pop()  # 对于栈顶元素来说不可能有更大值， 因此pop出
                re = max(re, k)  # 找到每个单调递增堆中元素的最大宽度坡，max即为整个数组最终结果
        return re


s = Solution()
A = [6,0,8,2,1,5]
# print(s.maxWidthRamp2(A))
print(s.maxWidthRamp3(A))

A = [9,8,1,0,1,9,4,0,4,1]
# print(s.maxWidthRamp2(A))
print(s.maxWidthRamp3(A))
