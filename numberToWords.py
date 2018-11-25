def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    billion_str =[]
    million_str =[]
    thousand_str =[]

    if num >= 1000000000:
        billion = num // 1000000000
        billion_str = number_less_three_digit(billion)
        if (billion_str[0]!= '') or (billion_str[1]!= '') or (billion_str[2]!= ''):
            # 存在百位数
            billion_str.append('Billion')
        # print(billion_str)
        num = num % 1000000000

    if num >= 1000000:
        million = num // 1000000
        million_str = number_less_three_digit(million)
        if (million_str[0]!= '') or (million_str[1]!= '') or (million_str[2]!= ''):
            # 存在百位数
            million_str.append('Million')
        # print(million_str)
        num = num % 1000000

    if num>=1000:
        thousand = num // 1000
        thousand_str = number_less_three_digit(thousand)
        if (thousand_str[0]!= '') or (thousand_str[1]!= '') or (thousand_str[2]!= ''):
            # 存在百位数
            thousand_str.append('Thousand')
        print(thousand_str)
        num = num % 1000

    interger_str = number_less_three_digit(num)
    # print(interger_str)

    final_list = billion_str + million_str + thousand_str + interger_str

    res_str = ' '.join(final_list)
    if res_str == '':
        return 'Zero'
    else:
        return res_str


def number_less_three_digit(num):
    interger_num_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                         9: 'Nine', 0: '',
                         10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                         16: 'Sixteen', 17: 'Seventeen',18: 'Eighteen', 19: 'Nineteen'}
    decade_num_dict = {2: 'Twenty', 3: 'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
    number = []
    hundred = num // 100
    num = num % 100
    if num >= 20:
        decade = num // 10
        integer = num % 10

        number.append(interger_num_dict[hundred])
        number.append(decade_num_dict[decade])
        number.append(interger_num_dict[integer])
    else:
        number.append(interger_num_dict[hundred])
        number.append(interger_num_dict[num])
        number.append('')


    if number[0] != '':
        # 存在百位数
        number.insert(1,'Hundred')
    #     res_str =' '.join(number)
    # else:
    #     res_str =' '.join(number)
    # print(number)
    number_new =[]
    for tem in range(len(number)):
        # print(tem)
        # print(number[tem])
        if number[tem] !='':
            number_new.append(number[tem])
    number = number_new
    return number



if __name__ =='__main__':
    res = numberToWords(100000)
    print(res)