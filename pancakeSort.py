class Solution:
    def pancakeSort(self, A):
        def pancakeSortCore(arr):
            if not arr:
                return arr
            if len(arr) == 1:
                return arr

            largest = -float('inf')
            largest_index = -1

            for index, num in enumerate(arr):
                if num > largest:
                    largest = num
                    largest_index = index
            print(largest_index, "largest")
            if largest_index == 0:
                res.append(len(arr))
                arr = arr[::-1]
                pancakeSortCore(arr[:-1])
            elif largest_index == len(arr):
                pancakeSortCore(arr[:-1])
            else:
                res.append(largest_index+1)
                arr[:largest_index+1] = arr[:largest_index+1][::-1]
                res.append(len(arr))
                arr = arr[::-1]
                pancakeSortCore(arr[:-1])


        if not A:
            return A
        if len(A) == 1:
            return A
        res = []
        pancakeSortCore(A)
        return res

# ----
    def flip(self, A, k):
        A[0:k] = A[0:k][::-1]

        return A

    def pancakeSort2(self, A):
        M = max(A)
        res = []
        while A:
            if A[0] != M:
                res.append(A.index(M)+1)
                A = self.flip(A, res[-1])
            res.append(A[0])
            A = self.flip(A, res[-1])
            del A[-1]
            M -= 1

        return res[0:-1]



# A = [93,19,91,20,82,12,18,5,57,14,37,36,32,99,100,33,22,58,83,75,49,70,60,63,15,31,88,21,35,66,89,64,69,95,50,41,52,30,56,47,1,17,77,13,26,39,53,98,81,48,8,46,45,3,55,84,51,24,42,34,25,38,96,71,27,80,85,40,28,6,59,86,65,73,29,10,94,61,2,4,7,90,43,54,87,23,97,9,62,44,68,78,72,11,74,79,67,76,92,16]
A = [5,3,2,4,1]
s = Solution()
print(s.pancakeSort(A))



