class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        continue_empyt = 1
        count = 0
        for each in flowerbed:
            if each == 1:
                if continue_empyt > 2:
                    count += (continue_empyt-1) // 2
                continue_empyt = 0
            else:
                continue_empyt += 1
        if continue_empyt >= 2:
            count += (continue_empyt) // 2
        if count >= n:
            return True
        return False

    def canPlaceFlowers2(self, flowerbed, n: int) -> bool:
        flowerbed = [1, 0] + flowerbed + [0, 1]

        cnt, cnt_range = 0, 0
        for i in flowerbed:
            if cnt >= n:
                break

            if i == 0:
                cnt_range += 1
            else:
                if cnt_range > 0:
                    cnt += (cnt_range - 1) // 2
                    cnt_range = 0

        return cnt >= n


flowerbed = [1,0,1,0,0]
n = 1
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))