# 코딩테스트 연습 > 정렬 > 가장 큰 수 ( level 2 )
# https://programmers.co.kr/learn/courses/30/lessons/42746

import itertools

def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers_string = [element*3 for element in numbers]

    # numbers_string.sort(key=lambda x:x[0],reverse=True)
    numbers_string.sort(reverse=True)


    for i in range(len(numbers_string)):
        string = len(numbers_string[i]) // 3
        numbers_string[i] = numbers_string[i][:string]

    # print(numbers_string)

    answer = int(answer.join(numbers_string))


    return str(answer)

numbers = [0,0]
print(solution(numbers))

'''
11번 테스트케이스만 통과x
주의해야할 테스트 케이스
 - 입력 : [0,0]
 - 출력 : 0
 
해결법?
    정답 출력은 문자열이므로, 계속 00이 나오는 문제가 있었다.
    그래서 정답을 출력하기 전에 int로 변환 후 return 값에는 다시 str로 감싸줌. 
'''