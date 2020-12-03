# 프로그래머스 - Lv1.좌석 구매

def solution(seat):
    tup_seat = list(map(tuple, seat))

    # 방법 1. set => O(n)
    # ** set의 원소로 list형은 안된다!
    # reserved = set(seat)
    # print(seat)


    # 방법 2. dict => O(n)
    dict = {}
    for i in tup_seat:
        dict[i] = 0

    return len(dict)

seat = [[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]
print(solution(seat))