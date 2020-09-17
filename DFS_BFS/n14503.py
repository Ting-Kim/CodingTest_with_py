def dfs(dir, y, x):
    global cnt
    # 경계조건 : 영역 밖으로 나갔을 경우
    if x < 0 or y < 0 or x >= m or y >= n:
        return

    # 청소가 안되어 있는 경우 방문 처리( 2는 방문, 1은 벽 )
    if graph[y][x] == '0':
        cnt += 1
        graph[y][x] = '2'

    for i in range(dir+7, dir+3,-1):

        i = i % 4
        # print('dir =',dir,'and, i =', i)
        ny = y + dy[i]
        nx = x + dx[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue

        if graph[ny][nx] == '0':
            dfs(i, ny, nx)
            return

    back_dir = (dir+2) % 4
    # print('dir =',dir,'back_dir =',back_dir)

    ny = y + dy[back_dir]
    nx = x + dx[back_dir]

    # 뒤쪽 방향이 벽일 경우
    if nx < 0 or ny < 0 or nx >= m or ny >= n:
        return
    elif graph[ny][nx] == '1':
        # print('nx =',nx,'ny =',ny)
        return
    # 뒤쪽 방향이 청소가 되어있는 경우
    elif graph[ny][nx] == '2':
        dfs(dir, ny, nx)
        return
    # else:
    #     dfs(dir, ny, nx)


import sys

# sys.setrecursionlimit(1000000)
cnt = 0
graph = []
dy = [-1,0,1,0]
dx = [0,1,0,-1]
n, m = map(int, sys.stdin.readline().split())
y, x ,dir = map(int, sys.stdin.readline().split())
for i in range(n):
        graph.append(sys.stdin.readline().split())
# print('x =', x, 'y =',y, ' dir =',dir)

dfs(dir, y, x)
# for i in range(len(graph)):
#     print(graph[i])

print(cnt)
'''
11 10
7 4 1
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

출력 : 27
'''

