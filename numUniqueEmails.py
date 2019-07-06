class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if not emails:
            return 0
        dict = {}
        for each in emails:
            # print(each.split('@'))
            part1 = each.split('@')[0]
            part2 = each.split('@')[1]
            if "+" in part1:
                part1 = part1.split("+")[0]
                part1 = "".join(part1.split("."))
            else:
                part1 = "".join(part1.split("."))
            whole = part1+part2
            if whole not in dict:
                dict[whole] = 1
        return len(dict.keys())



emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


s = Solution()
print(s.numUniqueEmails(emails))