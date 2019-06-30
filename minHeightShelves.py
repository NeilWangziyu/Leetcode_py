class Solution:
    def minHeightShelves(self, books, shelf_width) -> int:
        # 摆放书的顺序与你整理好的顺序相同
        if not books:
            return 0

        number = len(books)

        sum_or_length = 0
        for each in books:
            sum_or_length += each[0]
        print(sum_or_length)





s = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(s.minHeightShelves(books, shelf_width))