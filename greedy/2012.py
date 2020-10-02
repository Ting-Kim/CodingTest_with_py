
def solve():
    answer = 0
    arr.sort()
    for i in range(n):
        answer += abs(arr[i] - (i+1))

    print(answer)
    return

import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for i in range(n)]

solve()