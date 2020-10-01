# / - \ 순으로 탐색
# 점마다 /-\ 순으로 반복해서 진행하며, 진행 성공한 경우 o체크 + 다음 process로..
def search(graph, x, y):
    global answer
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0])\
            or graph[x][y] != '.':
        return False

    if y == len(graph[0])-1 and graph[x][y] == '.':
        graph[x][y] = 'o'   # 방문 체크
        answer += 1
        return True


    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if search(graph, nx, ny):
            graph[x][y] = 'o'   # 방문 체크
            return True
    return False

def install(graph, a, b):
    global answer

    for i in range(a):
        search(graph, i, 0)

    return answer



n, m = map(int, input().split())
graph = []
dx = [-1, 0, 1]
dy = [1, 1, 1]
answer = 0

for _ in range(n):
    graph.append(list(input()))

answer = install(graph, n, m)

print(answer)

