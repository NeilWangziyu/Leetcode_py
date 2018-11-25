def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s

    result = []
    circle = numRows * 2 - 2
    row = 0
    k = 0
    while(k*circle<len(s)):
        print("a")
        result.append(s[k*circle])
        k += 1
    row = 1
    while(row<numRows-1):
        print(row)
        k = 0
        while(k*circle+row < len(s)):
            result.append(s[k*circle+row])
            if ((k+1)*circle-row < len(s)):
                result.append(s[(k+1)*circle-row])
            k += 1
        row += 1

    k = 0
    while(k*circle+numRows-1 < len(s)):
        print("c")
        result.append(s[k*circle+numRows-1])
        k += 1

    return "".join(result)


print(convert(s = "PAYPALISHIRING", numRows = 4))
