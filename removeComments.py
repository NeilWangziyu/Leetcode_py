class Solution:
    # def removeComments(self, source: 'List[str]') -> 'List[str]':
    #     if not source:
    #         return ""
    #     in_comment = False
    #     res = []
    #     inside_res = ""
    #     for i in range(len(source)):
    #         if not in_comment:
    #             index_line = source[i].find("//")
    #             if index_line != -1:
    #                 inside_res += source[i][:index_line]
    #                 if inside_res:
    #                     res.append(inside_res)
    #                 inside_res = ""
    #             else:
    #                 index_comment_init = source[i].find("/*")
    #                 if index_comment_init != -1:
    #                     index_comment_end = source[i][index_comment_init+2:].find("*/")
    #                     if index_comment_end == -1:
    #                         inside_res += source[i][:index_comment_init]
    #                         in_comment = True
    #                         continue
    #                     else:
    #                         print(index_comment_init, index_comment_end)
    #                         inside_res += source[i][:index_comment_init]
    #                         print(inside_res)
    #                         inside_res += source[i][index_comment_end + 2 + len(source[i][index_comment_init+2:]):]
    #                         print(inside_res)
    #                         if inside_res:
    #                             res.append(inside_res)
    #                         inside_res = ""
    #                 else:
    #                     res.append(source[i])
    #                     inside_res = ""
    #
    #         else:
    #             # in comment
    #             index_end = source[i].find("*/")
    #             if index_end == -1:
    #                 pass
    #             else:
    #                 index_comment_init = source[i][index_end + 2:].find("/*")
    #                 if index_comment_init == -1:
    #                     inside_res += source[i][index_end + 2:]
    #                     if inside_res:
    #                         res.append(inside_res)
    #                     inside_res = ""
    #                     in_comment = False
    #                 else:
    #                     inside_res += source[i][index_end + 2:index_comment_init+len(source[i][index_end + 2:])]
    #                     if inside_res:
    #                         res.append(inside_res)
    #                     inside_res = ""
    #
    #     print(len(res))
    #     return res

    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        multi = False
        line = ''
        for s in source:
            i = 0
            while i < len(s):
                if not multi:
                    if s[i] == '/' and i < len(s) - 1 and s[i + 1] == '/':
                        break
                    elif s[i] == '/' and i < len(s) - 1 and s[i + 1] == '*':
                        multi = True
                        i += 1
                    else:
                        line += s[i]
                else:
                    if s[i] == '*' and i < len(s) - 1 and s[i + 1] == '/':
                        multi = False
                        i += 1
                i += 1
            if not multi and line:
                res.append(line)
                line = '' # 注意line重新设置成空字符串的位置
        return res
# ---------------------
# 作者：负雪明烛
# 来源：CSDN
# 原文：https://blog.csdn.net/fuxuemingzhu/article/details/79540349
# 版权声明：本文为博主原创文章，转载请附上博文链接！


source = \
    ["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]
s = Solution()
print(s.removeComments(source))