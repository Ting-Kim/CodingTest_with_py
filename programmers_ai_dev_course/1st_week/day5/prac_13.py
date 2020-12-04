# 프로그래머스 - Lv2.문자열 압축 사본

from collections import deque
# 최대공약수
def solution(s):
    answer = len(s)
    length = len(s)
    lst_split = deque() # 자른 문자열 집합 스택
    stack = deque() # 옮길 스택

    for i in range(1, length // 2 + 1):
        # 약수 갯수에 따라 배열에 split 해서 담고
        # print('# ', i, ' 개 단위로 쪼갰을 때------' )
        for j in range(0, length, i):
            lst_split.append(s[j:i+j])
        # print('lst_split = ',lst_split)

        cal = 0
        # split 한 배열로 반복 시행
        while lst_split:
            duplicated = 1 # 압축한 횟수 저장 변수
            # 빈 스택에 옮겨 담는 과정에서 스택 최상단 값과 비교하여 같다면
            while stack and stack[len(stack)-1] == lst_split[0]:
                duplicated +=1
                # print('@@   ', stack)
                # 담지 않고 대기 스택에서만 제외(while) (대신 덩어리 마다 number += 1)
                lst_split.popleft()
                if not lst_split:
                    break

            if duplicated == 1:
                stack.append(lst_split.popleft())
            else:
                cal += len(str(duplicated))

        # print('stack = ', stack)

        while stack:
            cal += len(stack.pop())

        # print(i, ' 일 때 총 길이 : ', cal)
        if answer > cal:
            answer = cal
        stack.clear()
        lst_split.clear()

    return answer

s = "aaaaaaaaaaaaaaaaaaaaaaaaaabbaccccccccccccccccccc"
print(solution(s))