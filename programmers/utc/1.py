

def solution(grades, weights, threshold):
    answer = 0

    grade_list = {
        "A+":10,
        "A0" : 9,
        "B+" : 8,
        "B0" : 7,
        "C+" : 6,
        "C0" : 5,
        "D+" : 4,
        "D0" : 3,
        "F" : 0
    }

    for i in range(len(grades)):
        answer += grade_list[grades[i]] * weights[i]

    answer -= threshold

    return answer
grades = ["B+","A0","C+"]
weights = [6,7,8]
threshold = 200
print(solution(grades,weights,threshold))