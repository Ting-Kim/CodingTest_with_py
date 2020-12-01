class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear + 1) % self.maxCount

        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount

        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]

CQ = CircularQueue(10)
CQ.enqueue(4)
CQ.enqueue(2)
print(CQ.data)
print('peek', CQ.peek())
print('추출', CQ.dequeue())
print(CQ.data)
CQ.enqueue(7)
CQ.enqueue(8)
print(CQ.data)
print('peek', CQ.peek())
print('추출',  CQ.dequeue())
print(CQ.data)
CQ.enqueue(9)
print(CQ.data)
print('peek', CQ.peek())
print('추출', CQ.dequeue())
print(CQ.data)

