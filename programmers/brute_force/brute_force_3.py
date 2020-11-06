# 코딩테스트 연습 > 완전탐색 > 카펫 (프로그래머스 level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    answer = []
    for i in range(1, math.floor(math.sqrt(yellow))+1):
        if yellow % i == 0:
            h = i
            w = yellow // h
            if (w + (h+2))*2 == brown:
                answer.append(w+2)
                answer.append(h+2)
                return answer

    return answer


brown = 24
yellow = 24
print(solution(brown,yellow))