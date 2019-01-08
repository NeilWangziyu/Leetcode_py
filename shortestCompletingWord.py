class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        check_dict = {}
        for each in licensePlate:
            if each.isalpha():
                each = each.lower()
                if each not in check_dict:
                    check_dict[each] = 1
                else:
                    check_dict[each] += 1
        length = 10000
        min_length = None
        for each in words:
            ok = False

            tem_dict = {}
            for digit in each:
                if digit not in tem_dict:
                    tem_dict[digit] = 1
                else:
                    tem_dict[digit] += 1

            for check_keys in check_dict.keys():
                if check_keys not in tem_dict:
                    ok = True

                else:
                    if tem_dict[check_keys] < check_dict[check_keys]:
                        ok = True
            if len(each) < length and ok==False:
                length = len(each)
                min_length = each

        return min_length





licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
s = Solution()
print(s.shortestCompletingWord(licensePlate, words))