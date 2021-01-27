# 프로그래머스 - Lv3.배달

from collections import deque

def solution(N, road, K):
    answer = 0
    dist = [500001 for _ in range(N+1)]
    dist[1] = 0
    queue = deque([[1,0]])

    while queue:
        curr, curr_dist = queue.popleft()

        for dept, dest, l in road:
            if curr == dept and dist[dest] > curr_dist+l:
                dist[dest] = curr_dist+l
                queue.append([dest, curr_dist+l])
            if curr == dest and dist[dept] > curr_dist+l:
                dist[dept] = curr_dist+l
                queue.append([dept, curr_dist+l])

    for n in dist:
        if n <= K:
            answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4
print(solution(N,road,K))
