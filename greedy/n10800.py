
# https://mygumi.tistory.com/273 참고 .. (누적합!)


class ball:
    def __init__(self, id, color, score):
        self.id = id
        self.color = color
        self.score = score


def solve(arr):
    sum = 0

    arr.sort(key=lambda obj:obj.score)
    j = 0

    for i in range(1,n):

        while arr[j].score < arr[i].score:
            sum += arr[j].score
            score_c[arr[j].color] += arr[j].score
            j += 1

        player[arr[i].id] = sum - score_c[arr[i].color]

    for k in range(n):
        print(player[k])

    return 1

import sys

n = int(sys.stdin.readline())
ball_arr = []
player = [0 for _ in range(n+1)]
score_c = [0 for _ in range(n+1)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ball_arr.append(ball(i, a, b))

solve(ball_arr)

