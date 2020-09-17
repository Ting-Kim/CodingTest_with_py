def solution(n):
    global cnt # 덧셈 기호 사용 횟수
    length = str(n)
    if len(length) == 1:    # 경계 조건
        return [cnt, n]

    half_index = len(str(n)) // 2
    a = str(n)[:half_index]
    b = str(n)[half_index:]
    c = str(n)[:half_index+1]
    d = str(n)[half_index+1:]

    cnt += 1

    if len(length) <= 2:
        # print('cnt : ', cnt, '\tn = ', n)
        return solution(int(length[0]) + int(length[1]))
    else:
        if b[0] == '0' and d[0] != '0':
            return solution(int(c)+int(d))
        elif b[0] != '0' and d[0] == '0':
            return solution(int(a) + int(b))
        elif b[0] == '0' and d[0] == '0':
            index = half_index + 1
            while b[0] == '0':
                index += 1
                a = length[:index]
                b = length[index:]
            # print('cnt : ', cnt, '\tn = ', int(a)+int(b))
            return solution(int(a)+int(b))
        else:
            if int(a) + int(b) >= int(c) + int(d):
                # print('cnt : ', cnt, '\tn = ', int(c)+int(d))
                return solution(int(c)+int(d))
            else:
                # print('cnt : ', cnt, '\tn = ', int(a)+int(b))
                return solution(int(a)+int(b))

cnt = 0
print(solution(73425))
