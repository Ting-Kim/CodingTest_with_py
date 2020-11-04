# 코딩테스트 연습 > 탐욕법(Greedy) > 체육복(level 1)
# https://programmers.co.kr/learn/courses/30/lessons/42862
# 만약 문제가 여벌의 체육복을 2장 빌려줄 수 있는 조건이었다면?

def solution(n, lost, reserve):
    # answer = 0

    for i in range(len(lost)):
        temp = lost.pop(0)
        if temp in reserve:
            reserve.remove(temp)
        else:
            lost.append(temp)


    for i in range(len(lost)):
        temp = lost.pop(0)
        temp1 = temp - 1
        temp2 = temp + 1
        if temp1 in reserve:
            reserve.remove(temp1)

        elif temp2 in reserve:
            reserve.remove(temp2)

        else:
            lost.append(temp)

    answer = n - len(lost)

    return answer


n = 8
lost = [1,3,4]
reserve = [1,3,6,7]
print(solution(n,lost,reserve))
