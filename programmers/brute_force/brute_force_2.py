# 코딩테스트 연습 > 완전탐색 > 소수 찾기 (프로그래머스 level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42839

import itertools
import math

def solution(numbers):
    answer = 0
    arr = []
    arr1 = []

    for i in range(1,len(numbers)+1):
        arr += set(itertools.permutations(numbers,i))
    # print(arr)      # [('1',), ('7',), ('1', '7'), ('7', '1')]

    for i in range(len(arr)):
        number = int(''.join(arr[i]))
        # print('후보 : ', number)
        arr1.append(number)

    arr1 = set(arr1)

    for i in range(len(arr1)):
        n = arr1.pop()
        check = False
        if n== 1 or n == 0:
            continue


        for j in range(2, math.floor(math.sqrt(n))+1):
            if n % j == 0:
                check = True
                # print('소수가 아님!', n)
                break
        if not check:
            # print('소수임!! ', n)
            answer += 1

    return answer

numbers = '011'
print(solution(numbers))