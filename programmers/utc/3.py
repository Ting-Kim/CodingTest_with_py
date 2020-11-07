def solution(money, expected, actual):
    answer = -1
    go_money = 100

    for i in range(len(expected)):
        if expected[i] != actual[i]: # 졌을 때
            money -= go_money
            if money < go_money*2:
                go_money = money
            else:
                go_money *= 2

        else: # 이겼을 때
            money += go_money
            go_money = 100
        # print("남은돈 : ", money)
        # print("배팅 금액 : ", go_money)
        # print()

    answer = money

    return answer

money = 1500
expected = ['H', 'H', 'H', 'T', 'H']
actual = ['T', 'T', 'T', 'H', 'T']
print(solution(money,expected,actual))