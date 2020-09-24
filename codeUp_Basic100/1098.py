x, y = map(int, input().split())
arr = [[0 for i in range(y)] for j in range(x)]
n = int(input())

for i in range(n):
    l, d, a, b = map(int, input().split())
    # l = 길이
    # d = 방향 (0->가로, 1->세로)
    # a,b 좌표
    for j in range(l):
        # if b - 1 + j > y - 1 or a - 1 + j > x - 1:
        #     break
        if d == 0:  # 가로
            if b - 1 + j > y - 1:
                continue
            arr[a-1][b-1+j] = 1


        if d == 1:  # 세로
            if a - 1 + j > x - 1:
                continue
            arr[a-1+j][b-1] = 1

for i in range(x):
    for j in range(y):
        print(arr[i][j], end = ' ')
    print()


