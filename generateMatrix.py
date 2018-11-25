def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n == 0:
        return 0
    if n == 1:
        return [[1]]

    matrix = [[0]*n for _ in range(n)]

    count = 1

    circle = 0
    xrange = n - 1

    while(count<n**2):
        print("start",count)
        print(matrix)

        for i in range(circle, circle+xrange):
            matrix[circle][i] = count
            count += 1
            print(count)
            print(matrix)

        for j in range(circle, circle+xrange):
            matrix[j][n-1-circle] = count
            count += 1
            print(count)
            print(matrix)

        for k in range(circle, circle+xrange):
            matrix[n-1-circle][-k-1] = count
            count += 1
            print(count)
            print(matrix)

        for l in range(circle, circle+xrange):
            matrix[-l-1][-n+circle] = count
            count += 1
            print(count)
            print(matrix)


        xrange -= 2
        circle += 1
        print("circle",circle, "finished")
        print(xrange,count)
        print(matrix)
        if n%2==1:
            matrix[circle][circle] = count

    return matrix


n = 17
print(n**2)
print(generateMatrix(n))
