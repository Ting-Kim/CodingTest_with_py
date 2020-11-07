def solution(n, horizontal):
    answer = [[0 for i in range(n)] for i in range(n)]
    dy = [1, 0, -1]
    dx = [1, 0, -1]
    nx = 0
    ny = 0

    while ny < n-1 or nx < n-1:
        # 우측 한칸 가면 아래 남서 방향
        if horizontal == True:
            y = ny
            x = nx
            nx += 1
            print(ny,nx)
            answer[ny][nx] = answer[y][x] + 1
            while ny < n-2 and nx > 0:
                # 남서 전진
                y = ny
                x = nx
                ny = ny + dy[0]
                nx = nx + dx[2]
                print(nx)
                answer[ny][nx] = answer[y][x] + 2
            horizontal = False

        # 아래 한칸 가면, 북동 방향
        if horizontal == False:
            y = ny
            x = nx
            ny += 1
            answer[ny][nx] = answer[y][x] + 1
            while ny > 0 and nx < n-2:
                # 북동 전진
                y = ny
                x = nx
                ny = ny + dy[2]
                nx = nx + dx[0]
                answer[ny][nx] = answer[y][x] + 2
            horizontal = True

    # try:
    #     while ny < n-1 or nx < n-1:
    #         # 우측 한칸 가면 아래 남서 방향
    #         if horizontal == True:
    #             y = ny
    #             x = nx
    #             nx += 1
    #             answer[ny][nx] = answer[y][x] + 1
    #             while ny < n-1 and nx > 0:
    #                 # 남서 전진
    #                 y = ny
    #                 x = nx
    #                 ny = ny + dy[0]
    #                 nx = nx + dx[2]
    #                 print(nx)
    #                 answer[ny][nx] = answer[y][x] + 2
    #             nx += 1 # 아래한칸 전진
    #             answer[ny][nx] = answer[y][x] + 1
    #
    #             horizontal = False
    #
    #
    #         # 아래 한칸 가면, 북동 방향
    #         if horizontal == False:
    #             y = ny
    #             x = nx
    #             ny += 1
    #             answer[ny][nx] = answer[y][x] + 1
    #             while ny > 0 and nx < n-1:
    #                 # 북동 전진
    #                 y = ny
    #                 x = nx
    #                 ny = ny + dy[2]
    #                 nx = nx + dx[0]
    #                 answer[ny][nx] = answer[y][x] + 2
    #             y = ny
    #             x = nx
    #             ny += 1# 우측 한칸 전진
    #             answer[ny][nx] = answer[y][x] + 1
    #             horizontal = True
    # except:
    #     print(answer)
    return answer


n = 4
horizontal = True

print(solution(n,horizontal))