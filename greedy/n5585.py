# greedy problem no.2
# acmicpc.net 5585번 거스름돈

# 거스름돈 종류 : 500 / 100 / 10 / 5 / 1
def cal(money, arr):
    count = 0
    for element in arr:
        if money // element != 0:
            n = money // element
            money %= element
            count += n
    return count

receive = 1000 - int(input())  # 거스름돈
arr = [500, 100, 50, 10, 5, 1]
print(cal(receive, arr))


