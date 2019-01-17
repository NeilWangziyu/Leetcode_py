class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0:
            return ["0:00"]

        def check_time(string):
            hour = string[0:4]
            minute = string[4:]
            hour_dec = int(hour, 2)
            minute_dec = int(minute, 2)
            if (hour_dec < 12 and minute_dec <=59):
                if str(hour_dec)+":"+"{:0>2d}".format(minute_dec) != "0:00":
                    return str(hour_dec)+":"+"{:0>2d}".format(minute_dec)
                return False
            else:
                return False

        res = []

        def dfs(count, length, check_list):


            if count == num:
                str_check = check_list + ["0"] * (10-len(check_list))
                print(str_check)
                if check_time("".join(str_check)) != False:
                    res.append(check_time("".join(str_check)))
                    return
            else:
                if length < 10:
                    dfs(count+1, length+1, check_list+["1"])
                    dfs(count,length+1,  check_list + ["0"])

        dfs(0, 0, [])

        return res






num = 2
s = Solution()
print(s.readBinaryWatch(num))