# 프로그래머스 - Lv2.배상 비용 최소화 사본

# 배상 비용 = sigma{(선박의 완성까지 남은 일의 작업량)^2}

import heapq

def solution(no, works):
    result = 0
    max_heap_list = [(-x, x) for x in works]
    heapq.heapify(max_heap_list)

    if not max_heap_list:
        return 0
    for i in range(no):
        temp = heapq.heappop(max_heap_list)[1]
        if int(temp) < 1:
            return 0

        heapq.heappush(max_heap_list, (-(temp-1), temp-1))

    while max_heap_list:
        result += heapq.heappop(max_heap_list)[1] ** 2

    return result

N = 4
works = [1,1,1]
print(solution(N,works))