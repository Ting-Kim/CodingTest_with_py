import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville and scoville[0] < K and len(scoville) > 1:
        h1 = heapq.heappop(scoville)
        h2 = heapq.heappop(scoville)
        heapq.heappush(scoville, h1 + h2*2)
        answer += 1

    if not scoville or scoville[0] < K:
        return -1

    return answer


scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville,K))