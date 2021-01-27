# lv3. N으로 표현
# DP(동적 프로그래밍)

def solution(N, number):
    answer = 0
    num_group = []
    # index = 0은 더미
    for i in range(9):
        num_group.append(set([int(str(N) * i if i != 0 else 0)]))
        
    # N을 몇개 사용하는지
    for i in range(2, 9):
        # 1개면 , 2개면 (1,1), 3개면 (1,2), (2,1), 4개면 (1,3), (2,2), (3,1)  . . . .
        for j in range(1, i):
            for k in num_group[j]:
                for l in num_group[i - j]:
                    num_group[i].add(k + l)
                    num_group[i].add(k - l)
                    if l != 0:
                        num_group[i].add(k // l)
                    num_group[i].add(k * l)

    for idx in range(1, len(num_group)):
        if number in num_group[idx]:
            return idx

    return -1