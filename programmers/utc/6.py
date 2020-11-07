def solution(logs):
    answer = []
    arr = []
    test_list = {} # 수험번호 : [[문제번호, 문제점수], ...]
    name_amount = {} # 수험번호 : 푼 문제 수
    for i in range(len(logs)):
        arr.append(logs[i].split(" "))
        if arr[i][0] not in test_list:
            test_list[arr[i][0]] = {}

        test_list[arr[i][0]][arr[i][1]] = arr[i][2] # 수정완료
        name_amount[arr[i][0]] = 0

    name_arr = list(test_list.keys()) # 수험번호 리스트 : ['0001', '0002', '0003']


    # for i in range(len(arr)):
    #     test_list[arr[i][0]].append([arr[i][1], arr[i][2]])

    for i in range(len(name_arr)):
        answer.append(name_arr[i])
        name_amount[name_arr[i]] = len(test_list[name_arr[i]])

    print(test_list) # {'0001': {'3': '95', '5': '100', '7': '80', '8': '80', '10': '90'}, '0002': {'3': '95', '10': '90', '7': '80', '8': '80', '5': '100'}, '0003': {'99': '90'}}

    number_check = []

    # 1. 두 수험자가 푼 문제 수가 같다. 단, 푼 문제 수가 5 미만인 경우는 제외한다.
    # 2. 두 수험자가 푼 문제의 번호가 모두 같다.
    for i in range(len(name_arr)):
        insert_element = list(test_list[name_arr[i]].keys())
        insert_element.sort()
        number_check.append(insert_element)

    number_check_new = []
    abnormal = []
    for i in range(len(number_check)):
        if len(number_check[i]) < 5 or number_check[i] not in number_check:
            number_check_new.append(number_check[i])
        else:
            if number_check[i] not in abnormal:
                abnormal.append(number_check[i])

    for i in range(len(number_check_new)):
        index = number_check.index(number_check_new[i])
        if number_check_new[i] in number_check:
            answer.pop(index)

    print(abnormal)
    print(number_check_new)

    # 3. 두 수험자가 푼 문제의 점수가 모두 같다.
    for i in range(len(answer)):
        for j in range(i, len(answer)):
            for k in range(len(abnormal)):
                if test_list[answer[i]][abnormal[k]] != test_list[answer[j]][abnormal[k]]:
                    pass  # 중단


    return answer


logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
print(solution(logs))