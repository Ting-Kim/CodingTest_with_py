import math

def solution(brown, red):
    answer = []
    sum = brown + red
    red_sqr = int(float(math.sqrt(red)))
    for i in range(red, red_sqr-1, -1):
        if red % i == 0:
            a = i
            b = red // i
            if (a+2) * (b+2) == sum:
                answer.append(a+2)
                answer.append(b+2)
                return answer

    return -1

brown = 10
red = 2
print(solution(brown, red))