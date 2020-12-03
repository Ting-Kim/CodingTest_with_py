# 프로그래머스 - Lv1.대중소 괄호 짝 맞추기
from collections import deque

def solution(s):
    stack = deque()
    dict = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    try:
        for m in s:

            if m in ["(", "{", "["]:
                stack.append(m)
            else:
                if stack.pop() != dict[m]:
                    return False

        if stack:
            return False

    except:
        return False


    return True

s = "([())]"
print(solution(s))

