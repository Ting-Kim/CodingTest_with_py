def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer

A = [1,2,5,3,7,9]
B = [3,4,0,12,0,43]
print(solution(A, B))