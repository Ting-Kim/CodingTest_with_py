def solution(v):
    answer = []
    arr = []
    for i in range(len(v[0])):
        for element in v:
            if element[i] not in arr:
                arr.append(element[i])
            else:
                arr.remove(element[i])
        if len(arr) != 1:
            return -1
        else:
            answer.append(arr[0])
        arr.clear()


    return answer

v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))