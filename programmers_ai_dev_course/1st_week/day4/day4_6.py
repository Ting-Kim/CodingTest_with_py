# 프로그래머스 - Lv3.N으로 표현

def solution(N, number):
    cbn = [set() for _ in range(8)]  # n=1 ~ n=8까지의 조합 경우의수들을 모은 set을 원소로 하는 리스트

    for i in range(1, len(cbn)+1):
        # N을 1개 사용한 경우 추가
        cbn[i-1].add(int(str(N)*i))
        print('i = ', i)
        for j in range(1, i):
            for k in range(i-j,0,-1):
                # print('j,k = ', (j,k)) # (j,k) 순서쌍 확인
                for first in cbn[j-1]:
                    for second in cbn[k-1]:
                        cbn[i-1].add(first + second)
                        cbn[i-1].add(first - second)
                        cbn[i-1].add(first * second)
                        if second != 0:
                            cbn[i-1].add(first // second)

        if number in cbn[i-1]: # 조합된 갯수마다 집합에서 찾는 number가 있는지 확인
            return i

    # 8개의 집합에서 발견하지 못한다면
    return -1

N = 5
number = 12
print(solution(N,number))