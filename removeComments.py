class Solution:
    def removeComments(self, source: 'List[str]') -> 'List[str]':
        if not source:
            return ""
        in_comment = False
        res = []
        inside_res = ""
        for i in range(len(source)):
            if not in_comment:
                index_line = source[i].find("//")
                if index_line != -1:
                    inside_res += source[i][:index_line]
                    if inside_res:
                        res.append(inside_res)
                    inside_res = ""
                else:
                    index_comment_init = source[i].find("/*")
                    if index_comment_init != -1:
                        index_comment_end = source[i][index_comment_init+2:].find("*/")
                        if index_comment_end == -1:
                            inside_res += source[i][:index_comment_init]
                            in_comment = True
                            continue
                        else:
                            print(index_comment_init, index_comment_end)
                            inside_res += source[i][:index_comment_init]
                            print(inside_res)
                            inside_res += source[i][index_comment_end + 2 + len(source[i][index_comment_init+2:]):]
                            print(inside_res)
                            if inside_res:
                                res.append(inside_res)
                            inside_res = ""
                    else:
                        res.append(source[i])
                        inside_res = ""

            else:
                # in comment
                index_end = source[i].find("*/")
                if index_end == -1:
                    pass
                else:
                    index_comment_init = source[i][index_end + 2:].find("/*")
                    if index_comment_init == -1:
                        inside_res += source[i][index_end + 2:]
                        if inside_res:
                            res.append(inside_res)
                        inside_res = ""
                        in_comment = False
                    else:
                        inside_res += source[i][index_end + 2:index_comment_init+len(source[i][index_end + 2:])]
                        if inside_res:
                            res.append(inside_res)
                        inside_res = ""


        print(len(res))
        return res




source = \
    ["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]
s = Solution()
print(s.removeComments(source))