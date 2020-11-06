# 코딩테스트 연습 > 스택/큐 > 프린터 (프로그래머스 level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    ch = ord('a')
    # print(chr(ch+1))
    documents = [chr(ch + i) for i in range(len(priorities))]

    # 목표한 출력 문서 기호
    target = documents[location]

    break_check = True
    # print(documents)
    while priorities:
        J = priorities.pop(0)
        J_alpha = documents.pop(0)
        answer += 1

        # 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하는지 체크
        for i in range(len(priorities)):
            if J < priorities[i]:
                priorities.append(J)
                documents.append(J_alpha)
                answer -= 1
                break_check = False
                break
                # print("현재 출력 위치? >> " , element)

        if break_check == False:
            break_check = True
            continue

        # J보다 중요도가 높은게 없으니 그대로 J 인쇄 ( pop된 상태이므로 내비둠
        if J_alpha == target:
            break

    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))