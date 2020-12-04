# 프로그래머스 - Lv2.짝지어 제거하기
from collections import deque

def solution(s):
    stack = deque()
    for t in s:
        if stack:
            while stack and t > stack[len(stack)-1]:
                stack.pop()

        stack.append(t)

    return ''.join(stack)

s = "yxyc"
print(solution(s))