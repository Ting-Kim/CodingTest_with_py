def solution(num):
    n = str(num)
    answer = n

    # 완전 탐색
    while True:
        l = len(answer)
        if l % 2 != 0: # 자릿수가 홀수일 때는 자릿수 + 1인 최솟값 반환
            print(answer)
            temp = ['1'] + ['0' for i in range(l)]
            # temp.insert(0, '1')
            answer = ''.join(temp)
            if len(answer) != 2:
                answer = int(answer)
                break
            # print(answer)
            # answer = '1' + ('0' * l)
        print(answer)
        mulA = 1
        mulB = 1

        # 맨 앞, 맨 뒤 인덱스를 통해서 두 변수에 각각 곱해준다.
        for i in range(len(answer)//2):
            mulA *= int(answer[i])
            mulB *= int(answer[-(i+1)])

        # 비교
        if mulA == mulB:
            print("mulA = ", mulA)
            print("mulB = ", mulB)
            answer = int(answer)
            break

        answer = str(int(answer)+1)


    return answer

num = 1
print(solution(num))