n, k = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(list(map(int,input().split())))

for i in range(k):
    arr2.append(int(input()))

arr1.sort(key=lambda x:x[1])
print(arr1)





