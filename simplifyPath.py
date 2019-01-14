class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        print(path)
        res = []
        for each in path:
            if each == "":
                pass
            elif each == "..":
                if res != []:
                    res.pop()
            elif each == '.':
                pass
            else:
                res.append(each)
        return "/"+"/".join(res)



path = "/a/../../b/../c//.//"

s = Solution()
print(s.simplifyPath(path))