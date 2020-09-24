def search(arr,x,y):
    # arr [미로]
    # x,y -> 시작점(2,2 부터)
    if arr[x][y] == 2:
        arr[x][y] = 9
        return

    if arr[x][y] == 0:
        arr[x][y] = 9

    if arr[x][y+1] != 1:
        search(arr,x,y+1)
        return
    else:
        if arr[x+1][y] != 1:
            search(arr,x+1,y)

arr = [list(map(int, input().split())) for i in range(10)]

search(arr, 1, 1)

for i in range(10):
    for j in range(10):
        print(arr[i][j], end= ' ')
    print()
# print(arr)



