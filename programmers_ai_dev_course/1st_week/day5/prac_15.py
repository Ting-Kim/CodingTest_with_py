# 프로그래머스 - Lv3.FloodFill

# def solution(n, m, image):
#
#     visit = [[False for i in range(m)] for j in range(n)] # 방문 체크용
#     bfs(0, 0, image, True, visit)
#
#     return answer
#
# def bfs(y, x, image, color_flag, visit):
#     global answer
#     print(visit)
#     # 경계 조건
#     if y < 0 or x < 0 or y > len(image)-1 or x > len(image[0])-1 or visit[y][x]:
#         # print('y = ',y, ' x = ', x)
#         return
#
#     # 종료 조건
#     # if y == len(image)-1 and x == len(image[0])-1:
#     #     return
#
#     if not color_flag:
#         answer += 1
#     visit[y][x] = True
#
#     c = True
#     d = True
#
#     a = False
#     if y+1 < len(image):
#         if image[y+1][x] == image[y][x]:
#             bfs(y+1, x, image, True, visit)
#             a = True
#     else:
#         c = False
#
#     b = False
#     if x+1 < len(image[0]):
#         if image[y][x+1] == image[y][x]:
#             bfs(y, x+1, image, True, visit)
#             b = True
#     else:
#         d = False
#
#     if c and not a:
#         bfs(y+1, x, image, False, visit)
#     if d and not b:
#         bfs(y, x+1, image, False, visit)

from collections import deque

def solution(n, m, image):
    def bfs(y, x, color):
        queue.append((y,x)) # bfs 탐색을 위한 큐에 노드 삽입
        image[y][x] = 0 # 방문 처리
        while queue:
            y1, x1 = queue.popleft()
            for dy,dx in zip(dy_, dx_):
                ny = y1 + dy
                nx = x1 + dx
                if 0 <= ny < n and 0 <= nx < m and color == image[ny][nx]:
                    queue.append((ny, nx))
                    image[ny][nx] = 0

    answer = 0
    queue = deque()
    dy_ = [0,0,1,-1]
    dx_ = [1,-1,0,0]
    for i in range(n):
        for j in range(m):
            if image[i][j] != 0:
                bfs(i, j, image[i][j])
                answer += 1

    return answer



# answer = 1
n = 2
m = 3
images = [[1, 2, 3], [3, 2, 1]]
print(solution(n,m, images))
