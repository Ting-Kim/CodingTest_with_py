def truck(box, check, capacity):
    answer = 0
    room = 0
    for i in range(len(box)):
        x = box[i][0]-1
        y = box[i][1]-1
        z = box[i][2]
        m = min(check[x:y])

        if m >= z:
            answer += z
            for i in range(x,y):
                check[i] -= z

        else:
            answer += m
            for i in range(x,y):
                check[i] -= m

    return answer


n, c = map(int, input().split())
m = int(input())
box = []
check = [c for _ in range(n)]
for _ in range(m):
    box.append(list(map(int, input().split())))

# 각 list의 두번째 element를 기준으로 오름차순, 첫번째 element를 기준으로 내림차순으로 정렬
box.sort(key=lambda x:(x[1],-x[0]))
# print(box)
print(truck(box, check, c))