def solution(boxes):
    remains = []
    cnt = 0

    for i in range(len(boxes)):
        remains += boxes[i]

    for i in range(len(remains)):
        for j in range(i+1, len(remains)):
            if remains[i] == remains[j] and remains[i] != 0 and remains[j] != 0:
                # print(remains[i])
                remains[i] = 0
                remains[j] = 0
                cnt += 1
                continue

    # print('cnt : ',cnt)
    # print('len(boxes) : ', len(boxes))
    if len(boxes) >= cnt:
        return len(boxes)-cnt
    else:
        return 0


print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))