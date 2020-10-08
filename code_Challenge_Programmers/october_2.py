def solution(arr):

    return list(division(arr))

def division(arr):
    a, b = 0, 0
    group = []
    arr1 = [[arr[j][i] for i in range(len(arr) // 2)] for j in range(len(arr[0]) // 2)]
    arr2 = [[arr[j][i] for i in range(len(arr) // 2)] for j in range(len(arr[0]) // 2, len(arr))]
    arr3 = [[arr[j][i] for i in range(len(arr) // 2, len(arr))] for j in range(len(arr[0]) // 2)]
    arr4 = [[arr[j][i] for i in range(len(arr) // 2, len(arr))] for j in range(len(arr[0]) // 2, len(arr))]
    group.append(arr1)
    group.append(arr2)
    group.append(arr3)
    group.append(arr4)

    # print(arr1)
    # print(arr2)
    # print(arr3)
    # print(arr4)

    for arrays in group:

        check = [False, False]

        for element in arrays:
            for i in range(2):
                if i in element:
                    check[i] = True

        if check == [True, True]:
            c, d = division(arrays)
            a += c
            b += d

        elif check[0] == True:
            a += 1
        else:
            b += 1

    return a,b

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# print(solution(arr))

'''
1 1 0 0 
1 0 0 0 
1 0 0 1
1 1 1 1


'''