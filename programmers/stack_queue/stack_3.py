# 프로그래머스 > 코딩테스트 연습 > 스택/큐 > 다리를 지나는 트럭 ( Level 2 )
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossBridgeQueue = deque([0 for i in range(bridge_length)]) # 다리를 건너는 트럭 큐
    curr_weight = 0 # 현재 다리에 올라와있는 트럭 총 무게

    while truck_weights:
        answer += 1
        bridge_out = crossBridgeQueue.popleft()
        curr_weight -= bridge_out

        if curr_weight + truck_weights[0] <= weight:
            temp = truck_weights.pop(0)
            print(temp)
            crossBridgeQueue.append(temp)
            curr_weight += temp
        else:
            crossBridgeQueue.append(0)

    while curr_weight > 0 and crossBridgeQueue:
        answer += 1
        bridge_out = crossBridgeQueue.popleft()
        curr_weight -= bridge_out

    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))