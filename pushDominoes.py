class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        模拟左推倒以及右推倒 根据推倒的时间先后判断最终多米诺的朝向        :param dominoes:
        :return:
        """
        length = len(dominoes)
        if len(dominoes) < 2:
            return dominoes
        push_l = [-1 for i in range(len(dominoes))]
        push_r = [-1 for i in range(len(dominoes))]

        push = False
        for i in range(length):
            if dominoes[i] == 'R':
                push_r[i] = 0
                push = True
            else:
                if push == False:
                    continue
                elif dominoes[i] == 'L':
                    push = False
                    continue
                else:
                    push_r[i] = push_r[i-1] + 1
        print(push_r)
        push = False
        for i in range(length-1, -1, -1):
            if dominoes[i] == 'L':
                push_l[i] = 0
                push = True
            else:
                if push == False:
                    continue
                elif dominoes[i] == 'R':
                    push = False
                    continue
                else:
                    push_l[i] = push_l[i+1] + 1
        print(push_l)

        res = ['.' for _ in range(length)]
        for i in range(length):
            if push_l[i] == push_r[i]:
                continue

            elif push_l[i] < push_r[i]:
                if push_l[i] != -1:
                    res[i] = 'L'
                else:
                    res[i] = 'R'

            elif push_l[i] > push_r[i]:
                if push_r[i] != -1:
                    res[i] = 'R'
                else:
                    res[i] = 'L'

            else:
                continue
        return "".join(res)

    def pushDominoes2(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        s=[]
        out=[]
        for i in dominoes:
            s.append(i)
            if i=='L':
                if s[0]=='.':
                    out.append('L'*len(s))
                    s=[]
                elif s[0]=='R':
                    if len(s)%2==0:
                        out.append('R'*int((len(s)/2)))
                        out.append('L'*int((len(s)/2)))
                    else:
                        out.append('R'*int((len(s)//2)))
                        out.append('.')
                        out.append('L'*int((len(s)//2)))
                    s=[]
                else:
                    out.extend(s)
                    s=[]
            elif i=='R':
                if s[0]=='.':
                    out.extend(s[:-1])
                elif s[0]=='R':
                    out.append('R'*(int(len(s))-1))
                s=['R']
        if s:
            if s[0]=='R':
                out.append('R'*int(len(s)))
            else:
                out.extend(s)
        return ''.join(out)

    def pushDominoes3(self, d):
        """
        :type dominoes: str
        :rtype: str
        """
        d = "L" + d + "R"
        res = []
        l = 0
        for r in range(1, len(d)):
            if d[r] == '.':
                continue
            mid = r - l - 1
            if l:
                res.append(d[l])
            if d[l] == d[r]:
                res.append(d[l] * mid)
            elif d[l] == 'L' and d[r] == 'R':
                res.append('.' * mid)
            else:
                res.append('R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2))
            l = r
        return "".join(res)


dominoes = ".L.R...LR..L.."
s = Solution()
print(s.pushDominoes(dominoes))