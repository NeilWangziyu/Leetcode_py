class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        from collections import Counter
        couter = Counter(s)
        print(couter)
        res = 0
        flag = False
        for each in couter.keys():
            if couter[each] % 2 == 1:
                flag = True
                res += couter[each] - 1
            else:
                res += couter[each]
        if flag:
            return res+1
        else:
            return res

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = set(s)
        k = 0
        res = 0
        for x in strs:
            num = s.count(x)
            if num % 2 == 0:
                res += num
            else:
                k = 1
                res += num - 1
        return k + res


s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
so = Solution()
print(so.longestPalindrome(s))