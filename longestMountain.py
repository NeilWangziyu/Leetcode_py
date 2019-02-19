class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        i = 0
        while(i+1<len(A) and A[i+1]<=A[i]):
            i += 1
        if i + 1 == len(A):
            return 0
        j = i + 1
        longest = 0
        print("init",i, j)
        while(True):
            init = A[i]
            while(j < len(A) and A[j] > init):
                init = A[j]
                j += 1

            if j >= len(A):
                break

            left_part = j - i
            print(i, j)

            i = j
            init = A[i-1]
            while(j < len(A) and A[j] < init):
                init = A[j]
                j += 1

            right_part = j - i
            print(i, j)


            if left_part and right_part:
                if left_part + right_part > longest:
                    longest = left_part + right_part


            if j >= len(A):
                break

            if j != i:
                i = j - 1
            else:
                while (i + 1 < len(A) and A[i + 1] <= A[i]):
                    i += 1
                if i + 1 == len(A):
                    break
                j = i + 1

        return longest

    def longestMountain2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        res = 0
        end = 1
        while end < len(A):
            # 负责找到上山的那条路
            while end < len(A) and A[end] <= A[end - 1]:
                end += 1
            # 找不到则返回
            if end >= len(A):
                return res
            tmp = 1
            while end < len(A) and A[end] > A[end - 1]:
                tmp += 1
                end += 1
            # 一直在上山，直到结束，则直接返回
            if end >= len(A):
                return res
            else:
                flag = False
                while end < len(A) and A[end] < A[end - 1]:
                    tmp += 1
                    flag = True
                    end += 1
                # 用来判断是否有下山的那部分
                if flag:
                    res = max(res, tmp)

        return res


A = [875,884,239,731,723,685]
s = Solution()
print(s.longestMountain(A))
print(s.longestMountain2(A))
