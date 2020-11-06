# # 코딩테스트 연습 > 스택/큐 > 기능개발 (프로그래머스 level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    stack_progress = deque(progresses)
    stack_speed = deque(speeds)

    while stack_progress.__len__() != 0 :
        score = 0
        while stack_progress[0] >= 100:
            stack_progress.popleft()
            stack_speed.popleft()
            score += 1
            if len(stack_progress) == 0:
                break

        if score != 0:
            answer.append(score)

        for i in range(stack_progress.__len__()):
            stack_progress[i] += stack_speed[i]

    return answer



p = list(map(int, input().split(",")))
s = list(map(int, input().split(",")))
print(solution(p,s))

