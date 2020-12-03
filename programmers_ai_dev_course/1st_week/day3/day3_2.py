# # 방법 1 - O(n)
# def solution(n, lost, reserve):
#     student = [1] * (n+2)
#     for element in lost:
#         student[element] -= 1
#     for element in reserve:
#         student[element] += 1
#     for i in range(1, n+1):
#         if student[i] == 2:
#             if student[i-1] == 0:
#                 student[i-1] += 1
#             elif student[i+1] == 0:
#                 student[i+1] += 1
#
#     return len([x for x in student[1:n+1] if x > 0])

# 방법 2 - O(nlogn)
def solution(n, lost, reserve):
    answer = 0
    s = set(lost) & set(reserve)
    l = set(lost) - s # 체육복이 없는 학생 집합
    r = set(reserve) - s # 여분이 있는 학생 집합

    for element in sorted(r):
        if element-1 in l:
            l.remove(element-1)
        elif element+1 in l:
            l.remove(element+1)

    return n - len(l)

n = 5
lost = [2,4]
reserve = [3]
print(solution(n,lost,reserve))