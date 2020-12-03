class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        # 원소를 마지막에 추가
        self.data.append(item)

        nodeIdx = len(self.data) - 1
        parentIdx = nodeIdx//2

        while parentIdx > 0 and self.data[parentIdx] < self.data[nodeIdx]:
            self.data[parentIdx], self.data[nodeIdx] = self.data[nodeIdx], self.data[parentIdx]
            nodeIdx = parentIdx
            parentIdx = nodeIdx//2


def solution(x):
    return 0

heap = MaxHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
if heap.data:
    print(heap.data)