# class Solution:
#     def process_string(self, express):
#         print(express)
#         if '(' in express:
#             index_left = express.find('(')
#             index_right = express.find(')')
#             print(express[index_left+1:index_right])
#
#             left_item = express[1:index_left]
#             right_item = express[index_right+1:]
#             already_set = self.hash_for_string[express[index_left+1:index_right]]
#             if not left_item and not right_item:
#                 return already_set
#
#             new_set = set()
#             if left_item and not right_item:
#                 left_item_spilt = left_item.split(',')
#                 if len(left_item_spilt) == 1:
#                     left_item = left_item_spilt[0]
#                     for each in already_set:
#                         new_set.add(left_item+each)
#                     return new_set
#                 else:
#                     for each_extra in left_item_spilt[:-1]:
#                         new_set.add(each_extra)
#                     left_item = left_item_spilt[-1]
#                     for each in already_set:
#                         new_set.add(left_item+each)
#                     return new_set
#
#
#
#             if not left_item and right_item:
#                 right_item_spilt = right_item.split(',')
#                 if len(right_item_spilt) == 1:
#                     right_item = right_item_spilt[0]
#                     for each in already_set:
#                         new_set.add(each + right_item)
#                     return new_set
#                 else:
#                     for each_extra in right_item_spilt[:-1]:
#                         new_set.add(each_extra)
#                     right_item = right_item_spilt[0]
#
#                     for each in already_set:
#                         new_set.add(each+right_item)
#                     return new_set
#
#
#             if left_item and right_item:
#                 # 、、
#                 for each in already_set:
#                     new_set.add(left_item + each+right_item)
#                 return new_set
#         else:
#             # 、、
#             pass
#
#
#     def braceExpansionII(self, expression: str):
#
#         if not expression:
#             return []
#         stack = []
#
#         self.hash_for_string = {}
#
#         count = 0
#         for each in expression:
#             if each != '}':
#                 stack.append(each)
#             else:
#                 get_out = "}"
#                 while(stack and stack[-1]!='{'):
#                     get_out = stack.pop(-1) + get_out
#                 get_out = stack.pop(-1) + get_out
#
#                 print(get_out)
#                 get_out_res = self.process_string(get_out)
#                 count += 1
#                 self.hash_for_string["("+str(count)+")"] = get_out_res
#                 stack.append("("+str(count)+")")
#         print(stack)
#
#
#
#
# s = Solution()
# print(s.braceExpansionII("{a,b}{c{d,e}}"))
#
#
#


class Solution:
    def braceExpansionII(self, expression: str):
        expression = "{" + expression + "}"
        stack = []
        i = 0
        while i < len(expression):
            c = expression[i]
            if c == '{':
                stack.append(c)
                i += 1
            elif c == ',':
                stack.append(c)
                i += 1
            elif c == '}':
                ans = stack.pop()
                while stack[-1] != '{':
                    if stack[-1] == ',':
                        stack.pop()
                        ans = ans | stack.pop()
                    else:
                        temp = stack.pop()
                        res = set()
                        for pre in temp:
                            for suf in ans:
                                res.add(pre+suf)
                        ans = res
                stack.pop()
                while stack and stack[-1] != ',' and stack[-1] != '{':
                    temp = stack.pop()
                    res = set()
                    for pre in temp:
                        for suf in ans:
                            res.add(pre+suf)
                    ans = res
                stack.append(ans)
                i += 1
            else:
                start = i
                while i < len(expression) and expression[i] not in {'{', '}', ','}:
                    i += 1
                string = expression[start:i]
                ans = {string}
                while stack and stack[-1] != ',' and stack[-1] != '{':
                    temp = stack.pop()
                    res = set()
                    for pre in temp:
                        for suf in ans:
                            res.add(pre+suf)
                    ans = res
                stack.append(ans)
        return sorted(list(stack[0]))

