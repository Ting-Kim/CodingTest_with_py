from itertools import combinations

def solution(m, weights):
    answer = 0
    arr = []
    for i in range(2, len(weights)+1):
        arr += list(combinations(weights,i))
        if weights[i-2] == m:
            answer += 1
            continue
    # print(arr)
    sum = 0
    for group in arr:
        # if group == m:
        #     answer += 1
        #     continue

        for element in group:
            sum += element
            if sum > m:
                break

        if sum == m:
            answer += 1
        sum = 0


    return answer

m = 3000
weights = 	[500, 1500, 2500, 1000, 2000]
print(solution(m, weights))