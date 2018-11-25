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
                result = min(result, condtion)
            state[egg][floor] = result
    print(state)

    return state[K][N]


K = 4
N = 2000
print(superEggDrop(K, N))