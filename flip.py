import random
from typing import List

import random
from typing import List


class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.flapped_mapping = {}
        self.flapped_cnt = 0
        self.total = n_rows * n_cols
        self.n_rows = n_rows
        self.n_cols = n_cols

    # While calc the random posi value, mapping the chosen posi value with max_posi. If the chosen posi value return again from random, then use the mapped max posi instead.
    def flip(self) -> List[int]:
        max_posi = self.total - 1 - self.flapped_cnt
        chosen = random.randint(0, max_posi)
        # print(f"Begin: chosen:{chosen} max_posi:{max_posi} flapped_cnt:{self.flapped_cnt} flapped_mapping:{self.flapped_mapping}")

        res = chosen
        # The chosen posi used before, so pick up the alternative posi value from mapping
        # keep loopping unitl found a un-used max posi value
        while self.flapped_mapping.get(res):
            res = self.flapped_mapping[res]

        self.flapped_mapping[chosen] = max_posi
        # print(f"End: chosen:{chosen} max_posi:{max_posi} flapped_cnt:{self.flapped_cnt} flapped_mapping:{self.flapped_mapping} res:{res} [{res//self.n_cols},{res%self.n_cols}] ")

        self.flapped_cnt += 1

        return [res // self.n_cols, res % self.n_cols]

    def reset(self) -> None:
        self.flapped_mapping.clear()
        self.flapped_cnt = 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()


class Solution1:
    def __init__(self, n_rows: int, n_cols: int):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        self.n_cols_counter = {}
        self.n_rows_counter = {}
        self.n_cols_list = list(range(n_cols))
        self.n_rows_list = list(range(n_rows))

    def flip(self) -> List[int]:
        while (True):
            if not self.n_rows_list or not self.n_cols_list:
                return

            if len(self.n_rows_list) > 1:
                rand_row_index = random.randint(0, len(self.n_rows_list) - 1)
            else:
                rand_row_index = 0

            if len(self.n_cols_list) > 1:
                rand_col_index = random.randint(0, len(self.n_cols_list) - 1)
            else:
                rand_col_index = 0
            # print(self.n_rows_list, self.n_cols_list)
            rand_row = self.n_rows_list[rand_row_index]
            rand_col = self.n_cols_list[rand_col_index]
            # print(rand_row, rand_col)

            if self.grid[rand_row][rand_col] == 0:
                self.grid[rand_row][rand_col] = 1
                if rand_row not in self.n_rows_counter:
                    self.n_rows_counter[rand_row] = 1

                if self.n_rows_counter[rand_row] == self.n_cols:
                    self.n_rows_list.pop(self.n_rows_list.index(rand_row))

                if rand_col not in self.n_cols_counter:
                    self.n_cols_counter[rand_col] = 1

                if self.n_cols_counter[rand_col] == self.n_rows:
                    self.n_cols_list.pop(self.n_cols_list.index(rand_col))

                return [rand_row, rand_col]

    def reset(self) -> None:
        self.grid = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        self.n_cols_counter = {}
        self.n_rows_counter = {}
        self.n_cols_list = list(range(self.n_cols))
        self.n_rows_list = list(range(self.n_rows))


class Solution0:
    def __init__(self, n_rows: int, n_cols: int):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    def flip(self) -> List[int]:
        while (True):
            rand_row = random.randint(0, self.n_rows - 1)
            rand_col = random.randint(0, self.n_cols - 1)
            if self.grid[rand_row][rand_col] == 0:
                self.grid[rand_row][rand_col] = 1
                return [rand_row, rand_col]

    def reset(self) -> None:
        self.grid = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()