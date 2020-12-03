# 프로그래머스 - Lv2.스킬트리

def solution(skill, skill_trees):
    answer = len(skill_trees)
    order = list(skill)

    for x in skill_trees:
        i = 0
        for m in x:
            if m in order:
                if order[i] == m:
                    i += 1
                else:
                    answer -= 1
                    # print(x, ' 차례: ', m)
                    break

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))