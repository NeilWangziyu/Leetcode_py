class Solution:
    def lastSubstring0(self, s: str) -> str:
        # 超时
        def all_sub_set(input):
            if not input:
                return []
            lenth = len(input)
            if lenth == 1:
                return [input]
            all_Subset = set()
            for i in range(lenth):
                for j in range(i+1, lenth+1):
                    all_Subset.add(input[i:j])
            return list(all_Subset)
        all_sub = all_sub_set(s)
        all_sub.sort()
        return all_sub[-1]

    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        index_dict={}

        for i,char in enumerate(s):
            if i>0:
                if s[i-1]!=char:
                    if char not in index_dict:
                        index_dict[char] = [i]
                    else:
                        index_dict[char].append(i)
            else:
                if char not in index_dict:
                    index_dict[char]=[i]
                else:
                    index_dict[char].append(i)
        keys=list(index_dict.keys())
        keys.sort()
        candidate = index_dict[keys[-1]]
        maxlength = len(s)-candidate[0]
        if len(candidate)==1:
            return s[candidate[0]:]

        for i in range(2,maxlength):
            max_string=''
            next_candidate=[]
            for j in candidate:
                if not max_string:
                    max_string=s[j:j+i]
                    next_candidate=[j]
                else:
                    if s[j:j+i]==max_string:
                        next_candidate.append(j)
                    elif s[j:j+i]>max_string:
                        max_string=s[j:j+i]
                        next_candidate = [j]
            candidate=next_candidate
        return s[candidate[0]:]

s = Solution()
print(s.lastSubstring("abab"))
print(s.lastSubstring("leetcode"))




