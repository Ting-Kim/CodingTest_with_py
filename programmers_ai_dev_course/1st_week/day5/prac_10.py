# 프로그래머스 - Lv2.배상 비용 최소화 사본

# 배상 비용 = sigma{(선박의 완성까지 남은 일의 작업량)^2}

import heapq

def solution(no, works):
    result = 0
    heapq.heapify([(-x, x) for x in works])
    last = len(works)-1

    for i in range(N):
        print(heapq.heappop(works))


    return result

N = 3
works = [4,6,1]
print(solution(N,works))