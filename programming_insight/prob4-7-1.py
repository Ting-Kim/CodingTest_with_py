# 스택 - 괄호 짝 맞추기 예제

from collections import deque

def match_block(input):
    stack = deque()

    for element in input:
        if element not in ['(', '{', '[', ']', '}', ')']:
            continue
        if element in ['(', '{', '[']:
            stack.append(element)
            continue
        else:
            if stack.__len__() == 0:
                return -1
            else:
                temp = stack.pop()
                if temp == '(':
                    if element != ')':
                        return -1
                elif temp == '{':
                    if element != '}':
                        return -1
                else:
                    if element != ']':
                        return -1

    if stack.__len__() == 0:
        return 0
    else:
        return -1

block = input()
answer = match_block(block)
print(answer)

