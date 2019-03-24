class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        if not A:
            return False
        if len(A) < 3:
            return False
        if sum(A) % 3 != 0:
            return False

        subSum = sum(A) // 3
        low = 0
        high = len(A) - 1
        front = A[low]
        back = A[high]

        while (low < high):
            if front == back == subSum:
                return True

            if front < subSum:
                low += 1
                front += A[low]
            elif back < subSum:
                high -= 1
                back += A[high]
            else:
                if front == subSum:
                    high -= 1
                    back += A[high]
                else:
                    low += 1
                    front += A[low]
        return False

A = [0,2,1,-6,6,7,9,-1,2,0,1]
s = Solution()
print(s.canThreePartsEqualSum(A))