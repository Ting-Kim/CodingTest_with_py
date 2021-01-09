from itertools import combinations

# 프로그래머스 - Lv1.세 소수의 합

def solution(n):
    answer = 0

    lst = eratosthenes(n)
    lst_up = [lst[i] for i in range(2, len(lst)) if lst[i] != 0]
    print(lst_up)

    group = list(combinations(lst_up, 3))
    for element in group:
        if sum(element) == n:
            answer += 1

    return answer

def eratosthenes(n):
    lst = [i for i in range(n)]
    for i in range(2,n):
        if lst[i] == 0:
            continue
        for j in range(2*i, n, i):
            lst[j] = 0
    return lst
n = 33
print(solution(n))
