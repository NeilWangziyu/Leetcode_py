def superEggDrop(K, N):
    """
    :type K: int
    :type N: int
    :rtype: int
    """
    state =  [[0 for i in range(N+1)] for i in range(K+1)]
    # print(state)
    for i in range(1, N + 1):
        state[1][i] = i
    for j in range(1, K+1):
        state[j][1] = 1
    # print(state)
    for egg in range(2, K+1):
        for floor in range(2, N+1):
            result = float('inf')
            for drop in range(1, floor+1):
                broken = state[egg-1][drop-1]
                unbroken = state[egg][floor-drop]
                condtion = max(broken, unbroken) + 1
                # condition:破和不破两种可能性，再加上这一次用掉的丢弃机会
                result = min(result, condtion)
                # 每一个drop从1到 floor，总有一个最小解，就是floor楼层的最优
            state[egg][floor] = result
    print(state)

    return state[K][N]

def superEggDrop2(K, N):
    """
        :type K: int
        :type N: int
        :rtype: int
        """
    DP = [0 for i in range(K+1)]
    # DP[i]=n表示i个鸡蛋，经过move次移动，最多检测n层楼
    move = 0
    while(DP[K]<N):
        for i in range(K, 0, -1):
            # print(i)
            DP[i] += DP[i-1] + 1

        move += 1
    return move


K = 2
N = 100
print(superEggDrop(K, N))
print(superEggDrop2(K, N))