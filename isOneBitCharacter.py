class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return True
        if len(bits) < 2:
            return True
        length = len(bits)
        i = length - 2
        count = 0
        while (i >= 0):
            if bits[i] != 1:
                break
            else:
                i -= 1
                count += 1
        if count % 2 == 1:
            return False
        else:
            return True

