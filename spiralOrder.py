def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    circle = 0
    if matrix == []:
        return []
    m = len(matrix)
    n = len(matrix[0])
    range1 = n - 1
    range2 = m - 1
    print(m)
    print(n)
    new_list = [0] * (n * m)
    count = 0
    while (range1 >= 0 and range2 >= 0):
        if range1 != 0 and range2 != 0:
            for i in range(circle, circle + range1):
                print(matrix[circle][i])
                new_list[count] = matrix[circle][i]
                count += 1
            for j in range(circle, circle + range2):
                new_list[count] = matrix[j][n - 1 - circle]
                count += 1
            for k in range(circle, circle + range1):
                new_list[count] = matrix[m - 1 - circle][-k - 1]
                count += 1
            for l in range(circle, circle + range2):
                new_list[count] = matrix[-l - 1][-n + circle]
                count += 1
        if range1 != 0 and range2 == 0:
            print("finish2")
            for i in range(circle, n - circle):
                new_list[count] = matrix[circle][i]
                count += 1
            break
        if range1 == 0 and range2 != 0:
            print("finish0")
            for i in range(circle, m - circle):
                new_list[count] = matrix[i][circle]
                count += 1
            break

        if range1 == 0 and range2 == 0:
            print("finish1")
            new_list[count] = matrix[circle][circle]
            count += 1
            break

        circle += 1
        range1 -= 2
        range2 -= 2
        print(circle, range1, range2, count)
    print("circle:", new_list)
    return new_list



#
# matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralOrder(matrix))