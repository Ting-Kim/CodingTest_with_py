def solution(d, budget):
    answer = 0
    d.sort()
    i = 0
    while i <= len(d)-1 and budget >= d[i]:
        answer += 1
        budget -= d[i]
        i += 1

    return answer


d = [2,2,3,3]
budget = 10
print(solution(d,budget))