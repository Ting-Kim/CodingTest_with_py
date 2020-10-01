# / - \ 순으로 탐색
# 점마다 /-\ 순으로 반복해서 진행하며, 진행 성공한 경우 o체크 + 다음 process로..
def search(x, y):

    if y == m-1:
        graph[x][y] = 'o'   # 방문 체크
        # answer += 1
        return True

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
            graph[nx][ny] = 'o'  # 방문 체크

            if search(nx, ny):
                return True

    return False


import sys

n, m = map(int, sys.stdin.readline().strip().split())
dx = [-1, 0, 1]
dy = [1, 1, 1]
answer = 0
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
# graph = []
# for _ in range(n):
#     graph.append(list(sys.stdin.readline().strip()))

for i in range(n):
    if search(i, 0):
        answer += 1
# install(graph, n)


for i in range(n):
    print(graph[i])

print(answer)
'''
15 15
.xxxxxxxxxx....
...x.......xxx.
...x.......x...
..xx.......xx..
...x........xx.
.x.x......x.x..
...x......xx...
.x.x....xxx....
.x....x.x......
.x.....xx.x....
.x..x.xx.......
.....xx........
....x..........
......x........
...............
'''
