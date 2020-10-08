def solution(n):
    answer = []
    result = 0
    while n // 3 != 0 or n >= 3:
        a, b = division(n)
        answer.append([a,b])
        n -= b * (3**(a-1))

    if n != 0:
        answer.append([1,n])

    for i in range(len(answer)):
        result += answer[i][1] * (3**(answer[0][0]-answer[i][0]))


    # print(answer)

    return result


def division(num):
    idx = 0
    div = 0
    div += num
    while div != 0:
        div //= 3
        idx += 1

    i = 1

    if num // (3 ** (idx-1)) > 1:
        i = 2

    return idx, i

# input = 125
# print(solution(input))