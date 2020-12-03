def solution(participant, completion):
    participant_dict = {}

    ''' 더 좋은 방법
    participant_dict[element] = d.get(element, 0) + 1
    '''
    for element in participant:
        if element in participant_dict:
            participant_dict[element] += 1
        else:
            participant_dict[element] = 1

    print('체크 : ', participant_dict.items())
    print('체크!! ', [k for k, v in participant_dict.items()])
    for element in completion:
        participant_dict[element] -= 1

    '''
    dnf = [k for k, v in participant_dict.items() if v > 0] # 시간 복잡도는 participant 리스트 크기에 비례함
    return dnf[0]
    '''
    for name in participant:
        if participant_dict[name] != 0 :
            return name

    return -1

    # return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))