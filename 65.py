# 不用加减乘除做加法
def Add(num1, num2):
    sum = num1 ^ num2
    carry = (num1 & num2) << 1
    num1 = sum
    num2 =carry

    while(num2!=0):
        sum = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = sum
        num2 = carry

    return num1

if __name__ == "__main__":
    a = 10
    b = 15
    print(a+b)
    print(Add(a, b))