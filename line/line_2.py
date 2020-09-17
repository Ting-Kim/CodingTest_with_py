def check(queue, prior, answer):
    index = 0
    for i in range(len(prior)):
        if len(prior) > 0 and len(queue) > 0:
            if prior[index] == queue[len(queue) - 1]:
                answer.append(queue.pop())
                prior.remove(prior[index])
                check(queue, prior, answer)

            elif prior[index] == queue[0]:
                answer.append(queue.popleft())
                prior.remove(prior[index])
                check(queue, prior, answer)

            else:
                index += 1
    return

def solution(ball, order):
    answer = []
    prior = []
    order.reverse()
    queue = deque(ball)
    element = 0



    while queue:
        check(queue, prior, answer)

        if len(order) > 0:
            element = order.pop()

            if element == queue[len(queue)-1]:
                answer.append(queue.pop())
            elif element == queue[0]:
                answer.append(queue.popleft())
            else:
                prior.append(element)

    return answer

from collections import deque

print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))