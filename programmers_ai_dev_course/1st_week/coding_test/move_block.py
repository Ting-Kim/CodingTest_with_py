from collections import deque

def solution(board):
    start_y = 0
    start_x = 1
    start_dir = 0 # 0 = horizontal, 1 = vertical
    n = len(board)
    queue = deque([((start_y, start_x, start_dir), 0)]) # y,x,dir,cnt
    visited = set([(start_y, start_x, start_dir)])

    def reachable(y, x, dir):
        arr = set()
        if dir == 0: # horizontal
            # up
            if y > 0 and x > 0 and board[y-1][x-1] != 1 and board[y-1][x] != 1:
                # 평행이동
                arr.add((y-1, x, 0))
                # 시계방향 9시 -> 12시 회전
                arr.add((y, x, 1))
                # 반시계방향 3시 -> 12시 회전
                arr.add((y, x-1, 1))

            # down
            if y < n-1 and x-1 >= 0 and board[y+1][x-1] != 1 and board[y+1][x] != 1:
                # 평행이동
                arr.add((y+1, x, 0))
                # 시계방향 3 -> 6 회전
                arr.add((y+1, x-1, 1))
                # 반시계방향 9시 -> 6시 회전
                arr.add((y+1,x, 1))

            # right
            if x < n-1 and board[y][x+1] != 1:
                # 오른쪽 1칸 전진
                arr.add((y, x+1, 0))

            # left
            if x > 1 and board[y][x-2] != 1:
                # 왼쪽 한칸 후퇴
                arr.add((y, x-1, 0))

        elif dir == 1: # vertical
            # up
            if board[y-2][x] != 1:
                arr.add((y-1, x, 1))

            if y < n-1 and board[y+1][x] != 1:
                # 아래로 한칸 전진
                arr.add((y+1, x, 1))

            if y > 0 and x > 0 and board[y-1][x-1] != 1 and board[y][x-1] != 1:
                # 평행이동
                arr.add((y, x-1, 1))
                # 시계방향 6시 -> 9시
                arr.add((y-1,x,0))
                # 반시계방향 12시 -> 9시
                arr.add((y, x, 0))

            if y > 0 and x < n-1 and board[y][x+1] != 1 and board[y-1][x+1] != 1:
                # 평행이동
                arr.add((y, x+1, 1))
                # 반시계방향 6시 -> 3시
                arr.add((y-1, x+1, 0))
                # 시계방향 12시 -> 3시
                arr.add((y, x+1, 0))

        return arr

    def bfs(visited, queue):
        while queue:
            curr, cnt = queue.popleft() # 튜플에 횟수도 담자..
            y1, x1, direction = curr
            # print(y1,x1,dir,cnt)
            # 경계조건
            if (y1, x1) == (n-1, n-1):
                return cnt
            if y1 < 0 or y1 > n-1 or x1 < 0 or x1 > n-1:
                continue

            for next in reachable(y1,x1,direction):
                if next not in visited:
                    queue.append((next, cnt+1))
                    visited.add(next)


        return cnt

    return bfs(visited, queue)



board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))