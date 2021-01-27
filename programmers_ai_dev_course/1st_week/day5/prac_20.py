# lv3_N-Queen
# DFS & BackTracking(잘 사용한지 몰겠음..) 사용
# 효율이 좋지 않고, 하드코딩한 부분이 있어서 DP로 푸는 방법도 공부해야 한다.

from _collections import deque
import time

def solution(n):
    answer = 0
    stack = deque()
    num = set([_ for _ in range(1,n+1)])

    for i in range(1, n+1):
        stack.append([i])

    while stack:
        arr = stack.pop()

        if check(arr):
            set_temp = set(arr)
            set_temp.add(arr[-1]-1)
            set_temp.add(arr[-1]+1)
            if len(arr) > 1:
                set_temp.add(arr[-2] - 2)
                set_temp.add(arr[-2] + 2)
            if len(arr) > 2:
                set_temp.add(arr[-3] - 3)
                set_temp.add(arr[-3] + 3)
            if len(arr) > 3:
                set_temp.add(arr[-4] - 4)
                set_temp.add(arr[-4] + 4)
            for element in num.difference(set_temp):
                temp = list(arr)
                temp.append(element)
                stack.append(temp)


            # for i in range(1,n+1):
            #     # temp = [element for element in arr]
            #     temp = list(arr)
            #     if i in arr or i in [arr[-1]-1, arr[-1], arr[-1]+1]:
            #         continue
            #     temp.append(i)
            #     stack.append(temp)
        else:
            continue

        if len(arr) >= n: # 크기만큼 모두 채웠는데 이상 없다면 answer에 추가가
            answer += 1

    return answer

def check(arr):
    if len(arr) > 1:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                index_odd = j - i
                odd = abs(arr[i] - arr[j])
                if index_odd == odd or odd == 0:
                    return False

    return True

start = time.time()
n = 12
print(solution(n))
print("time: ", time.time() - start)