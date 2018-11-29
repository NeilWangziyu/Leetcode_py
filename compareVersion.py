class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_separate = version1.split('.')
        version2_separate = version2.split('.')

        ver1 = 0
        for i, num in enumerate(version1_separate):
            ver1 += int(num)*(0.1**i)

        ver2 = 0
        for i, num in enumerate(version2_separate):
            ver2 += int(num)*(0.1**i)

        if ver1>ver2:
            return 1
        elif ver1 < ver2:
            return -1
        else:
            return 0




        # while (version1_separate[-1] == '0' and version1_separate):
        #     version1_separate.pop(-1)
        #
        # while (version2_separate[-1] == '0' and version2_separate):
        #     version2_separate.pop(-1)
        #




        # if not version2_separate and not version1_separate:
        #     return 0
        #
        # if not version2_separate:
        #     return -1
        # if not version1_separate:
        #     return 1
        # if len(version1_separate) > len(version2_separate):
        #     max_len = len(version1_separate)
        #     min_len = len(version2_separate)
        #     flag = 1
        # elif len(version1_separate) < len(version2_separate):
        #
        #     min_len = len(version1_separate)
        #     max_len = len(version2_separate)
        #     flag = -1
        #
        # else:
        #     min_len = len(version1_separate)
        #     max_len = len(version2_separate)
        #     flag = 0
        #
        # for i in range(max_len):
        #     if int(version1_separate[i]) > int(version2_separate[i]):
        #         return 1
        #     elif int(version1_separate[i]) < int(version2_separate[i]):
        #         return -1
        #     elif i == min_len - 1:
        #         return flag


s = Solution()
print(s.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))