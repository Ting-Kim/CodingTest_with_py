def cal(arr1, arr2):
    answer = 0
    max_heap = []
    # 가장 값비싼 것을 기준으로 첫번쨰 가방부터 담는다.
    # (담을 수 있는 무게인 경우에만)
    j = 0

    for i in range(len(arr2)):

        while j < len(arr1) and arr2[i] >= arr1[j][0]:
            heapq.heappush(max_heap, -arr1[j][1])
            j += 1

        if len(max_heap) > 0:
            x = heapq.heappop(max_heap)
            answer += abs(x)

    # 결과 값어치 반환
    return(answer)

import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(list(map(int, sys.stdin.readline().split())))

for i in range(k):
    arr2.append(int(sys.stdin.readline()))

arr1.sort()
arr2.sort()

print(cal(arr1, arr2))




