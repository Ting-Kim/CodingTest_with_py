def solution(L, x):
    # answer = 0
    lower = 0
    upper = len(L)-1
    while lower <= upper:
        middle = (lower + upper)//2
        if x == L[middle]:
            return middle
        if x < L[middle]:
            upper = middle - 1
        else:
            lower = middle + 1


    return -1

L = [2, 3, 5, 6, 9, 11, 15]
x = 6
print(solution(L,x))