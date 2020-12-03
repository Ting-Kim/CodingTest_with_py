# 프로그래머스 - Lv2.짝지어 제거하기

'''방법 3 : 스택 + 스택 사용 => 성공 !'''
from collections import deque

def solution(s):
    stack1 = deque(list(s))
    stack2 = deque()

    while stack1:
        if stack2:
            if stack2[len(stack2)-1] == stack1[len(stack1)-1]:
                stack1.pop()
                stack2.pop()
                continue
        stack2.append(stack1.pop())

    return 1 if not stack2 else 0

'''방법 2: 큐 + 스택 조합 => 시간 초과 실패'''
# def solution(s):
#     queue1 = deque(list(s))
#     queue2 = deque()
#     flag = True
#     while queue1 or queue2 and flag:
#         flag = False
#         while queue1:
#             a = queue1.popleft()
#             if queue1:
#                 b = queue1[0]
#                 if a == b :
#                     queue1.popleft()
#                     flag = True
#                     continue
#             queue2.append(a)
#
#         if queue2 and flag:
#             queue1, queue2 = queue2, queue1
#
#     return 1 if not queue1 and not queue2 else 0

'''방법 1: 반복 완전탐색'''
# def solution(s):
#     lst = list(s)
#     i = 0
#     while lst and i < len(lst)-1:
#         if lst[i] == lst[i+1]:
#             lst = lst[:i] + lst[i+2:]
#             i = 0
#         else:
#             i += 1
#
#     return 1 if not lst else 0


s = "baabaa"
print(solution(s))