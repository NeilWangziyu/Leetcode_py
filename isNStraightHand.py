class Solution:
    def isNStraightHand(self, hand, W: int) -> bool:
        if not hand:
            return False
        if len(hand) % W != 0:
            return False
        from collections import Counter
        c = Counter(hand)
        keys = list(c.keys())
        keys.sort()
        for each in keys:
            num = c[each]
            if num == 0:
                continue
            else:
                for index in range(W):
                    if c[each + index] < num:
                        return False
                for index in range(W):
                    c[each + index] -= num
        return True


if __name__ == "__main__":
    pass