# 프로그래머스 - Lv2.올바른 괄호
from collections import deque

def solution(s):
    stack = deque()

    for m in s:
        if m == '(':
            stack.append(m)
        else:
            if stack:
                if stack.pop() != '(':
                    return False
            else:
                return False

    if stack:
        return False

    return True

s = "(()("
print(solution(s))