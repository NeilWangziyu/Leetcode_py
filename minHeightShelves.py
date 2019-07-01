class Solution:
    # def minHeightShelves(self, books, shelf_width) -> int:
    #     # 摆放书的顺序与你整理好的顺序相同
    #     if not books:
    #         return 0
    #
    #     number = len(books)
    #
    #     sum_or_length = 0
    #     for each in books:
    #         sum_or_length += each[0]
    #     print(sum_or_length)

    def minHeightShelves(self, books, shelf_width: int) -> int:
        # code from others

        dp = [0] * (len(books) + 1)
        for i in range(len(books) - 1, -1, -1):
            sums = 0
            height = 0
            res = 0x3fffffff
            for j in range(i, len(books)):
                if sums + books[j][0] <= shelf_width:
                    sums += books[j][0]
                    height = max(height, books[j][1])
                    res = min(height + dp[j + 1], res)
                else:
                    break
            dp[i] = res
        return dp[0]




s = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(s.minHeightShelves(books, shelf_width))