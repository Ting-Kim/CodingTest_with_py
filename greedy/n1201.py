# https://kyu9341.github.io/algorithm/2020/03/18/algorithm1201/
# acmicpc 1201

# m+k-1 <= n < m*k+1
'''
    1. 1부터 N까지 수를 오름차순으로 적는다.
    2 수를 M등분한다. 이 때, 그룹에 들어있는 수는 K보다 작거나 같아야 하며,
       적어도 한 그룹은 들어있는 수의 개수가 K이어야 한다.
    3. 각 그룹에 들어있는 수의 순서를 뒤집는다.
    4. 끝
'''
# 런타임 Err 발생. . .
# 0으로 나누는 경우가 있을 경우, divided by zero 에러 발생 가능!
def solve():
    if m+k-1 > n or n > m*k:
        print(-1)
        return 1

    arr = [i for i in range(1,n+1)]
    temp = []

    if m == 1:
        arr.reverse()
        for x in range(len(arr)):
            print('%d' % arr[x], end=' ')

        return

    t = (n-k)//(m-1) # 2

    # a+b+c = m
    a = 1   # k개가 들어있는 집합 수
    b = (n-k)%(m-1)   # t + 1 개가 들어있는 집합 수 # 0
    c = (m-1) - b   # t 개가 들어있는 집합 수 # 1

    temp.append(arr[:k])
    for i in range(1,b+1):
        first = k+(t+1)*(i-1)
        second = k+(t+1)*i
        temp.append(arr[first:second])

    for j in range(1, c+1):
        first = k+(t+1)*b+t*(j-1)
        second = k+(t+1)*b+t*j
        temp.append(arr[first:second])

    answer = []

    for element in temp:
        element.reverse()
        answer += element

    for x in range(len(answer)):
        print('%d' % answer[x], end=' ')


n, m, k = map(int, input().split())

solve()






