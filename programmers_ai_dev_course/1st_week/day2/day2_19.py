class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r

    '''구현'''
    def bft(self):
        # 빈 리스트, 빈 큐 초기화
        travalsal = []
        queue = ArrayQueue()

        # 루트 노드가 있다면 루트 노드를 큐에 담고 시작 / 없다면 종료
        if self.root:
            queue.enqueue(self.root)
        else:
            return []

        # 큐가 빌 때까지 시행
        while not queue.isEmpty():
            # 큐에서 dequeue하고 해당 노드 방문처리(travalsal List에 데이터 append)
            node = queue.dequeue()
            travalsal.append(node.data)

            # dequeue한 노드의 왼쪽부터 자식 노드를 큐에 push
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


        return travalsal


def solution(x):
    return 0