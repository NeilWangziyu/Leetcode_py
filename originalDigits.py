class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_list = {}
        for each in "abcdefghigklmnopqrstuvwxyz":
            if each not in dict_list:
                dict_list[each] = 0

        for each in s:
            dict_list[each] += 1

        print(dict_list)

        #         check each num
        res = []
        while (dict_list['z'] > 0):
            res.append(0)
            dict_list['z'] -= 1
            dict_list['e'] -= 1
            dict_list['r'] -= 1
            dict_list['o'] -= 1


        while (dict_list['w'] > 0):
            res.append(2)
            dict_list['t'] -= 1
            dict_list['w'] -= 1
            dict_list['o'] -= 1


        while (dict_list['u'] > 0):
            res.append(4)
            dict_list['f'] -= 1
            dict_list['o'] -= 1
            dict_list['u'] -= 1
            dict_list['r'] -= 1



        while (dict_list['x'] > 0):
            res.append(6)
            dict_list['s'] -= 1
            dict_list['i'] -= 1
            dict_list['x'] -= 1
        #
        # while (dict_list['s'] > 0 and dict_list['e'] > 1 and dict_list['v'] > 0 and dict_list['n'] > 0):
        #     res += '7'
        #     dict_list['s'] -= 1
        #     dict_list['v'] -= 1
        #     dict_list['n'] -= 1
        #     dict_list['e'] -= 2

        while (dict_list['g'] > 0):
            res.append(8)
            dict_list['e'] -= 1
            dict_list['i'] -= 1
            dict_list['g'] -= 1
            dict_list['h'] -= 1
            dict_list['t'] -= 1



        while (dict_list['o'] > 0):
            res.append(1)
            dict_list['o'] -= 1
            dict_list['n'] -= 1
            dict_list['e'] -= 1

        while (dict_list['h'] > 0):
            res.append(3)
            dict_list['t'] -= 1
            dict_list['h'] -= 1
            dict_list['r'] -= 1
            dict_list['e'] -= 2

        while (dict_list['f'] > 0):
            res.append(5)
            dict_list['f'] -= 1
            dict_list['i'] -= 1
            dict_list['v'] -= 1
            dict_list['e'] -= 1

        while (dict_list['s'] > 0):
            res.append(7)
            dict_list['s'] -= 1
            dict_list['v'] -= 1
            dict_list['n'] -= 1
            dict_list['e'] -= 2

        while (dict_list['i'] > 0 and dict_list['n'] > 1 and dict_list['e'] > 0):
            res.append(9)
            dict_list['n'] -= 2
            dict_list['i'] -= 1
            dict_list['e'] -= 1

        res.sort()
        res_str = ""
        for each in res:
            res_str += str(each)
        return res_str

    def originalDigits2(self, s):

        zero = s.count('z')
        six = s.count('x')
        seven = s.count('s') - six
        five = s.count('v') - seven
        four = s.count('u')
        two = s.count('w')
        eight = s.count('g')
        nine = s.count('i') - six - eight - five
        three = s.count('t') - two - eight
        one = s.count('o') - zero - two - four
        return '0' * zero + '1' * one + '2' * two + '3' * three + '4' * four + '5' * five + '6' * six + '7' * seven + '8' * eight + '9' * nine


s = Solution()
print(s.originalDigits("zeroonetwothreefourfivesixseveneightnine"))
print(s.originalDigits2("zeroonetwothreefourfivesixseveneightnine"))











