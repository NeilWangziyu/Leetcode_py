import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # if day == 1 and month == 1 and year == 1970:
        #     return "Thursday"
        #
        # separate_day = 0
        #
        # year_gap = year - 1970
        input_day = datetime.datetime(year, month, day)
        weekday = input_day.weekday()
        weekday = weekdays[weekday]
        return weekday


