def solution(s):
    answer = []
    binary_score = 0 # 이진 변환 횟수
    zero_score = 0 # 제거한 0 개수

    while True:
        # s가 '1'이 되면 break
        if s == '1':
            break
        # print("현재 s = ", s)

        before = len(s)
        s = s.replace("0", "")
        after = len(s)
        zero_score += before - after # 제거한 0의 개수 추가

        # 이진 변환 (after값)
        # s = ""
        temp = []
        while after // 2 != 0:
            # s += str(after % 2)
            temp.append(str(after%2))
            after //= 2

        temp.append(str(after))
        temp.reverse()
        s = ''.join(temp)
        binary_score += 1

    answer.append(binary_score)
    answer.append(zero_score)



    return answer

s = "110010101001"
print(solution(s))