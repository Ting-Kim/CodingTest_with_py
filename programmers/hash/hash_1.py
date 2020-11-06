# 코딩테스트 연습 > 해시 > 완주하지 못한 선수 (프로그래머스 level 1)
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    dic = {}
    for element in completion:
        if element in dic.keys():
            dic[element] += 1
        else:
            dic[element] = 1

    for element in participant:
        try:
            if dic[element] == 0:
                answer += element
                return answer

            dic[element] -= 1

        except:
            answer += element
            return answer

    # print(dic)

    return answer

participant = ["marina", "josipa", "nikola", "filipa", "taeho", "taeho", "hello"]
completion = ["josipa", "taeho", "taeho", "filipa", "marina", "nikola"]
print(solution(participant,completion))