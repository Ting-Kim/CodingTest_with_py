# 프로그래머스 - Lv2.주사위 게임

def solution(monster, S1, S2, S3):
    a = 0
    b = S1*S2*S3
    dict = {}
    for t1 in range(1,S1+1):
        for t2 in range(1,S2+1):
            for t3 in range(1,S3+1):
                dict[t1+t2+t3] = dict.get(t1+t2+t3 ,0) + 1

    for x in monster:
        a += dict.get(x-1, 0)
    return int((1-a/b)*1000)

monster = [4,9,5,8]
S1 = 2
S2 = 3
S3 = 3
print(solution(monster, S1, S2, S3))