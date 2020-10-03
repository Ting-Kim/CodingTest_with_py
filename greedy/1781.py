# 파이썬 풀이
# https://velog.io/@ckstn0777/%EB%B0%B1%EC%A4%80-1781-%EC%BB%B5%EB%9D%BC%EB%A9%B4
# list보다 tuple이 성능이 더 좋다.(데이터가 변하지 않는다면 tuple로!)

import heapq, sys

n = int(sys.stdin.readline().strip())
# arr = []
#
# for _ in range(n):
#     arr.append(tuple(map(int, input().split())))

arr = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

arr.sort()
# print(arr)

queue = []
for deadline, score in arr:
    heapq.heappush(queue, score)

    if len(queue) > deadline:
        heapq.heappop(queue)

print(sum(queue))
