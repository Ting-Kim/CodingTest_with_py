def solution(arr):
    signs = [1]
    values = []
    for x in arr:
        if x == '+':
            signs.append(1)
        elif x== '-':
            signs.append(-1)
        else:
            values.append(int(x))

    base = sum([x*y for (x,y) in zip(signs, values)])
    # 10
    n = len(values) # n = len(signs)
    loss = [0] * n
    gain = [0] * n
    l, g = 0, 0
    for i in range(n-1, -1, -1): # 10, 9, 8, 7, ..., 0
        if signs[i] == 1: # 양수
            # 어딘가에 쌓아라 (l)
            l += values[i]
        else:
            # 쌓인 양수를 엎어라
            loss[i] = l
            # 양수 쌓은 건 이제 버려라
            l = 0
            # 음수 쌓여 있던 것도 엎어라
            gain[i] = g
            # 음수도 또한 쌓아라
            g += values[i]


    # gain 과 loss의 차이 중에 가장 큰 것
    benefit = max([g - l for (g, l) in zip(gain, loss)])
    return base + 2 * benefit


