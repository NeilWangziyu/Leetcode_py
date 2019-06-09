class Solution:
    res_set = ""
    def smallestSubsequence(self, text: str) -> str:
        """
        超时
        """
        def DFS(depth, total_length, res_length, tem):
            if len(tem) == res_length:
                # print(self.res_set, tem, min(self.res_set, tem))
                self.res_set = min(self.res_set, tem)

            if depth >= total_length:
                pass

            else:
                for i in range(depth, total_length):
                    if new_text[i] not in tem:
                        DFS(i+1, total_length, res_length, tem+new_text[i])


        if not text:
            return ""
        new_text = ""
        init = 0
        init_char = text[0]
        while(init < len(text)):
            if text[init] == init_char:
                init += 1
            else:
                new_text += init_char
                init_char = text[init]

        if not new_text or init_char != new_text[-1]:
            new_text += init_char

        res_length = len(set(new_text))
        self.res_set = "z" * res_length


        DFS(0, len(new_text), res_length, "")
        return self.res_set

    def smallestSubsequence2(self, text):
        """
        :type text: str
        :rtype: str
        """
        from collections import Counter
        cnts = Counter(text)
        stack = []
        visited = set()
        for c in text:
            if c in visited:
                cnts[c] -= 1
                continue
            while stack and c < stack[-1] and cnts[stack[-1]]:
                item = stack.pop()
                visited.remove(item)
            cnts[c] -= 1
            visited.add(c)
            stack.append(c)
        return ''.join(stack)


s = Solution()
print(s.smallestSubsequence(text="leetcode"))
print(s.smallestSubsequence(text="abcd"))
print(s.smallestSubsequence(text="cdadabcc"))
print(s.smallestSubsequence(text="ecbacba"))
print(s.smallestSubsequence(text="aaaaaaa"))

