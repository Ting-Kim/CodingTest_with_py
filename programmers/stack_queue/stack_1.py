# 주식가격(level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3


def solution(prices):
    # prices 를 초기 큐로 만든다
    price_queue = deque(prices)
    answer = []

    for i in range(len(prices)):
        if i == len(prices) - 1 :
            answer.append(0)
            return answer
        # 큐에서 하나를 꺼낸다
        temp = price_queue.popleft()

        # score 및 index 값 선언
        t = i+1

        # 꺼낸값보다 작은 값 나올때까지 반복 {
        while prices[t] >= temp:
            if t >= len(prices) - 1 :
                break
            #     꺼낸 값과 나머지 큐 요소들과 비교하면서 answer 값 1씩더함
            t += 1
        # }

        answer.append(t - i)

    return answer


from collections import deque

arr = list(map(int, input().split(",")))
print(solution(arr))

