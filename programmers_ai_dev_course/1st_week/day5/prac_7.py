class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        # 구현하세요
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        # 구현하세요
        if self.max_size <= self.qsize(): # max_size를 넘는다면
            return False
        if self.stack1.size() == 0:
            if self.stack2.size() == 0:
                self.stack2.push(item)
                return True
        self.stack1.push(item)
        return True

    def pop(self):
        # 구현하세요
        if self.stack2.size() != 0:
            a = self.stack2.pop()
        else:
            if self.stack1.size() == 0:
                # raise EmptyException
                return False
            while self.stack1.size() != 0:
                self.stack2.push(self.stack1.pop())
            a = self.stack2.pop()
        return a

class EmptyException(Exception):
    def __init__(self):
        super().__init__('큐가 비어있는 상태입니다.')

n, max_size = map(int, input().strip().split(' '))
myQueue = MyQueue(max_size)
for i in range(n):
    a = input().split()
    if a[0] == 'PUSH':
        print(myQueue.push(a[1]))
    elif a[0] == 'POP':
        print(myQueue.pop())
    elif a[0] == 'SIZE':
        print(myQueue.qsize())
