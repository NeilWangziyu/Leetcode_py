class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        def find_in_A(A, each):
            if len(A) == 1:
                return 0
            if len(A) == 2:
                return 1
            else:
                first = 0
                last = len(A) - 1
                mid = (first+last)//2
                while(first<last):
                    if A[mid] <= each:
                        first = mid + 1
                    else:
                        last = mid
                    mid = (first + last) // 2
            return mid

        B_dict = {}
        for index, num in enumerate(B):
            B_dict[index] = num
        A.sort()
        B.sort()

        print(A,B)
        B_match = {}
        for each in B:
            if each >= A[-1] or each < A[0]:
                if each not in B_match:
                    B_match[each] = [A[0]]
                    A.pop(0)
                else:
                    B_match[each].append(A[0])
                    A.pop(0)
            else:
#                 利用二分法查找大于其的最小值
                i = find_in_A(A, each)
                if each not in B_match:
                    B_match[each] = [A[i]]
                    A.pop(i)
                else:
                    B_match[each].append(A[i])
                    A.pop(i)

        print(B_match)
        res = []
        for index in range(len(B)):
            res.append(B_match[B_dict[index]].pop(0))
        return res

    def advantageCount2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        import bisect
        A.sort()
        ans = []

        for bn in B:
            p = bisect.bisect(A, bn)
            if p >= len(A):
                ans.append(A.pop(0))
            else:
                ans.append(A.pop(p))

        return ans


A = [2,0,4,1,2]
B = [1,3,0,0,2]
s = Solution()
print(s.advantageCount2(A, B))