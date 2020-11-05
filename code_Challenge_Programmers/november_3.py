import itertools
def solution(a):
    answer = 0
    i = 4
    double_check=False

    while i <= len(a):
        arr = itertools.combinations(a, i)
        new_list = []
        for v in list(arr):
            if v not in new_list:
                new_list.append(v)
        # print(new_list)

        for element in new_list:
            # print(element)
            j = 0
            k = 2
            check = []
            while k <= len(element):
                check.append(set(element[j:k]))
                j+=2
                k+=2

            # print(check)
            for q in range(len(check)-1):
                if (check[q]&check[q+1]) == set():
                    # print("겹치는게 없어.")
                    double_check = True
                    break

            if double_check == True:
                double_check = False
                continue

            temp = len(element)
            if temp > answer:
                answer = temp

        i += 2

    return answer

a = [5,2,3,3,5,3]
print(solution(a))