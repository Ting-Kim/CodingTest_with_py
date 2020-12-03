from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speed_queue = deque(speeds)
    while queue:
        distribute = 0
        for i in range(len(speed_queue)):
            queue[i] += speed_queue[i]
        while queue and queue[0] >= 100:
            queue.popleft()
            speed_queue.popleft()
            distribute += 1
        if distribute != 0:
            answer.append(distribute)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses,speeds))