class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for index, num in enumerate(s):
            if num!=']' :
                stack.append(num)
            else:
#                 num == ']'
                copy_list = []
                while(stack and stack[-1].isalpha()):
                    copy_list.insert(0, stack.pop())
                # print(copy_list, stack)
                stack.pop()
                # pop '['
                num_list = []
                while(stack and stack[-1].isdigit()):
                    num_list.insert(0, stack.pop())
                # print(num_list)
                num_multipy = int("".join(num_list))
                stack += copy_list * num_multipy
        return "".join(stack)
    
s = "3[a]2[bc]"
sl = Solution()
print(sl.decodeString(s))

s = "3[a2[c]]"
print(sl.decodeString(s))


s = "2[abc]3[cd]ef"
print(sl.decodeString(s))
