x = [[0 for i in range(20)] for i in range(20)]


n = int(input())
# arr = []
for i in range(n):
    a, b = map(int, input().split())
    x[a][b] = 1

for i in range(1,20):
    for j in range(1,20):
        print(x[i][j], end=' ')
    print()


