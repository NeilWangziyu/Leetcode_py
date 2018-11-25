def cut_rod(p,n):
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n+1):
        q = max(q, p[i]+cut_rod(p, n-i))
    return q


def dynamicProgram(p,n):
    r = [-1]*(n+1)
    r[0] = 0
    for j in range(1, n+1):
        q = -1
        if j<=10:
            for i in range(1, j+1):
                q = max(q, p[i]+r[j-i])
        else:
            for i in range(1, 11):
                q = max(q, p[i]+r[j-i])
        r[j] = q
    print(r)
    return r[n]


def dynnamicProgram_cut_cost(p, n):
#     every time cut, cost 1
    r = [-float('inf')] * (n+1)
    r [0] = 0
    r [1] = 1
    for j in range(2, n+1):
        q = -float('inf')
        if j<=10:
            for i in range(2, j+1):
                if i!=j:
                    q = max(q, p[i]+r[j-i]-1)
                else:
                    q = max(q, p[i]+r[j-i])

        else:
            for i in range(2, 11):
                if i!=j:
                    q = max(q, p[i]+r[j-i]-1)
                else:
                    q = max(q, p[i]+r[j-i])
        r[j] = q
    print(r)
    return r[n]

if __name__ == "__main__":
    p = [0,1,5,8,9,10,17,17,20,24,30]
    print(cut_rod(p, 9))
    print(dynamicProgram(p, 13))
    print(dynnamicProgram_cut_cost(p, 13))
