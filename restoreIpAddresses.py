class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        res = []

        def DFS(start, end , depth, list_tem):
            # print(list_tem)
            if depth == 4:
                if start == len(s):
                    res.append(list_tem)
                    return
                else:
                    return
            else:

                if end <= len(s):
                    if int(s[start:end]) <= 255 and len(str(int(s[start:end]))) == len(s[start:end]):
                        DFS(end, end+1, depth+1, list_tem+[s[start:end]])
                        DFS(start, end + 1, depth, list_tem)
                        return
                else:
                    return

        DFS(0, 1, 0, [])
        print(res)
        res_list= []
        for each in res:
            # print("".join(each))
            res_list.append(".".join(each))
        return res_list




t = "010010"
s = Solution()
print(s.restoreIpAddresses(t))