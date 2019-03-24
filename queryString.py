class Solution:
    def queryString(self, S: str, N: int) -> bool:
        if not S:
            return False
        for i in range(N+1):
            str = bin(i)
            if str[2:] not in S:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    S = "0110"
    N = 3
    print(s.queryString(S, N))