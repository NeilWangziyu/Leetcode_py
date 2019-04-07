# max profit
def MaxDiff(number):
    if not number:return 0
    if len(number) < 2:
        return 0

    min_num = number[0]
    max_profit = 0
    for i in range(1, len(number)):
        max_profit = max(number[i] - min_num, max_profit)
        min_num = min(min_num, number[i])
    return max_profit

if __name__ == "__main__":
    print(MaxDiff([9,11,8,5,7,12,16,14]))