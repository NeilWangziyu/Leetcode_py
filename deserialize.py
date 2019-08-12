# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # if not s:
        #     return ""
        stack = []
        queue = []
        for each in s:
            if each == '[':
                stack.append(NestedInteger())
            elif each == ']' or each == ',':
                if queue:
                    num = ""
                    while (queue):
                        num += queue.pop(0)
                    stack[-1].add(NestedInteger(int(num)))
                if each == ']':
                    top = stack.pop()
                    if not stack:
                        return top
                    else:
                        stack[-1].add(top)
            else:
                queue.append(each)
        return NestedInteger(int(s))

    def deserialize2(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        cur = NestedInteger()
        i = 0
        ls = len(s)
        while i < ls:
            if 48 <= ord(s[i]) <= 57 or s[i] == '-':
                j = i
                i += 1
                while i < ls and 48 <= ord(s[i]) <= 57:
                    i += 1
                cur.add(NestedInteger(int(s[j: i])))
                continue
            elif s[i] == '[':
                stack.append(cur)
                cur = NestedInteger()
            elif s[i] == ']':
                stack[-1].add(cur)
                cur = stack.pop()
            i += 1
        return cur.getList()[0]


