# 프로그래머스 - Lv2.더 맵게
# 스코빌 연산할 때 마다 데이터 삭제, 삽입(정렬) 필요
# => 힙 라이브러리 사용

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        food1 = heapq.heappop(scoville)
        if food1 > K:
            break
        elif not scoville:
            return -1

        food2 = heapq.heappop(scoville)
        mixed_food = food1 + (food2*2)
        heapq.heappush(scoville, mixed_food)
        answer += 1

    return answer


scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville,K))