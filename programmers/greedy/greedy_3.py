# 코딩테스트 연습 > 탐욕법(Greedy) > 조이스틱 (프로그래머스 level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42860

# 65 ~ 90 ( A ~ Z )
import re


def solution(name):
    answer = 0
    # pattern = re.compile("[^A]")
    answer_case = 'A' * len(name)
    idx = 0 # 현재 인덱스
    rIdx = 0 # 오른쪽 진행 인덱스
    lIdx = 0 # 왼쪽 진행 인덱스
    i = 0 # 좌우 전진 횟수
    
    while True:
        # 경계 조건
        # if pattern.search(name) == None:
        #     return answer
        if name == answer_case:
            return answer

        if name[idx] != 'A':
            answer += min(ord(name[idx]) - ord('A'), 91 - ord(name[idx]))
            name = name[:idx] + 'A' + name[idx+1:]

        rIdx += 1
        if rIdx > len(name)-1:
            rIdx = 0

        lIdx -= 1
        if lIdx < 0:
            lIdx = len(name) - 1

        i += 1
        if name[rIdx] != 'A':
            idx = rIdx
            answer += i
            i = 0

        elif name[lIdx] != 'A':
            idx = lIdx
            answer += i
            i = 0

        else:
            continue

        rIdx, lIdx = idx, idx

    return answer

name = "JAZ"
print(solution(name))