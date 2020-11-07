def solution(n, board):
    answer = 0
    arr = [[] for element in board for element1 in board]
    arr.insert(0, [0,0])
    width = len(board)
    for i in range(width):
        for j in range(width):
            index = board[i][j]
            arr[index].append(i)
            arr[index].append(j)

    # print(arr)  # [[0, 0], [2, 1], [1, 1], [0, 0], [2, 0]
                # , [0, 1], [0, 2], [1, 2], [2, 2], [1, 0]]


    for i in range(len(arr)-1):
        y1 = arr[i][0]
        y2 = arr[i+1][0]
        x1 = arr[i][1]
        x2 = arr[i+1][1]
        if y1 < y2:
            answer += min(abs(y1-y2),  abs(y1+(width-y2)))
        else:
            answer += min(abs(y1-y2), abs(y2+(width-y1)))
        if x1 < x2:
            answer += min(abs(x1-x2), abs(x1+(width-x2)))
        else:
            answer += min(abs(x1-x2),abs(x2+(width-x1)))

        answer += 1
        a = min(abs(y1-y2), abs(y1+(width-y2)))
        b = min(abs(x1-x2), abs(x1+(width-x2)))

    return answer


n = 4
board = [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]
print(solution(n,board))