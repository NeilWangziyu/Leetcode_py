class Solution:
    def corpFlightBookings0(self, bookings, n: int):
        # 超时
        hash_set = {}
        for i in range(1, n+1):
            hash_set[i] = 0

        for each in bookings:
            for index in range(each[0], each[1]+1):
                hash_set[index] += each[2]

        res = []
        for i in range(1, n+1):
            res.append(hash_set[i])
        return res

    def corpFlightBookings(self, bookings, n: int):
        res = [0 for _ in range(1, n+1)]
        for each in bookings:
            for index in range(each[0], each[1]+1):
                res[index-1] += each[2]
        return res


if __name__ == "__main__":
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    s = Solution()
    print(s.corpFlightBookings0(bookings, n))
    print(s.corpFlightBookings(bookings, n))
