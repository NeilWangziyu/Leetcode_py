class Solution:
    def numRabbits(self, answers):
        from collections import Counter
        if not answers:
            return 0

        counter = Counter(answers)
        # print(counter)
        c = 0
        number_hash = {}
        for each in counter.keys():
            max_number = each + 1
            true_number_least = counter[each]
            if max_number >= true_number_least:
                number_hash[c] = max_number
                c += 1
            else:
                while(max_number < true_number_least):
                    number_hash[c] = max_number
                    true_number_least -= max_number
                    c += 1
                number_hash[c] = max_number
                c += 1
        # print(number_hash)
        res = 0
        for each in number_hash.keys():
            res += number_hash[each]
        return res






answers = [0,0,1,1,1]
s = Solution()
print(s.numRabbits(answers))
