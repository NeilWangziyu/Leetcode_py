class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if not input:
            return 0

        stack = []
        chrlen = 0
        tablen = 0
        longest = 0
        is_file = False
        input += "\n"
        for each in input:
            if each == '\n':
                # print(stack,len(stack), chrlen, tablen)
                while(stack != [] and len(stack) > tablen):
                    stack.pop()
                if stack != []:
                    length = stack[-1] + 1 + chrlen
                else:
                    length = 0 + chrlen

                if is_file:
                    if (length > longest):
                        longest = length
                else:
                    stack.append(length)

                chrlen = 0
                tablen = 0
                is_file = 0

            elif each == '\t':
                tablen +=1
            else:
                if (each == '.'):
                    is_file = True
                chrlen += 1
        return longest



    def lengthLongestPath2(self, input: 'str') -> 'int':
        """
        Best result
        :param input:
        :return:
        """
        result_len, path_list = 0, []
        for string in input.split('\n'):
            now_tab_num = string.count('\t')
            string = string[now_tab_num:]
            if len(path_list) > now_tab_num:
                path_list[now_tab_num] = string
            else:
                path_list.append(string)
            if string.count('.'):
                result_len = max(result_len, len('/'.join(path_list[:now_tab_num + 1])))
        return result_len


input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
s = Solution()
print(s.lengthLongestPath(input))