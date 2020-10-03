def solve():
    if n <= k:
        print(0)
        return

    interval = [arr[i] - arr[i-1] for i in range(n-1,0,-1)]
    interval.sort(reverse=True)
    answer = 0


    for i in range(k-1, n-1):
        answer += interval[i]

    '''
    # 2개가 아니라 k개의 기지국. . HOW?
    for i in range(len(arr)-1):
        length = (arr[i] - arr[0]) + (arr[len(arr)-1] - arr[i+1])
        answer.append(length)
    '''

    print(answer)
    return

import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()
solve()