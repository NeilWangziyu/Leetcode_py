def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    M = len(matrix)
    N = len(matrix[0])
    list = []
    count = 0
    while(N>=2) and (M>=2):
        for i in range(N):
            list.append(matrix[count][i+count])
        for j in range(1,M):
            list.append(matrix[j][N-1])
            M = M - 1
        for k in range(1,N):
            list.append(matrix[k][N-1-k])
            N = N - 1
        for l in range(1,M-1):
            list.append(matrix[M-1-l][count])
        count = count + 1
        N = N - 1

    print(list)
    print(N)
    print(M)


arr = [
 [ 1, 2, 3 ,4],
 [ 4, 5, 6 ,7],
 [ 7, 8, 9 ,10],
 [ 8, 9, 10 ,11]]
spiralOrder(arr)
