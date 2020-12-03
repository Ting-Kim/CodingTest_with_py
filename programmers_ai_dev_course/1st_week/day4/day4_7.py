# 프로그래머스 - Lv3.여행 경로

# 한붓그리기 유형 -> 재귀적인 DFS 방법으로 해결
# 종료 조건이 만족되지 않았는데 방문한 노드에서 더이상 진행할 수 있는 경로가 없는 경우,
# 그 노드가 종료 지점이다.
from collections import deque

def solution(tickets):
    answer = []
    route = {}
    stack = deque(['ICN'])
    tickets.sort(key=lambda x:x[1], reverse=True)
    for t in tickets:
        route[t[0]] = route.get(t[0], []) + [t[1]]

    while stack:
        if stack[-1] not in route or not route[stack[-1]]:
            answer.append(stack.pop())
        else:
            stack.append(route[stack[-1]].pop())

    return answer[::-1]

tickets = [['ICN', "SFO"], ['ICN', "ATL"], ['SFO', 'ATL'], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

