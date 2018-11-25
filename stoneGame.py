def stoneGame(piles):
    """
    :type piles: List[int]
    :rtype: bool
    """
    N = len(piles)

    def dp(i,j):
        if i > j : return 0
        which_one = (N-(j-i)) % 2
        if which_one == 1:
#             first
            return max(piles[i]+dp(i+1,j), piles[j]+dp(i,j-1))
        else:
#             second
            return min(-piles[i]+dp(i+1,j), -piles[j]+dp(i,j-1))


    return dp(0,N-1)>0

print(stoneGame([5,3,4,5]))