def cal(arr1, arr2):
    answer = 0

    # 가장 값비싼 것을 기준으로 첫번쨰 가방부터 담는다.
    # (담을 수 있는 무게인 경우에만)
    for bag in arr2:
        for i in range(len(arr1)):
            if bag >= arr1[i][0]:
                answer += arr1[i][1]
                arr1[i][0] = 100000001
                # print(arr1)
                break


    # 결과 값어치 반환
    return(answer)

import sys

n, k = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(list(map(int, sys.stdin.readline().split())))

for i in range(k):
    arr2.append(int(sys.stdin.readline()))

# arr1.sort(key=lambda x:x[1], reverse=True)
# arr2.sort()

print(cal(arr1, arr2))




