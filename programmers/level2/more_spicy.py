from collections import deque


def solution(scoville, K):
    answer = 0
    scoville.sort()
    # scoville을 담은 큐를 만듬
    queue = deque(scoville)
    # 비어있는 wait 큐를 만듬
    wait = deque()
    try:
        while True:
            if queue:
                if queue[0] >= K:
                    if wait:
                        if wait[0] >= K:
                            break
                    else:
                        break
            else:
                if wait[0] >= K:
                    break

            new_food = 0

            # 큐의 첫째 element와 wait element 비교해서 작은걸 꺼냄
            # 또 비교해서 꺼냄

            for i in range(1, 3):
                if wait:
                    if queue:
                        if queue[0] > wait[0]:
                            element = wait.popleft()
                        else:
                            element = queue.popleft()
                    else:
                        element = wait.popleft()
                else:
                    element = queue.popleft()

                # 꺼낸 것들을 first, second로 지정해서 스코빌 지수 연산
                new_food += element * i

            answer += 1

            # 연산 결과는 wait 큐에 push
            wait.append(new_food)

    except:
        return -1


    return answer

scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))