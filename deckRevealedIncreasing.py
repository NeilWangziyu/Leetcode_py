class Solution:
    def deckRevealedIncreasing(self, deck):
        if not deck:
            return []
        if len(deck) == 1:
            return deck
        deck.sort()
        length = len(deck)
        res = [-1 for _ in range(length)]
        check_list = list(range(length))
        i = 0
        while(check_list):
            check = check_list.pop(0)
            res[check] = deck[i]
            i += 1
            if check_list:
                check_list.append(check_list.pop(0))
        return res



deck = [17,13,11,2,3,5,7]
s = Solution()
print(s.deckRevealedIncreasing(deck))