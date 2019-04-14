class Solution:
    def divisorGame(self, N: int) -> bool:
        if N % 2 == 0:
            return True
        else:
            return False
        


if __name__ == "__main__":
    s =Solution()
    print(s.divisorGame(N=10))