def solution(dirs):
    answer = 0
    arr = [[Node(i, j) for i in range(11)] for j in range(11)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    x, y = 5, 5 # 시작점

    for dir in dirs:
        if dir == 'U':
            if y-1 >= 0:
                if arr[y][x].u == False:
                    arr[y][x].u = True
                    answer += 1
                y += dy[0]
                x += dx[0]
                arr[y][x].d = True

        elif dir == 'D':
            if y+1 <= 10:
                if arr[y][x].d == False:
                    arr[y][x].d = True
                    answer += 1
                y += dy[1]
                x += dx[1]
                arr[y][x].u = True

        elif dir == 'R':
            if x+1 <= 10:
                if arr[y][x].r == False:
                    arr[y][x].r = True
                    answer += 1
                y += dy[2]
                x += dx[2]
                arr[y][x].l = True

        elif dir == 'L':
            if x-1 >= 0:
                if arr[y][x].l == False:
                    arr[y][x].l = True
                    answer += 1
                y += dy[3]
                x += dx[3]
                arr[y][x].r = True

    return answer

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.u = False
        self.d = False
        self.r = False
        self.l = False

dirs = "LLLLLLLLLLLLLL"
print(solution(dirs))