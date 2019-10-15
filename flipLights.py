class Solution:
    def flipLights(self, n: int, m: int) -> int:
        light_odd = ["1" if i % 2 == 0 else "0" for i  in range(n)]
        light_odd_num = int("".join(light_odd), 2)
        light_even = ["0" if i % 2 == 0 else "1" for i  in range(n)]
        light_even_num = int("".join(light_even), 2)
        light_three = ["1" if i % 3 == 0 else "0" for i in range(n)]
        light_three_num = int("".join(light_three), 2)

        light_begin = "1" * n

        light_begin_num = int(light_begin, 2)
        light_all_num = int(light_begin, 2)

        check_map = set()
        check_map.add(light_begin_num)

        for i in range(m):
            check_map_next = set()
            for each in check_map:
                check_map_next.add(each ^ light_all_num)
                check_map_next.add(each ^ light_even_num)
                check_map_next.add(each ^ light_odd_num)
                check_map_next.add(each ^ light_three_num)
            check_map = check_map_next

        # for each in check_map:
        #     print(each)
        return len(check_map)

    def flipLights2(self, n: int, m: int) -> int:
        if n == 0:
            return 0
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8


if __name__ == '__main__':
    s = Solution()
    print(s.flipLights(3,1))







