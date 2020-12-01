class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    '''* 구현해야하는 부분 *'''
    def popAt(self, pos):
        # pos (인덱스) 번째의 node 삭제
        # 예외 처리를 잘해줘야 한다(구석값들)
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        # 삭제하려는 노드가 첫번째
        if pos == 1:
            curr = self.head
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                # curr = self.head
                self.head = curr.next

        # 삭제하려는 노드가 마지막
        elif pos == self.nodeCount:
            prev = self.getAt(self.nodeCount-1)
            curr = self.tail
            prev.next = None
            self.tail = prev

        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next

        # 총 노드 수 감소
        self.nodeCount -= 1
        # 삭제된 노드 데이터 출력
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0