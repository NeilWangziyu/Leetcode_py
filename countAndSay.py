class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            init = "1"
            for i in range(1, n):
                res = ""
                char = init[0]
                count = 1
                for each in init[1:]:
                    if each == char:
                        count += 1
                    else:
                        res += str(count)
                        res += char
                        char = each
                        count = 1
                res += str(count)
                res += char

                init = res
        return res





n = 4
s = Solution()
print(s.countAndSay(n))