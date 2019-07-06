class Solution:
    def sampleStats(self, count):
        total_number = sum(count)
        if total_number == 0:
            return [0,0,0,0,0]
        elif total_number % 2 == 0:
            even = True
        else:
            even = False


        min_num = 256
        max_num = -1

        mean_num = -1

        most_count_num = -1
        most_count_num_value = -1

        res = 0

        total_number = sum(count)

        middle_number = total_number // 2
        first_number = -1
        second_number = -1
        # first_number is middle_number, second_number is middle_number+1 for even
        #

        total_number_counter = 0

        for i in range(256):
            if count[i] > 0:
                if i > max_num:
                    max_num = i
                if i < min_num:
                    min_num = i
                if count[i] > most_count_num_value:
                    most_count_num = i
                    most_count_num_value = count[i]

                if even == True:
                #     found two number

                    if total_number_counter > middle_number + 1:
                        pass
                    elif total_number_counter + count[i] < middle_number:
                        pass
                    elif total_number_counter < middle_number and total_number_counter + count[i] > middle_number + 1:
                        first_number = i
                        second_number = i
                    elif total_number_counter + count[i] == middle_number:
                        first_number = i
                    elif total_number_counter <= middle_number and total_number_counter + count[i] > middle_number:
                        if second_number == -1:
                            second_number = i
                        else:
                            pass
                else:
                    if total_number_counter > middle_number + 1:
                        pass
                    elif total_number_counter + count[i] < middle_number + 1:
                        pass
                    elif total_number_counter < middle_number + 1 and total_number_counter + count[i] >= middle_number + 1:
                        first_number = i
                        second_number = i
                    else:
                        pass

                res += count[i] * i
                total_number_counter += count[i]



        mean_num = res/total_number
        middle_number_res = (first_number + second_number) / 2

        # print(first_number, second_number)

        return list(map(float, [min_num, max_num, mean_num, middle_number_res, most_count_num]))



count = [0, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


s = Solution()
print(s.sampleStats(count))

count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.sampleStats(count))