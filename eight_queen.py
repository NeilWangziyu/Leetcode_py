import random
def conflict(state, nextX):
    # 冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，
    # 例如： state[0]=3，表示该皇后位于第1行的第4列上

    nextY = len(state)
    for i in range(nextY):
        #如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i] - nextX) in (0, nextY-i):
            return True
    return False

def queens(num, state=()):
    #采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos, )
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))




if __name__ == "__main__":
    # 不遍历
    prettyprint(random.choice(list(queens(8))))

    # 遍历
    i = 1
    print(list(queens(5)))
    # queens返回迭代器，list将迭代器的内容转为list
    for item in list(queens(5)):
        print('-----------------')
        print("solution ", i)
        i += 1
        print(item)
        prettyprint(item)
        print('-----------------')

