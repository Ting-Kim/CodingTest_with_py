def solution(max_weight, specs, names):
    answer = 1
    curr_weight = 0
    specs_dict = {}
    # specs dictinary 화
    for spec in specs:
        specs_dict[spec[0]] = int(spec[1])
    for element in names:
        # 물품 담으려고 할 때 무게 초과 시
        # max_weight 보다 무거운 물품일 경우 패스
        if specs_dict[element] > max_weight:
            continue
        if curr_weight + specs_dict[element] > max_weight:
            answer += 1
            curr_weight = 0

        curr_weight += specs_dict[element]

    return answer

max_weight = 300
specs = [["toy",70], ["snack", 200]]
names = ["toy", "snack", "snack"]
print(solution(max_weight,specs,names))