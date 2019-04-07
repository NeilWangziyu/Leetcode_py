# flush in poker
def IsContinuous(numbers):
    if not numbers or len(numbers) < 1 :
        return False

    numbers.sort()
    number_of_zero = 0
    number_of_gap = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            number_of_zero += 1

    small = number_of_zero
    big = small + 1
    while(big < len(numbers)):
        if numbers[small] == numbers[big]:
            return False

        number_of_gap += (numbers[big] - numbers[small] - 1)
        small = big
        big += 1

    if number_of_gap <= number_of_zero:
        return True
    else:
        return False

