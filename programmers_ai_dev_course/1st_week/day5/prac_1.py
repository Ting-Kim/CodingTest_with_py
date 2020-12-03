# 프로그래머스 - Lv1.완주하지 못한 선수

def solution(participant, completion):
    dict = {}
    for key in participant:
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

    for key in completion:
        dict[key] -= 1
        
    answer = [key for key in dict if dict[key] > 0]

    if len(answer) != 1:
        return -1

    return answer[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))