# 배터리의 가격표가 배열로 [[단위개수, 단위가격], ...] 표현되어 있다.
# n개를 구매할 때 최소 금액을 구해라. (수량 초과해도 됨)

# 그리디
def solution(n, battery):
    price_list = []
    price_checkList = []
    total = 0
    sum = 0

    # 단위 가격 리스트
    for i in range(len(battery)):
        price_list.append(battery[i][1] / battery[i][0])

    # 단위 가격 인덱스
    idx = price_list.index(min(price_list))

    # 최소 단위 가격 배터리의 단위 수량
    amount = battery[idx][0]
    # 단위가격
    price = battery[idx][1]

    # n을 넘지 않는 선까지 구매
    for i in range(amount, n, amount):
        total += price
        sum = i

    print("total = ", total)
    print("sum = ", sum)

    # 남은 갯수를 구매한 모든 경우의 가격을 리스트에 담음
    for i in range(len(battery)):
        sum_check = sum
        price_check = 0
        while sum_check < n:
            if sum_check >= n:
                break
            sum_check += battery[i][0]
            price_check += battery[i][1]

        price_checkList.append(price_check)


    print(price_checkList)

    # 그 중 최소 금액을 총 금액에 더함
    total += min(price_checkList)


    return total

n = 1
battery = [[100,100000],[3,15000],[5,15000],]
print(solution(n,battery))

