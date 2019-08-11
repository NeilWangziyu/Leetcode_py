class Solution:
    def ordinalOfDate(self, date: str) -> int:
        year, month, day = date.split("-")
        if month == "01":
            return int(day)
        if month == "02":
            return 31 + int(day)
        year = int(year)
        month = int(month)
        day = int(day)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            dict_each_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            res = 0
            for index in range(1, month):
                res += dict_each_day[index]
            return res + day
        else:
            dict_each_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            res = 0
            for index in range(1, month):
                res += dict_each_day[index]
            return res + day

