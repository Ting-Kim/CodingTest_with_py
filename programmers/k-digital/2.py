from collections import deque

def solution(arr1, arr2):
    answer = 0
    flush = -1
    flag = False
    arr_dict1 = {}
    arr_dict2 = {}
    for val in arr1:
        try:
            arr_dict1[val] += 1
        except:
            arr_dict1[val] = 1
    arr_new1 = list(arr_dict1.keys())
    len_arr_new1 = len(arr_new1)

    for val in arr2:
        try:
            arr_dict2[val] += 1
        except:
            arr_dict2[val] = 1
    arr_new2 = list(arr_dict2.keys())
    len_arr_new2 = len(arr_new2)

    for i in range(len_arr_new1):
        if arr_new1[i][0] == ")":
            continue
        for j in range(len_arr_new2):
            if (len(arr_new1[i]) + len(arr_new2[j])) % 2 != 0:
                continue

            check = arr_new1[i] + arr_new2[j]

            stack = deque()
            for index in range(len(check)):
                if check[index] == "(":
                    stack.append(check[index])
                else:
                    if stack:  # 스택이 비어있지 않다면
                        if stack[-1] == "(":
                            flush = stack.pop()
                    else:  # 스택이 비어있으면
                        flag = True
                        break  # 에러 발생
            if flag or stack:
                flag = False
                continue
            answer += arr_dict1[arr_new1[i]] * arr_dict2[arr_new2[j]]

    return answer

arr1 = ["()", "(()", "(", "(())"]
arr2 = 	[")()","()", "(())", ")()"]
print(solution(arr1,arr2))